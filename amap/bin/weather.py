#!/usr/bin/env python3
"""Amap weather query via the stored custom.amap credential.

Usage: weather.py [adcode] [--forecast]
  adcode defaults to 440600 (Foshan). Use --forecast for 3-day outlook.
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import (
    url_with_surrogate_query_param,
    read_json_response,
)

HOSTS = ["restapi.amap.com"]


def fetch(adcode: str, extensions: str) -> dict:
    base = (
        "https://restapi.amap.com/v3/weather/weatherInfo"
        f"?city={adcode}&extensions={extensions}&output=JSON"
    )
    url = url_with_surrogate_query_param(
        base, "custom.amap", entry_name="access_token", allowed_hosts=HOSTS
    )
    req = urllib.request.Request(url, headers={"User-Agent": "muse-amap-skill/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return read_json_response(resp)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    adcode = args[0] if args else "440600"
    forecast = "--forecast" in sys.argv

    try:
        live = fetch(adcode, "base")
    except Exception as e:
        print(f"请求失败: {e}", file=sys.stderr)
        return 1
    if live.get("status") != "1":
        print(f"高德返回错误: {live.get('info')} ({live.get('infocode')})", file=sys.stderr)
        return 1

    l = live["lives"][0]
    print(f"{l['province']}{l['city']} 实况（{l['reporttime']} 发布）")
    print(f"天气：{l['weather']}，{l['temperature']}°C，{l['winddirection']}风{l['windpower']}级，湿度{l['humidity']}%")

    if forecast:
        fc = fetch(adcode, "all")
        if fc.get("status") == "1":
            print("\n未来预报：")
            for c in fc["forecasts"][0]["casts"]:
                print(
                    f"{c['date']} 周{c['week']}：白天{c['dayweather']} {c['daytemp']}°C / "
                    f"夜间{c['nightweather']} {c['nighttemp']}°C，"
                    f"{c['daywind']}风{c['daypower']}级"
                )
    return 0


if __name__ == "__main__":
    sys.exit(main())

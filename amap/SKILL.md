---
name: "amap"
description: "Use Amap when the user asks for Amap or this provider's API."
---

# Amap

## Purpose
Use Amap with the user-connected `custom.amap` credential.

## Tooling
Add service-specific CLIs under `~/workspace/skills/amap/bin/`.

- `bin/weather.py [adcode] [--forecast]` — weather lookup; adcode defaults to
  440600 (Foshan). `--forecast` adds the 3-day outlook. City adcodes follow
  Amap's standard (e.g. 440605 桂城, 440600 佛山, 440100 广州).

Python CLIs must import `/opt/hatch/skills/skill-creator/bin/dynamic_credentials.py` and call `add_surrogate_to_request(...)`, `url_with_surrogate_query_param(...)`, or `url_with_surrogate_path_segment(...)` before authenticated requests, matching where the provider reads the key. If they use `urllib`, read JSON responses with `read_json_response(resp)` from the same helper instead of calling `resp.read()` directly. They must send only `hsurr:*` values, and only to the hosts below.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, call `credentials.request_api_access` with `reconnect` to replace it. The connector is stored as `custom.amap`.

## Operating Rules
1. Use this skill when the user asks for Amap or this provider's API.
2. Restrict authenticated requests to: restapi.amap.com.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.

# MEMORY（公开版 · 已脱敏）

个人 AI 助手运行手册。含内部路径/密钥的条目已泛化，密钥一律不进 git。

## 打卡
- 钉钉打卡脚本手动触发：按时段自动判定上下班（06:00–08:30 / 17:30–20:00），DB 去重。

## 音乐整理
- 流程：目录去重 → 元数据脚本 → 回读验证。
- API 优先级：iTunes → MusicBrainz → 文件名解析；mutagen.asf 处理 WMA。
- 质量规则：FLAC > APE > MP3 > M4A > WMA；保留 VeryCD/ZASV/GER 后缀；同名比码率。
- 触发词：整理滨崎步 / 整理音乐目录。

## 消息通道
- Telegram Bot 直调：token 放 .env（环境变量读），chat_id 放配置，绝不硬编码。

## 地图
- 国内地理编码优先高德（key 放 .env：`AMAP_API_KEY`），wttr.in 备用。

## 媒体服务（家庭服务器）
- OmniBox + PanSou：UI/PanSou 端口按配置；管理 API 用 Bearer token（放 .env）。
- 源导入：GitHub 单文件导入 + downloadProxy 走 gh-proxy.org 代理；批量连续导入会 502，按 3–5 个/批。
- 入库规则：营销推广类（带推广/返佣链接、FOMO 话术、收益无法验证的帖）只介绍不入库。

## 网盘
- 夸克网盘已授权（SVIP 到 2026-10）。CLI 必传 `--session-input` + `--session-id`；坑：search→browse、AI 助手等 24h 生效。

## 风水/玄学工具链
- 风水知识库在 skill: fengshui-study；答风水题先读该 skill，"继续学习"按 skill 内进度表推进（理论/飞星/阳宅/阴宅/商业风水/择日已完成）。
- AI 排盘：xuanxue CLI（16+ 术数）+ taibu-mcp（15 工具，MCP 协议），纯本地离线。占卜类（奇门/六爻/塔罗）正常，八字多法合参有 bug。

## 学习
- 法语早课/晚测：先读 vocab_progress.md 取进度再教/出题，教完新词追加并更新排期；勿重复已完成课次。
- Kali 学习：保留主机 Debian 服务，KVM 靶场，远程/无桌面、不重装；自动部署 + SSH 排障 + 边操作边教学。

## 网络
- AI/TikTok/Gemini/Codex/Claude 走链式代理（香港入口 → 美国落地）；出问题先看链路两跳是否都通。

## 偏好
- Headless 服务器优先 Web UI / SSH 管理，不依赖桌面 GUI；Mihomo 要 Dashboard + 订阅管理面板。
- 自动化纪律：SCAN → PLAN → DRY-RUN → EXECUTE → VERIFY；测试先行，保留原文件，删/覆需确认。
- 消息习惯：回复直接、技术给完整可执行步骤；带 [生活]/[旅行]/[法语]/[媒体] 前缀方便路由。

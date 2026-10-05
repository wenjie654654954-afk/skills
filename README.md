# skills

Bruce 的个人 AI 助手知识包：给本地模型（LM Studio 等）当人设/记忆/技能上下文用。

```
skills/
├── README.md            # 本文件
├── SOUL-public.md       # 助手人设与工作纪律（脱敏）
├── USER-public.md       # 用户画像（脱敏）
├── MEMORY-public.md     # 运行手册：工具链、流程、偏好（脱敏）
└── skills/              # 可复用 skill（从 mir Hermes 提取，密钥已剔除）
    └── agent-reach/     # YouTube / B站 / 小红书等通道能力
```

## 为什么是脱敏版

原版 MEMORY/USER 里含不适合公开的内容：API key（高德）、Apple ID 账号密码与安全问题、Telegram token/chat_id、Bearer token、内网 IP、设备序列号。这些**绝不进 git**，哪怕仓库设为 private 也只放脱敏版。

密钥放哪：`.env` / 密码管理器，需要时本地注入。

## 导入 LM Studio

把 `SOUL-public.md` + `USER-public.md` + `MEMORY-public.md` 作为 system prompt / 上下文导入；
`skills/<name>/` 按 LM Studio 的 skill 导入方式加载。

## 提取说明

skill 从 mir Hermes 的 `/root/.agents/skills/agent-reach/` 提取，提取时剔除：
cookie 文件、token、密钥、内网地址。只保留能力定义与用法文档。

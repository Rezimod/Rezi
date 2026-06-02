# Consolidated Personal Morning Hub

Replaces **Rezi**, **AI-NEWS**, and **Crypto-News** with one workflow.

## Jobs

| Job | Schedule (Tbilisi) | Source |
|-----|-------------------|--------|
| `morning_brief` | Daily 07:00 | Rezi morning briefing |
| `ai_news` | Mon & Sat 09:00 | AI-NEWS |
| `crypto_weekly` | Sun 19:00 | Crypto weekly recap |

## Secrets

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `OPENAI_API_KEY` (morning brief)
- `ANTHROPIC_API_KEY` (AI news)

## Manual run

Actions → **Personal Morning Hub** → Run workflow → pick a job.

## Migrated from

- [Rezimod/Rezi](https://github.com/Rezimod/Rezi) (this repo)
- [Rezimod/AI-NEWS](https://github.com/Rezimod/AI-NEWS) — archived
- [Rezimod/Crypto-News](https://github.com/Rezimod/Crypto-News) — archived

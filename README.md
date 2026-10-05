# Bomb Tracker Bot

A Discord bot that shows the currently active Wynncraft bombs, using data from [bombtracker-backend](https://github.com/amengdev/bombtracker-backend).

## The Bomb Tracker system

```
bombtracker (mod)  ──POST /bombs──▶  bombtracker-backend  ◀──GET /bombs/active──  bombtracker-bot
 reads game chat                      stores bombs                                  /bombs in Discord
```

| Repo | Role | Stack |
|---|---|---|
| [bombtracker](https://github.com/amengdev/bombtracker) | Detects bombs in game chat | Java, Fabric |
| [bombtracker-backend](https://github.com/amengdev/bombtracker-backend) | Stores bombs, serves active ones | Java, Spring Boot, PostgreSQL |
| **bombtracker-bot** (this repo) | Shows active bombs in Discord | Python, discord.py |

## Commands

| Command | Description |
|---|---|
| `/bombs` | Lists every active bomb with its server, who threw it, and a live countdown |
| `/ping` | Checks that the bot is online |

Example `/bombs` output:

> **Profession Speed** on **NA13** by ExamplePlayer, ends in 10 minutes
> **Profession Experience** on **NA13** by ExamplePlayer, ends in 20 minutes

## Setup

Requirements: Python 3.12 and a running [bombtracker-backend](https://github.com/amengdev/bombtracker-backend).

1. **Create the bot** at the [Discord Developer Portal](https://discord.com/developers/applications): create an application, then copy its token from the **Bot** tab.
2. **Invite it** using **OAuth2 → URL Generator** with the `bot` and `applications.commands` scopes and the **Send Messages** and **Embed Links** permissions.
3. **Install dependencies** (in a conda environment or venv):
   ```bash
   pip install -r requirements.txt
   ```
4. **Create `.env`** next to `bot.py`:
   ```
   DISCORD_TOKEN=your-bot-token
   GUILD_ID=your-server-id
   BACKEND_URL=http://localhost:8080
   ```
   The bot token is a password for your bot. Never commit it.
5. **Run it:**
   ```bash
   python bot.py
   ```

Commands are synced to the server in `GUILD_ID`, so they appear immediately.

## Disclaimer

This is a fan project and is not affiliated with Wynncraft.

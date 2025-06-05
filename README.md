# Discord AI Dev Relay

> Discord bot for sharing text messages between multiple channels.

## Prerequisites

- Python 3.8+
- [Rye](https://rye-up.com/) Python project manager

## Setup

```bash
rye install
```

> This installs both runtime and development dependencies defined in `pyproject.toml`.

> Copy the example configuration and update it with your bot token and channel IDs:

```bash
cp config.example.json config.json
```

> Edit `config.json` to add your Discord bot token and the list of channel IDs to link.

## Usage

```bash
rye run python bot.py
```

## Linting & Formatting

Before committing any changes, run:

```bash
rye run ruff --fix .
```
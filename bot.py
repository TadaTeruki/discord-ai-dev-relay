"""
Discord AI Dev Relay Bot

This bot forwards text messages posted in any of the configured channels
to all other linked channels.
"""

import json
import logging
import os

import discord

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
with open(CONFIG_PATH) as f:
    config_data = json.load(f)

DISCORD_BOT_TOKEN = config_data["discord_bot_token"]
LINKED_CHANNEL_IDS = config_data["linked_channel_ids"]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    logger.info("Logged in as %s (ID: %s)", client.user, client.user.id)


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot:
        return

    channel_id = message.channel.id
    if channel_id not in LINKED_CHANNEL_IDS:
        return

    for target_id in LINKED_CHANNEL_IDS:
        if target_id == channel_id:
            continue

        target_channel = client.get_channel(target_id)
        if target_channel is None:
            logger.warning("Linked channel %s not found", target_id)
            continue

        try:
            server_name = message.guild.name if message.guild else ""
            header = f"-# {message.author.display_name} `{server_name}`"
            if message.jump_url:
                header += f" {message.jump_url}"
            body = f"{header}\n{message.content}"
            await target_channel.send(body)
        except Exception:
            logger.exception("Failed to forward message to channel %s", target_id)


def main() -> None:
    client.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()

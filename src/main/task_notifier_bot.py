"""
This script implements a simple Discord bot that sends a message to a specific channel upon startup, based on the job status provided.  # pylint: disable=line-too-long
"""

# %% Importing necessary modules and functions
import argparse
import json
import os
import sys

import discord

# Define the base directory path for configuration files
BASE_PATH = "/Users/silver/Discord-Bot"

# %% Parse command-line arguments
# Create an argument parser to accept only job_status as input from the command line
parser = argparse.ArgumentParser(description="Process Task Notifier Bot in Discord.")
parser.add_argument(
    "job_status",
    type=str,
    help="The status of the job (e.g., 'success', 'failed', etc.)",
)
args = parser.parse_args()

# %% Initialize and create Client instance
# Set up intents to receive message content and create a Discord client instance
intents = discord.Intents.default()
intents.message_content = True  # Enable the permission to get message content
client = discord.Client(intents=intents)


# When the client is ready and connected, send the message automatically
@client.event
async def on_ready():
    """Handles sending messages to the designated channel when the bot is ready."""

    print(
        f"Task Notifier Bot is logged in as {client.user}"
    )  # Display bot login info in the console

    # Read the Channel ID file
    channel_id_config_path = os.path.join(BASE_PATH, "configs/channel_id.json")
    with open(channel_id_config_path, encoding="utf-8") as channel_config_file:
        channel_data = json.load(channel_config_file)

    # Get the channel ID from the loaded data
    channel_id = channel_data.get("TASK_NOTIFIER_BOT_CHANNEL_ID")
    if not channel_id:
        print(
            f"Error: TASK_NOTIFIER_BOT_CHANNEL_ID not found in {channel_id_config_path}."
        )
        sys.exit(1)

    # Retrieve the channel object using the channel ID
    channel = client.get_channel(int(channel_id))
    if not channel:
        print("Error: Channel not found.")
        sys.exit(1)

    # Send the corresponding message based on the job_status
    if args.job_status == "success":
        await channel.send("🎉 Job Completed Successfully!")  # type: ignore
    elif args.job_status == "failed":
        await channel.send("⚠️ Job Failed!")  # type: ignore
    else:
        await channel.send(f"❗ Unrecognized Job Status: {args.job_status}")  # type: ignore

    print("Message sent. Closing bot...")

    # Close the client after sending the message
    await client.close()


# %% Load the token file
# Load the bot token from the bot_token.json file
bot_token_config_path = os.path.join(BASE_PATH, "configs/bot_token.json")
with open(bot_token_config_path, encoding="utf-8") as token_config_file:
    token_data = json.load(token_config_file)

# Retrieve the TASK_NOTIFIER_BOT_TOKEN from the loaded token data
task_notifier_token = token_data.get("TASK_NOTIFIER_BOT_TOKEN")
if not task_notifier_token:
    print(f"Error: TASK_NOTIFIER_BOT_TOKEN not found in {bot_token_config_path}.")
    sys.exit(1)

# Run the Discord client with the provided token
client.run(task_notifier_token)

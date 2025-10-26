import os
import time
import asyncio
import logging
import discord
import Jetson.GPIO as GPIO

# ───────────────────────────────
# Logging設定（すべてstdoutへ出す）
# ───────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "0"))

# ───────────────────────────────
# GPIO設定
# ───────────────────────────────
GPIO.setmode(GPIO.BOARD)
PIN = 32
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # ←安定化のため追加

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
door_state = "不明"

# ───────────────────────────────
# チャンネル通知
# ───────────────────────────────
async def notify_channel(message: str):
    if CHANNEL_ID == 0:
        logging.info(f"[NO_CHANNEL] {message}")
        return
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message)
    else:
        logging.warning("Channel not found. Check CHANNEL_ID.")

# ───────────────────────────────
# 起動イベント
# ───────────────────────────────
@client.event
async def on_ready():
    global door_state
    logging.info(f" Logged in as {client.user}")

    try:
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            synced = await tree.sync(guild=guild)
            logging.info(f"Guild commands synced: {[cmd.name for cmd in synced]}")
        else:
            synced = await tree.sync()
            logging.info(f"Global commands synced: {[cmd.name for cmd in synced]}")
    except Exception as e:
        logging.error(f"Command sync failed: {e}")

    last_state = GPIO.input(PIN)
    door_state = "閉" if last_state == GPIO.LOW else "開"
    logging.info(f"初期状態: {door_state}")

    while True:
        current_state = GPIO.input(PIN)
        if current_state != last_state:
            if current_state == GPIO.LOW:
                door_state = "閉"
                msg = "ドアが閉まりました"
            else:
                door_state = "開"
                msg = "ドアが開きました"
            logging.info(msg)
            await notify_channel(msg)
            last_state = current_state
        await asyncio.sleep(0.5)

# ───────────────────────────────
# /status コマンド
# ───────────────────────────────
@tree.command(name="status", description="現在のドア状態を表示します")
async def status_command(interaction: discord.Interaction):
    msg = f"現在のドアの状態は「{door_state}」です。"
    logging.info(f"/status → {msg}")
    await interaction.response.send_message(msg)

# ───────────────────────────────
# Bot 起動
# ───────────────────────────────
client.run(TOKEN)

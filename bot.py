import discord
from datetime import datetime
from zoneinfo import ZoneInfo
import os


TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

# カウントダウンする日付（日本時間）
TARGET_YEAR = 2026
TARGET_MONTH = 3
TARGET_DAY = 16

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)

    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    target = datetime(TARGET_YEAR, TARGET_MONTH, TARGET_DAY)

    diff = target - now
    days = diff.days

    if days > 0:
        message = f"横浜旅行日まで **あと {days} 日だよ！"
    elif days == 0:
        message = "🎉当日だよ！！"

    await channel.send(message)
    await client.close()

client.run(TOKEN)

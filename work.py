import discord
import os
from dotenv import load_dotenv

load_dotenv()

SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

# intent: bot需要接收的事件種類
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"阿農已上線：{client.user}")

@client.event
async def on_message(message):
    # message.author.bot: boolean
    # 發出該訊息的作者是否為bot
    if message.author.bot:
        return
    
    # 排除公告來源的頻道的訊息
    if message.channel.id != SOURCE_CHANNEL_ID:
        return
    
    target_channel = client.get_channel(TARGET_CHANNEL_ID)
    if message.content:
        content = f"📢 **來自 {message.guild.name}：**\n{message.content}"
        
        if message.attachments:
            content += "\n".join([attachment.url for attachment in message.attachments])
        
        if content:
            await target_channel.send(content)

client.run(BOT_TOKEN)
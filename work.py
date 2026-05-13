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
    print(f"阿農機器人已上線：{client.user}")

@client.event
async def on_message(message):
    
    # 發出該訊息的作者是否為bot
    # message.author.bot: bool
    if message.author.bot: 
        return
    
    # 排除來源的頻道以外的頻道的訊息
    if message.channel.id != SOURCE_CHANNEL_ID:
        return
    
    # 避免找不到目標頻道
    target_channel = client.get_channel(TARGET_CHANNEL_ID)
    if target_channel is None:
        print(f"找不到目標頻道：{TARGET_CHANNEL_ID}")
        return
    
    Source_Server_Name = message.guild.name
    Source_Channel_Name = message.channel.name

    # 預設要轉發的訊息內容
    # content: str
    content = f"📢 **來自 `{Source_Server_Name}` 的 `{Source_Channel_Name}`：**\n\n"
    
    # 訊息中的內容(文字)
    # message.content: str
    # 確認 message.content != ""
    if message.content:
        content += message.content
        
    # 訊息中的附件
    # message.attachments: list
    # 確認 message.attachments != []
    if message.attachments:
        content += "\n".join([attachment.url + "\n" for attachment in message.attachments])
    
    # 確認要轉發的訊息內容有東西
    has_content = message.content or message.attachments
    # has_content: bool
    # has_content != ""
    if has_content:
        # 送出要轉發的訊息
        await target_channel.send(content)


client.run(BOT_TOKEN)
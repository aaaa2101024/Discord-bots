import discord
from discord.ext import commands

# Botの基本的な設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージの内容を読み取るために必要
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "1"

with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line[0 : len("TOKEN=")] == "TOKEN=":
            TOKEN = line[len("TOKEN="):]


# Botが起動したときに実行されるイベント
@bot.event
async def on_ready():
    print(f"{bot.user}としてログインしました")


# 'hello' というコマンドが入力されたときに実行される処理
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


# ⚠️注意: 'YOUR_BOT_TOKEN' の部分を、先ほど取得したあなたのBotのトークンに置き換えてください
bot.run(TOKEN)

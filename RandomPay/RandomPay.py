import discord
from discord import app_commands
import random

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

UPPERORLOWERNUM = [ord("a"), ord("A")]


def makeingPaypayURL():
    URL = "https://pay.paypay.ne.jp/"
    for i in range(16):
        # ランダム生成の文字について、大文字か小文字かを設定
        UpperOrLower = random.randint(0, 1)
        # 実質的に何の文字が追加されるか
        numOfAlp = random.randint(0, 25)
        # 実際の文字
        addWord = chr(UPPERORLOWERNUM[UpperOrLower] + numOfAlp)
        URL += addWord
    return URL


@bot.event
async def on_ready():
    print(f"{bot.user}としてログイン")
    await tree.sync()
    print("スラッシュコマンドなんね")

#32
@tree.command(name="hello", description="返事!!!")
async def hello(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("はろー！！！" + text)
    # await interaction.response.send_message(text)


@tree.command(name="randompay",description="paypayおみくじ 第一引数にURLを, 第二引数に出力個数を入力、discordの制約的に45個ぐらいが限界みたい",)
async def random_pay(interaction: discord.Interaction, url: str, sum: int):
    if sum <= 45:
        await interaction.response.send_message("[paypay] おみくじが開催されました。受け取りを完了してください。")
        output = "[paypay] おみくじが開催されました。受け取りを完了してください。\n"
        outputList = [url]
        for i in range(sum - 1):
            outputList.append(makeingPaypayURL())
        done_URL_num = set()
        while len(done_URL_num) != sum:
            numOfOutputURL = random.randint(0, sum - 1)
            if not numOfOutputURL in done_URL_num:
                done_URL_num.add(numOfOutputURL)
                output += outputList[numOfOutputURL] + "\n"
        await interaction.edit_original_response(content=output)
    else:
        await interaction.response.send_message("[paypay] おみくじが開催できませんでした。URLの個数などを見直してください。")

bot.run("MTQwNTAxODM0NDk3Mjg3NzgyNA.GLrup5.pwGgc7C-t2mVIxcWYIn6Jk4tu4ceoRgUGX-ovQ")

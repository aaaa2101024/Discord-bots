import discord
from discord import app_commands
import asyncio


intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

TOKEN = "1"
global flag

# TOKENを開く
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line[0 : len("TOKEN=")] == "TOKEN=":
            TOKEN = line[len("TOKEN=") :]

class ResponsButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.responsFlag = False

    # respons
    @discord.ui.button(label="I'm here!!!",style=discord.ButtonStyle.success)
    async def respons(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.defer()
        self.responsFlag = True
        button.disabled = True
        await interaction.edit_original_response(view=self)
        return 

@bot.event
async def on_ready():
    print(f"{bot.user}としてログイン")
    await tree.sync()

@tree.command(name="ping", description="メンバーに対してpingメッセージを送ります。")
@app_commands.describe(
    member="pingを送る相手",
    cnt="pingを送る回数"
)
async def ping(interaction :discord.Interaction, member:discord.Member, cnt:int):
    if cnt > 100:
        await interaction.response.send_message("さすがにね、discordが破壊されるんじゃないかな")
    view=ResponsButton()
    await interaction.response.send_message(f"{member.mention} に ping を送信しています 32 バイトのデータ:", view=view)
    for _ in range(cnt):
        # (非同期処理スリープ)
        await asyncio.sleep(3)
        if(view.responsFlag == True):
            break
        else :
            await interaction.followup.send(f"{member.mention}への要求がタイムアウトしました。")
    if(view.responsFlag == True):
        await interaction.followup.send(f"{member.mention}の生存を確認")
    else:
        await interaction.followup.send("行方不明")

bot.run(TOKEN)

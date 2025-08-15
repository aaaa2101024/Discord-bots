import discord
from discord import app_commands
import random

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

TOKEN = "1"
GOROKU = []

def decision_goroku():
    goroku = GOROKU[random.randint(0, len(GOROKU) - 1)]
    return goroku


# ボタンの設定
class QuestionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.ans = "Sure! "
    # Yes
    @discord.ui.button(label="Sure! ", style=discord.ButtonStyle.success)
    async def sure_button(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.edit_message(content=f"Yay!")
    # No
    @discord.ui.button(label="nop. ", style=discord.ButtonStyle.danger)
    async def nop_button(
        self, interaction: discord.Interaction, button: discord.ui.button
    ):
        # 応答の保留
        await interaction.response.defer()
        send_message = decision_goroku()
        # こうするとボタンを無効化できる
        button.disabled = True
        # 語録を送る
        await interaction.followup.send(content=send_message)
        # ボタンを無効化してくれる
        await interaction.edit_original_response(view=self)


# TOKENを開く
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line[0 : len("TOKEN=")] == "TOKEN=":
            TOKEN = line[len("TOKEN=") :]

# 語録を取得
with open("./goroku.txt", "r", encoding="utf-8") as f:
    for line in f:
        GOROKU.append(line)


# ログイン時メッセージ
@bot.event
async def on_ready():
    print(f"{bot.user}としてログイン")
    await tree.sync()

# ice-teaコマンド
@tree.command(name="icetea", description="サー")
async def ice_tea(interaction: discord.Interaction):
    await interaction.response.send_message(
        "お　ま　た　せ \nアイスティーしかなかったけど、いいかな？"
    )

# Sureとnopを選ばせるタイプのコマンド
@tree.command(name="messageyaju", description="?????")
@app_commands.choices(
    answer=[
        app_commands.Choice(name="Sure!", value="yes"),
        app_commands.Choice(name="nop.", value="no"),
    ]
)
async def massege_yaju(
    interaction: discord.Interaction, answer: app_commands.Choice[str]
):
    choice = answer.value
    if choice == "yes":
        await interaction.response.send_message("素晴らしい!")
    else:
        # 応答の保留
        await interaction.response.defer()
        send_message = decision_goroku()
        # 語録を送る
        await interaction.followup.send(content=send_message)

# ボタンで選択させるタイプのコマンド
@tree.command(name="doyoulikeyaku", description="Do you like Yaju? ")
async def doyoulikeyaju(interaction: discord.Interaction):
    view = QuestionView()

    await interaction.response.send_message("Do you like Yaju? ", view=view)


bot.run(TOKEN)

import discord
from discord import app_commands
import random

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

TOKEN = "1"
GOROKU = []
FILEPASSES = []

# TOKENを開く
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line[0 : len("TOKEN=")] == "TOKEN=":
            TOKEN = line[len("TOKEN=") :]

# 語録を取得
with open("./goroku.txt", "r", encoding="utf-8") as f:
    for line in f:
        GOROKU.append(line)

# 画像のパスを取得
with open("./imageFilePath.txt", "r", encoding="utf-8") as f:
    for line in f:
        # strip()で改行を削除
        FILEPASSES.append(line.strip())


def decision_goroku():
    goroku = GOROKU[random.randint(0, len(GOROKU) - 1)]
    return goroku


def decision_image():
    filePath = FILEPASSES[random.randint(0, len(FILEPASSES) - 1)]
    print(filePath)
    # try:
    with open(filePath, "rb") as f:
        picture = discord.File(f)
        return picture
    # except FileNotFoundError:
    #     # ephemeralはいい感じに特定のユーザしか表示されないらしい
    #     await interaction.edit_original_response(f"ファイルがないよ", ephemeral=True)
    # except Exception as e:
    #     await interaction.edit_original_response(f"{e}だよ", ephemeral=True)
    # return "a"


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
        # 応答の保留
        await interaction.response.defer()
        send_image = decision_image()
        # こうするとボタンを無効化できる
        button.disabled = True
        # 画像を送信
        await interaction.followup.send(file=send_image)
        # ボタンを無効化してくれる
        await interaction.edit_original_response(view=self)

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
        await interaction.response.defer()
        send_image = decision_image()
        # 画像を送信
        await interaction.followup.send(file=send_image)
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


@tree.command(name="sendimagetest", description="画像送信のテスト")
# @app_commands.describe(filename="icon.png") 何を与えたらいいかのヒント
async def sendimagetest(interaction: discord.Interaction):
    try:
        with open("./icon.png", "rb") as f:
            picture = discord.File(f)
            await interaction.response.send_message(file=picture)
    except FileNotFoundError:
        # ephemeralはいい感じに特定のユーザしか表示されないらしい
        await interaction.response.send_message(f"ファイルがないよ", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"{e}だよ", ephemeral=True)


bot.run(TOKEN)

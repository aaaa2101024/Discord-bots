import discord
from discord import app_commands

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

TOKEN = "1"

with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line[0 : len("TOKEN=")] == "TOKEN=":
            TOKEN = line[len("TOKEN=") :]


@bot.event
async def on_ready():
    print(f"{bot.user}としてログイン")
    await tree.sync()


@tree.command(name="icetea", description="サー")
async def ice_tea(interaction: discord.Interaction):
    await interaction.response.send_message(
        "お　ま　た　せ \n アイスティーしかなかったけど、いいかな？"
    )


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
        await interaction.response.send_message("残念、その程度の人間なんだね")


bot.run(TOKEN)

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

@bot.command()
async def malzeme(ctx, *, cevap):
    if cevap.lower() == "karton":
        await ctx.send("Klasörlük, telefon tutucu, sokak hayvanları için ev yapabilirsin!")
    else:
        await ctx.send("Üzgünüm, daha o bilgiyi almadım ama elinde karton varsa yardım edebilirim.")

bot.run("token")

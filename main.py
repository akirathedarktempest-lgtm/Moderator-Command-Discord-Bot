import discord
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
  print("The bot is ready...")

banned_words=["ban", "banned"] #i don't know much words, I was never muted...showing off, haha

@bot.event
async def on_message(message: discord.Message):
    member=message.author
    delta=timedelta(minutes=1440)#if you know, 60*24 is 1440
    m=message.content.split(" ")
    if member==bot.user:
        return
    else:
        ch=message.channel.id
        channel=message.guild.get_channel(ch)
        for i in m:
            for z in banned_words:#two loops to compare each
                if i==z:
                    await member.timeout(delta, reason=f"Used a banned word \n> {message.content}")
                    await channel.send(f"Used a banned word \n> {message.content}")
                else:
                    continue

bot.run("YOUR_TOKEN")

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #untuk dalam find(" ") dapat di ubah bebas
    if message.content.find("$hello") != -1: 
      await message.channel.send("Hi") #balasan dri bot dri perintah $hello

    if message.content.find("$instagram") != -1:
      await message.channel.send("https://www.instagram.com/.......")

    if message.content.find("$youtube") != -1:
      await message.channel.send("https://www.youtube.com/channel/.......")

    if message.content.find("$author") != -1:
      await message.channel.send("By Yuna Bear")

client.run(os.getenv('TOKEN'))

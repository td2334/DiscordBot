import discord 
import os
from keep_alive import keep_alive
from datetime import datetime
from discord.ext import commands
from discord.ext import tasks

client = discord.Client()

@client.event 

async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(message):
  #No response 
  if message.author == client.user:
    return 
  #Responds to Hello
  if message.content.startswith('hello'):
    await message.channel.send("Hello")

  #Responds to any url posted 
  if message.content.startswith('https' ):
    msg = 'Hi {0.author.mention} Thank You For Sending This Cool Link and Sharing Information!!'.format(message)
    await message.channel.send(msg)
  #Responds on general channel 

#Make bot spew random hashtag 
#studyformitsuru
@tasks.loop(hours = 4 )
async def randomhashtag():
  channel = client.get_channel(871913431287091210)
  await channel.send("Today is a good day to #StudyForMitsuru")


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  randomhashtag.start()

keep_alive()
client.run(os.environ['TOKEN']) 


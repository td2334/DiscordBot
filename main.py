import discord 
import os
from keep_alive import keep_alive
from datetime import datetime
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get 

client = discord.Client()

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
  if message.content.startswith('hi'):
    msg = "Hello {0.author.mention}".format(message)
    await message.channel.send(msg)
    role = get(message.server.roles, id=871074880890744893)
    await client.add_roles(message.author, role)

#Today in History!
@tasks.loop(hours = 4 ) 
async def history(): 
  channel = client.get_channel(871937620597436456)
  await channel.send("https")

#Make bot spew hashtag 
#studyformitsuru
@tasks.loop(hours = 12 )
async def personahashtag():
  channel = client.get_channel(871913431287091210)
  await channel.send("Today is a good day to #StudyForMitsuru")




@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  personahashtag.start()
  history.start()



keep_alive()
client.run(os.environ['TOKEN']) 


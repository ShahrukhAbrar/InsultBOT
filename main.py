import discord
import os
import random
from replit import db
from discord.ext.commands import Bot
import requests
import json
from keep_alive import keep_alive



# iniitializing discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'i am ready {client.user}')


@client.event
async def on_message(message):
    # if msg is sent by bot itself then ignore
    if message.author == client.user:
        return  

    msg = message.content.lower()
    msg=msg.lower()
   

    # if msg contain pre-defined words reply it with the pre-defined phrase
    if 'gay' in message.content.lower():
        await message.channel.send("Big words coming from such a public cum-dumpster of a man")

    if 'jamal' in message.content.lower():
        await message.channel.send('Name of White Pathan Piping your Girlfriend')    

    if 'asad'in message.content.lower():
        await message.channel.send('A-Sad Man')

    if '69'in message.content:
        await message.channel.send('( ͡° ͜ʖ ͡°)')    

    if 'grammar' in message.content.lower(): 
        await message.channel.send('Fuking Grammar Nazi')    

    if message.content.startswith('*'): 
        await message.channel.send('Fuking Grammar Nazi')       

    if 'shahrukh' in message.content.lower(): 
        await message.channel.send('https://cdn.discordapp.com/attachments/370277460735950852/930867291057446972/IMG_20210913_225900_293.jpg') 

    if 'problem' in message.content.lower():
        await message.channel.send('If you think your Problems are big, then look at my dick')

    if 'meme' in message.content.lower():
      meme_request=requests.get("https://meme-api.herokuapp.com/gimme")
      meme=json.loads(meme_request.text)
      channel = client.get_channel(370277460735950852)
      await message.channel.send(meme["url"])


    if '^announce' in message.content.lower():
      channel = client.get_channel(370277460735950852)
      await message.channel.send('@everyone')

    if any(word in msg for word in starter_sadwords):
        resp=requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        response=json.loads(resp.text)
        await message.channel.send(response["insult"])





keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)

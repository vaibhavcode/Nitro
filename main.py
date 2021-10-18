import discord
import os
from keep_alive import keep_alive
import string
import random
import requests


bot = discord.Client(activity=discord.Game(name="Nitro"))

comch = 859688850346868747
dropch = 899255722926301205
aemo = "<a:ani:886814282694668298>"
emo = "<:EWdeUeHXkAQgJh7:886492479577264148>"


@bot.event
async def on_ready():
    print(bot.user)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    
    if message.content == "!h":
      he = discord.Embed(title = "Help", color=0xf47fff)
      he.add_field(name="!g (nitro/nitro classic)", value="Generate 1 unchecked nitro/nitro classic code")
      he.add_field(name="!gc (nitro/nitro classic)", value="Generate and check 1 nitro/nitro classic code")
      he.add_field(name="!c (nitro code/nitro classic code)", value="Check a nitro/nitro classic code")
      he.add_field(name="!pc (nitro code/nitro classic code)", value="Check a nitro/nitro classic code using a proxy to prevent ratelimiting")
      he.add_field(name="!h", value="Help")

      await message.channel.send(embed=he)



    if message.content.startswith("!pc"):
      await message.channel.send("This feature is in beta.")
    

    if message.content.startswith("!g") and message.channel.id == comch:
     ntype = message.content[3:]
     ntype.strip()
     ntype = ntype.lower()
     if ntype == "nitro" or ntype == "nitro classic":
       code = nitrounchecked(ntype)
       await message.author.send("https://discord.gift/"+code)
       await message.channel.send(message.author.mention+" Check your DMs for "+ntype+"!")

    
    if message.content.startswith("!c") and message.channel.id == comch:
      code = message.content[3:]
      code.strip()
      if len(code) == 16 or len(code) == 24:

          url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
          response = requests.get(url)

          if response.status_code == 200:
              x = "Valid"
              channel = bot.get_channel(dropch)
              await channel.send("https://discord.gift/"+code)

          elif response.status_code == 429:
              x = "Ratelimited"
          elif response.status_code == 404:
              x = "Expired"
          else:
              x = "Invalid"
      
          if len(code) == 16:
              t = "Nitro Classic"
          elif len(code) == 24:
              t = "Nitro"
          else:
              t = "Invalid"

          emb1 = discord.Embed(title = emo + " Discord Nitro " + emo, color=0xf47fff)

          emb1.add_field(name="Code", value=code, inline=False)
          emb1.add_field(name="Type", value=t, inline=True)
          emb1.add_field(name="Status", value=x, inline=True)

          await message.channel.send(embed=emb1)



    if message.content.startswith("!gc") and message.channel.id == comch:

       ntype = message.content[4:]
       ntype.strip()
       ntype = ntype.lower()
       if ntype == "nitro" or ntype == "nitro classic":
          code = nitrounchecked(ntype)

          url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
          response = requests.get(url)

          if response.status_code == 200:
             x = "Valid"
             channel = bot.get_channel(dropch)
             await channel.send("https://discord.gift/"+code)

          elif response.status_code == 429:
              x = "Ratelimited"
          elif response.status_code == 404:
              x = "Expired"
          else:
              x = "Invalid"
          
          if len(code) == 16:
              t = "Nitro Classic"
          elif len(code) == 24:
              t = "Nitro"

          emb = discord.Embed(title = aemo + " Discord Nitro " + aemo, color=0xf47fff)

          emb.add_field(name="Code", value=code, inline=False)
          emb.add_field(name="Type", value=t, inline=True)
          emb.add_field(name="Status", value=x, inline=True)

          await message.channel.send(message.author.mention+" Check your DMs for "+ntype+"!")
          await message.author.send(embed=emb)
          await message.author.send("https://discord.gift/"+code)



def nitrounchecked(type):
  if type == "nitro classic":
      length = 16
  elif type == "nitro":
      length = 24
  code = list(string.ascii_letters + string.digits)
  random.shuffle(code)
  code = random.choices(code, k=length)
  random.shuffle(code)
  code = "".join(code) 
  return code


keep_alive()
bot.run(os.environ['Token'])





#Created by 6Ex#6666, removing these credits will result in a class action lawsuit against you / your corporation, under the DMCA Act.
#
import requests
import discord
from discord.ext import commands
import requests
from discord.ext.commands import cooldown, BucketType

minimum = 500000
from discord.ext.commands import has_permissions
def calculate(cash):
  finalprice = cash/20000
  return finalprice
multipliers = {'K':1000, 'M':1000000, 'B':1000000000,'k':1000, 'm':1000000, 'b':1000000000}

def string_to_int(string):
    if string[-1].isdigit():
        return int(string)
    mult = multipliers[string[-1]]
    return int(float(string[:-1]) * mult)

bot = commands.Bot(command_prefix='!')
@bot.command()
@has_permissions(administrator=True)  
async def revive(ctx  ):
  name = 'BUYERS'
  category = discord.utils.get(ctx.guild.categories, name=name)
  channels = category.channels
  for channel in channels:
    await channel.send("@everyone A quick revival of the ticket!")
@bot.command()
async def buy(ctx, arg):
    amount = string_to_int(str(arg))
    if int(amount) < minimum:
        await ctx.send("You must purchase over 500k cash.")
    else:
        resulto = int(calculate(int(amount)))
        result = round(resulto)
        await ctx.send(str(result) + " robux! You can create a ticket with !create or do !purchase (AMOUNT OF CASH YOU WANT) to automatically buy.")



@bot.command()
@commands.cooldown(2, 86400, commands.BucketType.user)
async def purchase(ctx, arg):
    amount = string_to_int(str(arg))
    if int(amount) < minimum:
        await ctx.send("You must purchase over 500k cash.")
    else:
        resulto = int(calculate(int(amount)))
        result = round(resulto)
        ID = requests.get(url = "YOURURLHERE/create?price="+str(result))
        ID = ID.content.decode("utf-8")
        await ctx.send("``"+(str(ID))+"``" + " is your ID. Please join the following game: https://www.roblox.com/games/8407856158/ \nThen, in the ROBLOX chat, please chat the following: !buy [ID]")

@purchase.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
         await ctx.send(f"Try again in {error.retry_after:.2f} seconds.")
@bot.command()
async def create(ctx):
    name = 'BUYERS'
    guild = ctx.guild
    channels = guild.text_channels
    category = discord.utils.get(ctx.guild.categories, name=name)
    thechannelname =f'buyerãƒ»{ctx.author.id}'
    duplicate = False
    for channel in channels:
        if thechannelname == channel.name:
            duplicate = True
            break
    if duplicate:
        await ctx.send("You already have a open ticket. ðŸ˜ðŸ˜ðŸ˜")
    else:
        ticket_channel = await guild.create_text_channel(name=f'buyerãƒ»{ctx.author.id}', category = category)
        await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
        await ctx.send("Created a ticket for you!")

@bot.command()
async def delete(ctx):
   guild = ctx.guild
   channels = guild.text_channels
   if ctx.message.channel.name == f'buyerãƒ»{ctx.author.id}':
       existing_channel = discord.utils.get(guild.channels, name=f'buyerãƒ»{ctx.author.id}')
       await existing_channel.delete()
   else:
        await ctx.send("Only use this for tickets you created!")

@bot.command()
async def payments(ctx):
    await ctx.send("disabled command")
@bot.event
async def on_ready():    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="people buy da hood cash."))

    
    print("Bot is ready!")
bot.run('OTI2MjQwOTg4OTk1OTI4MTI0.Yc4zJA.UTDlw0Gv6HvDHzM7aX5Jz_A-1h8')

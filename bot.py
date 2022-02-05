from asyncio.windows_events import INFINITE
import discord
import pickle
import os
import asyncio
from asyncio import sleep
from discord import activity
from discord import channel
from discord import member
from discord import guild
from discord import message
from discord.embeds import Embed
from discord.enums import Status
from discord.ext import commands
from discord.ext.commands import bot, has_permissions
from discord.player import AudioSource

client = discord.Client()


client = commands.Bot(command_prefix = 'p!', case_insensitive=True)

data_filename = "data.pickle"

class Data:
    def __init__(self, wallet, bank):
        self.wallet = wallet
        self.bank = bank


#Events
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

  

#Commands
@client.command(aliases=['job','breadmachine','moneymaker','givemoney','baconator'])
async def work(message):
    member_data = load_member_data(message.author.id)

    member_data.wallet += 20
    await message.channel.send("you got some money")

    save_member_data(message.author.id, member_data)
@client.command()
async def dep(message):
    member_data = load_member_data(message.author.id)

    member_data.bank += 20
    await message.channel.send('deposited 20 bucks in yo bank(spoiler: it doesnt work at all)')

@client.command(aliases=['balance'])
async def bal(message):
    member_data = load_member_data(message.author.id)

    embed = discord.Embed(title=f"{message.author.display_name}'s Balance")
    embed.add_field(name="Wallet", value=str(member_data.wallet))
    embed.add_field(name="bank, also if u see this then hi", value=str(member_data.bank))

    await message.channel.send(embed=embed)


#Functions
def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)


#you have left the bank zone

poopy = 'Made by Jimmy is not Happy#2208'
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(poopy))
    general_channel = client.get_channel(852989025827553291)
    await general_channel.send('<:ParloHaha:856902538070327358> Hi! Im currently online!')
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    await member.send(f'You were kicked from {guild.name} || reason {reason}.')

@client.command()
@has_permissions (ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    await member.send(f'You were banned from {guild.name} || reason {reason}. <:ParloHaha:856902538070327358> dont do it')

@client.command()
@has_permissions (manage_messages=True)
async def role(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.send(f'<:ParloHaha:856902538070327358> Gave role to user!')

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: The ping is {round(client.latency * 1000)}ms!')
@client.command()
async def bobux(ctx):
    await ctx.send('https://media.discordapp.net/attachments/797934906918305822/856653125602902016/E4WtjUQVgAM0h07.png')
    
client.run('no')

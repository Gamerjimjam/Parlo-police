import discord
from discord import activity
from discord import channel
from discord import member
from discord import guild
from discord.embeds import Embed
from discord.enums import Status
from discord.ext import commands
from discord.ext.commands import bot, has_permissions
from discord.player import AudioSource



client = discord.Client()


client = commands.Bot(command_prefix = 'p!')

@client.command()
async def mute(ctx, member = discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions)

@client.event
async def on_ready():
    general_channel = client.get_channel(845715616572112946)
    await general_channel.send('BOT IS READY')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Created by Jimmy is not Happy#2208, he is so cool'))
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: The ping is {round(client.latency * 1000)}ms!')
@client.command()

async def ban(ctx, member : discord.Member, *, reason=None):
    if(not ctx.author.guild_permissions.ban_members):
        await ctx.send('no perms lmao')
        return
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()

async def kick(ctx, member : discord.Member, *, reason=None):
    if(not ctx.author.guild_permissions.kick_members):
        await ctx.send('no perms lmao')
        return
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} sucsessfully')
@client.command()
async def commands(ctx):
    tosend = """THIS BOT IS FAIRLY NEW AND THERE WILL BE BUGS
    Administration commands
    p!ban
    p!kick
    Random commands
    p!ping, gets the ping from the bot
    
    """

client.run('ODUwNzUxODk0NDQyOTk5ODM4.YLuScQ.TRIexXpn8pscMa9EJgF6Ns8BJ2g')

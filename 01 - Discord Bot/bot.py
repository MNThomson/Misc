import discord
import asyncio
import time
import aiofiles
import re
import os

from discord.ext import commands, tasks
from datetime import datetime
from random import choice
from dotenv import load_dotenv

#Check if the .env file exists, if not, create it
if not os.path.exists('./.env'):
	env = open(".env", "w")  
	env.write("BOT_TOKEN=")
	env.close()
	print("Please add your Bot Token to the .env file\nExiting...")
	exit()


#Load the bot token from the .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

prefixes = "!", "@"
bot = commands.Bot(command_prefix=prefixes)
bot.remove_command('help') # Comment this line to get the default help command back

@bot.event
async def on_ready():
	print("Bot is running")
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('Bored!')) #This is the bots status

	####REACTION ROLES####
	bot.reaction_roles = []
	
	for file in ["reaction_roles.txt"]:
		async with aiofiles.open(file, mode="a") as temp:
			pass

	async with aiofiles.open("reaction_roles.txt", mode="r") as file:
		lines = await file.readlines()
		for line in lines:
			data = line.split(" ")
			bot.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))

#HELP#
@bot.command()
async def help(ctx):
	await ctx.channel.purge(limit=1)
	await ctx.send('Hi, I\'m Jamesy\nYour Personal Assiststant!')

#BINARY#
@bot.command()
async def binary(ctx, input):
	output = ' '.join(format(ord(i), 'b') for i in input)
	await ctx.channel.purge(limit=1)
	await ctx.send(str(output))

#PURGE#
@bot.command()
@commands.has_role('Admin')
async def purge(ctx, amount=6):
	await ctx.channel.purge(limit=amount + 1)

#@SOMEONE#
@bot.command()
async def someone(ctx):
	await ctx.send("Hullo " + choice(tuple(member.mention for member in ctx.guild.members if not member.bot)))

#Google It Idiot#
@bot.command()
async def google(ctx, *args):
	string = '+'.join(args)
	cleaned = re.sub(r'[^a-zA-Z+\d\s:]', '', string)
	await ctx.send("http://letmegooglethat.com/?q=" + cleaned)




####################################### REACTION ROLES #######################################
@bot.event
async def on_raw_reaction_add(payload):
	for role_id, msg_id, emoji in bot.reaction_roles:
		if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
			await payload.member.add_roles(bot.get_guild(payload.guild_id).get_role(role_id))

@bot.event
async def on_raw_reaction_remove(payload):
	for role_id, msg_id, emoji in bot.reaction_roles:
		if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
			guild = bot.get_guild(payload.guild_id)
			await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))

#bot commands
@bot.command()
async def set_reaction(ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
	if role != None and msg != None and emoji != None:
		await msg.add_reaction(emoji)
		bot.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
		
		async with aiofiles.open("reaction_roles.txt", mode="a") as file:
			emoji_utf = emoji.encode("utf-8")
			await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

		await ctx.channel.send("Reaction has been set.")
		await asyncio.sleep(1)
		await ctx.channel.purge(limit=2)
		
	else:
		await ctx.send("Invalid arguments.")

bot.run(BOT_TOKEN)
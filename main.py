from dotenv import load_dotenv
from discord.ext import commands
import json
import os
import discord
import time
import sys
import asyncio
load_dotenv()
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Bot logged in successfully {client.user}")

@client.event
async def on_message_delete(message):
    try:
        content = await open_snipe()
        content["author"] = str(message.author.name)+"#"+str(message.author.discriminator)
        content["authorpfp"] = str(message.author.avatar)
        content["message"] = str(message.content)
        content["messageID"] = str(message.id)
        try:
            content["messageLink"] = str(message.attachments[0].url)
        except:
            content["messageLink"] = ""
        content["authorID"] = str(message.author.id)
        out_file = open(os.path.join("json","snipe","snipe.json"), "w")
        json.dump(content, out_file, indent = 4)
        out_file.close()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
@client.command(name="sync")
async def sync(ctx):
    try: 
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} cmd(s).")
    except Exception as e:
        print(e)
  
@client.command(name="load")
async def load_(ctx):
    a = await load()
    await ctx.send(f"Load {a} extension(s).")


@client.command(name="unload")
async def unload(ctx, extension):
    message = await ctx.send(f"Unloading {extension}")
    client.unload_extension(f"commands.{extension}")
    message.edit(f"Unloaded {extension}")
  
@client.command(name="reload")
async def reload(ctx, extension):
    try:
        start_time = time.time()
        await client.unload_extension(f"commands.{extension}")
        message = await ctx.send("Unloading {} cmd.".format(extension))
        await message.edit(content="Loading {} cmd. ({}s)".format(extension,round(time.time()-start_time,1)))
        await client.load_extension(f"commands.{extension}")
        await message.edit(content="Loaded {} cmd. ({}s)".format(extension,round(time.time()- start_time,1)))
    except Exception as e:
        await ctx.send("No command named `{}`".format(extension))
        print(e)




async def open_snipe():
    with open(os.path.join("json","snipe","snipe.json"), "r") as f:
        return json.loads(f.read())


async def save_snipe(a):
    with open(os.path.join("json","snipe","snipe.json"), "r") as f:
        json.dump(a, f, indent=4)
async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")


async def main():
    await load()
    await client.start(os.getenv("TOKEN"))

asyncio.run(main())

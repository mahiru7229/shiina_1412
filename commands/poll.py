"""
Poll Command.
"""
from discord.ext import commands
import discord
import sys
import json
import os
import time
import asyncio
def get_time():
    return time.strftime("%H:%M")

class poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="poll")
    async def poll_(self, ctx, choice1, choice2,time_ ,*, topic ):
        try: 
            int(time_)
            embed = discord.Embed(title=topic, description=f":one: {choice1}\n\n:two: {choice2}\n\nVote end in {time_} second(s)", color= discord.Color.from_rgb(255,255,255))
            embed.set_footer(text=f"Poll created by {ctx.author.name}#{ctx.author.discriminator} | Today at {get_time()}.")
            embed.set_thumbnail(url=ctx.author.avatar)
            message = await ctx.send(embed=embed)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await asyncio.sleep(int(time_))

            new_msg = await ctx.fetch_message(message.id)
            count_1 = int(new_msg.reactions[0].count) -1
            count_2 = int(new_msg.reactions[1].count) -1
            result = "Tie"
            if int(count_1) > int(count_2):
                result = f"{choice1} win!"
            elif int(count_1) < int(count_2):
                result = f"{choice2} win!"
            embed_ = discord.Embed(title=f"{topic} (End)", 
            description=f":one: {choice1}: {int(count_1)}\n\n:two: {choice2}: {int(count_2)}\n\n{result}",
            color= discord.Color.from_rgb(255,255,255))
            embed_.set_footer(text=f"Poll created by {ctx.author.name}#{ctx.author.discriminator} | End at {get_time()}.")
            embed_.set_thumbnail(url=ctx.author.avatar)
            await message.edit(embed=embed_)
        except Exception as e:
            await ctx.send(f"{ctx.author.mention}| Wrong Argument !")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)
    
async def setup(client):
    await client.add_cog(poll(client))



if __name__ == "__main__":
    print("Mahiru#1542")
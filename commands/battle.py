from discord.ext import commands
import discord
import sys
import json
import asyncio
import os

class battle(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    # @commands.command(name="test")
    # async def test(self, ctx):
    #     question = ["Ban lop may","Ban bao nhieu tuoi"]
    #     answer = []
    #     def check(m):
    #         return m.author == ctx.author and m.channel == ctx.channel
    #     for i in question:
    #         await ctx.send(i)
    #         try:
    #             msg = await self.client.wait_for('message', timeout=5,check=check)
    #         except asyncio.TimeoutError:
    #             await ctx.send("Cham the")
    #             return
    #         except Exception as e:
    #             exc_type, exc_obj, exc_tb = sys.exc_info()
    #             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #             print(exc_type, fname, exc_tb.tb_lineno, e)
    #         else:
    #             answer.append(msg.content)
    #     await ctx.send(answer)



    
async def setup(client):
    await client.add_cog(battle(client))



if __name__ == "__main__":
    print("Mahiru#1542")
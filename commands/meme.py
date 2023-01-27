from redvid import Downloader
from moviepy.editor import VideoFileClip
from discord.ext import commands
import requests
import discord
import sys
import json
import os
import aiohttp
import random

class meme(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name="meme")
    async def meme(self,ctx):
        """Reddit Meme (jakertown, CursedRoblox, CursedMinecraft)"""
        #timeframe var
        t_f = ["hour", "day", "week", "month", "year", "all"]
        listing_ = ["controversial", "best", "hot", "new", "rising", "top"]
        random_ = 0
        try:
            subreddit = random.choice(["jakertown","CursedRoblox","CursedMinecraft"])
            limit = 100
            timeframe = random.choice(t_f)
            listing = random.choice(listing_)
            r = await meme.get_reddit(subreddit,listing,limit,timeframe)
            #del temp .mp4 file
            for filename in os.listdir("./temp"):
                if filename.endswith(".mp4"):
                    os.remove(os.path.join("temp",filename))

        
                # reddit = Downloader()
                # reddit.auto_max = True
                # reddit.max_s = 1 * (1 << 20)
                # reddit.path = os.path.join("temp")
                # print(f"{r['data']['children'][random_]['data']['url']}")
                # reddit.url = f"{r['data']['children'][random_]['data']['url']}"
                # reddit.download()
                # #convert video to gif for discord embed
                # for filename in os.listdir("./temp"):
                #     if filename.endswith(".mp4"):
                #         videoClip = VideoFileClip(os.path.join("temp",filename))
                #         videoClip.write_gif(os.path.join("temp","batocom.gif"))
                # embed = discord.Embed(title=f"r/{subreddit}",
                #                         url=f"{r['data']['children'][random_]['data']['url']}",
                #                         description=f"{r['data']['children'][random_]['data']['title']}",
                #                         color=discord.Color.from_rgb(255,255,255))
                
                # file = discord.File(os.path.join("temp","batocom.gif"), filename="image.gif")
                # embed.set_author(name=ctx.author.name+"#"+ctx.author.discriminator)
                # embed.set_image(url="attachment://image.gif")
                # embed.set_footer(text="Lượt xem: {} | Up: {} | Down: {} | Score: {} ".format(
                #     r['data']['children'][random_]['data']['view_count'],
                #     r['data']['children'][random_]['data']['ups'],
                #     r['data']['children'][random_]['data']['downs'],
                #     r['data']['children'][random_]['data']['score'],
                #     ))
                # await ctx.send(embed=embed, file=file)

            embed = discord.Embed(title=f"r/{subreddit}",
                                        url=f"{r['data']['children'][0]['data']['url']}",
                                        description=f"{r['data']['children'][0]['data']['title']}",
                                        color=discord.Color.from_rgb(255,255,255))
            embed.add_field(name="________________________", value=f"{r['data']['children'][0]['data']['selftext']}")
            embed.set_author(name=ctx.author.name+"#"+ctx.author.discriminator)
            embed.set_image(url=f"{r['data']['children'][0]['data']['url']}")
            embed.set_footer(text="Lượt xem: {} | Up: {} | Down: {} | Score: {} ".format(
                    r['data']['children'][random_]['data']['view_count'],
                    r['data']['children'][random_]['data']['ups'],
                    r['data']['children'][random_]['data']['downs'],
                    r['data']['children'][random_]['data']['score'],
                    ))
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send("Reddit APIs có lỗi, dùng lại lệnh xem ?")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)
        #get reddit data
    async def get_reddit(subreddit,listing,limit,timeframe):
        try:
            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
        except:
            print('An Error Occured')
        return request.json()




        
    
async def setup(client):
    await client.add_cog(meme(client))



if __name__ == "__main__":
    print("Mahiru#1542")


from discord.ext import commands
import discord
import sys
import json
import os
import requests
import aiohttp
import random

class meme(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name="meme")
    async def meme(self,ctx):
        subreddit = 'jakertown'
        limit = 100
        timeframe = 'month' #hour, day, week, month, year, all
        listing = 'top' # controversial, best, hot, new, random, rising, top
        r = await meme.get_reddit(subreddit,listing,limit,timeframe)
        to_extract = ['title','url','score','num_comments','view_count','ups','downs','selftext']
        # print(f"{e}: {r['data']['children'][0]['data'][e]}")
        embed = discord.Embed(title=f"{'title'}: {r['data']['children'][0]['data']['title']}")
        embed.set_author(name=f"/r/{subreddit}")



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
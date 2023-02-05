from discord.ext import commands
import discord
import sys
import json
import os

class nameoffile(commands.Cog):
    def __init__(self, client):
        self.client = client


    
async def setup(client):
    await client.add_cog(nameoffile(client))



if __name__ == "__main__":
    print("Mahiru#1542")
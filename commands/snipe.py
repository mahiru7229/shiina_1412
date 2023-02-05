from discord.ext import commands
import discord
import sys
import json
import os

class snipe(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name="snipe")
    # @commands.cooldown(1,5,commands.BucketType.user)
    async def snipe(self, ctx):
        try:
            new_msg = await ctx.message.channel.fetch_message(ctx.message.id)
            await new_msg.add_reaction("\U0001F3AF")
            snipe_ = await snipe.open_snipe()
            embed = discord.Embed(color=discord.Color.from_rgb(12, 225, 232))
            embed.set_author(name="Người gửi: {}".format(snipe_["author"]), icon_url=snipe_["authorpfp"])
            embed.add_field(name="Content: ", value=snipe_["message"])
            if snipe_["messageLink"]:
                embed.set_image(url=snipe_["messageLink"])
            embed.set_footer(text="Message ID: {} | Author ID: {}".format(snipe_["messageID"], snipe_["authorID"]))        
            await ctx.send(embed=embed)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)

    
    async def open_snipe():
        with open(os.path.join("json","snipe","snipe.json"), "r") as f:
            return json.loads(f.read())

async def setup(client):
    await client.add_cog(snipe(client))



if __name__ == "__main__":
    print("Mahiru#1542")
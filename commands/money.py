from discord.ext import commands
import discord
import sys
import json
import random
import time
import os
import asyncio
def get_time():
    return time.strftime("%H:%M")
class money(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(name="cash", invoke_without_command = True)
    async def cash_(self, ctx):
        try:
            """
                Kiểm tra số tiền có trong túi

                Cách dùng: .cash 
            """
            await money.check_user_exist(ctx.author.id)
            bank_account = await money.open_bank()
            user_money = bank_account[str(ctx.author.id)]["money"]
            await ctx.send("{} | **Số tiền có trong túi của bạn là** __**{:,d}**__ :dollar:.".format(
            ctx.author.mention,
            user_money
            ))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)

    @cash_.command(name="give")
    async def give_(self, ctx, mention, money_):
        try:
            mention_temp = mention.replace("<","")
            mention_temp = mention_temp.replace(">","")
            mention_temp = mention_temp.replace("@","")
            await money.check_user_exist(mention_temp)
            await money.check_user_exist(ctx.author.id)
            temp_1 = await money.check_enough_balance(ctx.author.id, money_)
            if  temp_1 == True:
                bank_account = await money.open_bank()
                bank_account[str(mention_temp)]["money"] += int(money_)
                bank_account[str(ctx.author.id)]["money"] -= int(money_)
                await money.save_bank(bank_account)
                await ctx.send("{} | **Bạn đã chuyển số tiền là** __**{:,d}**__ :dollar:. ".format(ctx.author.mention,int(money_)))
            else:
                await ctx.send("{} | **Bạn không đủ tiền để chuyển !**".format(ctx.author.mention))

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)
    
    @commands.command(name="bet")
    async def bet_(self, ctx, money_ : int):
        await money.check_user_exist(str(ctx.author.id))
        bank_account = await money.open_bank()
        if bank_account[str(ctx.author.id)]["money"] < int(money_):
            await ctx.send(f"{ctx.author.mention} | **Bạn không có đủ tiền để chơi !**")
        elif int(money_) > 100000000:
            await ctx.send(f"{ctx.author.mention} | **Tối đa chơi được 100 triệu !**")
        else:        
            try:
                bank_account[str(ctx.author.id)]["money"] -= int(money_)
                embed = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} cược {money_:,d} :dollar: ...",
                description="...Tôi sẽ không ngần ngại mà chiều hư cậu, nên hãy cứ an tâm làm người vô dụng đi nhé? - Shiina Mahiru",
                color=discord.Color.from_rgb(255,255,255))
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} bet | Today at {get_time()}.")
                message = await ctx.send(ctx.author.mention,embed=embed)
                await asyncio.sleep(3)
                index = random.randint(0,1)
                if str(ctx.author.id) == "748439531761434676":
                    index_2 = int(money_)*2
                    embed_ = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} thắng {index_2:,d} :dollar:",
                description="...Tôi sẽ không ngần ngại mà chiều hư cậu, nên hãy cứ an tâm làm người vô dụng đi nhé? - Shiina Mahiru",
                color=discord.Color.from_rgb(0,255,0))
                    embed_.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} bet | Today at {get_time()}.")
                    await message.edit(embed=embed_)
                    bank_account[str(ctx.author.id)]["money"] += int(index_2)
                elif index == 0:
                    embed_ = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} thua {money_:,d} :dollar:",
                description="...Tôi sẽ không ngần ngại mà chiều hư cậu, nên hãy cứ an tâm làm người vô dụng đi nhé? - Shiina Mahiru",
                color=discord.Color.from_rgb(255,0,0))
                    embed_.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} bet | Today at {get_time()}.")
                    await message.edit(embed=embed_)
                else:
                    index_2 = int(money_)*2
                    embed_ = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} thắng {index_2:,d} :dollar:",
                description="...Tôi sẽ không ngần ngại mà chiều hư cậu, nên hãy cứ an tâm làm người vô dụng đi nhé? - Shiina Mahiru",
                color=discord.Color.from_rgb(0,255,0))
                    embed_.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} bet | Today at {get_time()}.")
                    await message.edit(embed=embed_)
                    bank_account[str(ctx.author.id)]["money"] += int(index_2)
                await money.save_bank(bank_account)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, e)
    async def check_user_exist(id):
        bank_account = await money.open_bank()
        if str(id) not in bank_account:
            bank_account[str(id)] = {}
            bank_account[str(id)]["money"] = 0
        await money.save_bank(bank_account)

    async def check_enough_balance(id,money_):
        await money.check_user_exist(str(id))
        bank_account = await money.open_bank()
        if int(bank_account[str(id)]["money"]) >= int(money_):
            return True
        else:
            return False
    
    async def open_bank():
        with open(os.path.join("json","economy","money.json"),"r") as f:
            return json.loads(f.read())

    async def save_bank(content):
        with open(os.path.join("json","economy","money.json"),"w") as f:
            return json.dump(content, f, indent=4)
    
async def setup(client):
    await client.add_cog(money(client))



if __name__ == "__main__":
    print("Mahiru#1542")
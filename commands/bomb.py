from discord.ext import commands
import discord
import sys
import random
import json
import os

class bomb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="bomb")
    async def bomb_(self, ctx,*, who):
        index = random.randint(1,10)
        if who == "<@748439531761434676>":
            await ctx.send(f"{ctx.author.mention} danh bom cai dac cau")
        elif who == f"<@{ctx.author.id}>":
            await ctx.send(f"{ctx.author.mention} how to danh bom ?")
        elif index == 5:
            await ctx.send(f"{ctx.author.mention} **đánh bom {who} thành công :)**")
        else:
            await ctx.send(f"{ctx.author.mention} **đánh bom {who} nhu cai dac cau.**")
    @commands.command(name="tcca")
    async def tcca(self, ctx, *,question_replace):
        await ctx.send(f'Rất nhiều bạn cứ nhai đi nhai lại cái câu là "{question_replace}?", muốn biết "{question_replace}?" thì hãy so sánh, hãy đọc các nguồn tin khác, hãy đọc báo. Nếu đọc được một tin mà vẫn còn cảm thấy rằng là "À, chưa tin nổi" thì mình phải đi tìm kiếm các chỗ khác thay vì hỏi một câu cứ nhai đi nhai lại như một con bò là "{question_replace}" rồi là vào cười haha xong rồi vào viết linh ta linh tinh ở trên đấy. Thì thay vì như thế các bạn hãy làm một việc này cho mình, hãy đi tìm xem, đọc trên các báo khác, hãy tìm đọc trên các fanpage khác, hãy biết tiếng em để hiểu các nguồn tin của nước ngoài thay vì cứ đi hỏi "{question_replace}?", tất cả những ai vào hỏi: "{question_replace}", mình đều một là xóa, hai là block hết. Mình không thích chuyện này, nếu không tin bất cứ một vấn đề gì, thậm chí nếu không tin mình, các bạn có thể bỏ follow mình, không theo dõi fanpage của mình nhưng đừng bao giờ hỏi một câu là "{question_replace}?", không hay ho một chút nào cả, các bạn nhá! Một là block, hai là xóa, không có chuyện cứ nhai đi nhai lại cái một câu là "{question_replace}?')
async def setup(client):
    await client.add_cog(bomb(client))



if __name__ == "__main__":
    print("Mahiru#1542")
from discord.ext import commands
import discord
import sys
import json
import asyncio
import time
import os

class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
    def get_time():
        return time.strftime("%a, %b %d, %Y | %H:%M:%S")

    @commands.command(name="test")
    async def test(self, ctx):
        try:
            host = ctx.author.name+"#"+ctx.author.discriminator
            quiz_ = await quiz.get_quiz_content()
            # --Starting games Embed--
            embed = discord.Embed(title="Quiz Battle | Nơi bạn thể hiện cái đầu của mình", color=discord.Color.from_rgb(191,255,0))
            embed.set_author(
                    name=host,
                    url=ctx.author.avatar
                )
            embed.add_field(name= "Thể lệ cuộc chơi: ", value="Gồm 15 câu hỏi từ mọi lĩnh vực khác nhau, mỗi câu có từ 2-4 đáp án.", inline=False)
            embed.add_field(name= "Cách trả lời: ", value="Nhập số từ 1-4 theo thứ tự của các câu trả lời, câu trả lời sẽ là tin nhắn bạn nhắn trong channel cuối cùng (thay đổi phương án bằng cách nhắn tin lại).", inline=False)
            embed.add_field(name= "Cách tính điểm: ", value="Thời gian và điểm mỗi câu hỏi sẽ hiển thị trên embed, trả lời đúng thì được điểm.", inline=False)
            embed.add_field(name= "Thời gian nghỉ giữa mỗi câu hỏi: ", value="Thời gian nghỉ giữa mỗi câu hỏi sẽ là 7 giây, trong lúc đó các bạn có thể nhắn bất kì tin nhắn nào trong channel có event đó.", inline=False)
            embed.add_field(name= "Cách tham gia: ", value="React vào reaction ở dưới để được đăng kí tham gia, sau khi minigame khởi động thì sẽ có 60 giây để đăng kí và chuẩn bị.", inline=False)
            embed.add_field(name= "Và cuối cùng: ", value="Chúc các bạn may mắn và có được kết quả tốt >.<", inline=False)
            embed.set_footer(text="Hosted by {} | {}".format(host,quiz.get_time()))
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            # await asyncio.sleep(5)
            msg_react = await ctx.channel.fetch_message(msg.id)
            print(msg_react)
            users = set()
            for reaction in msg_react.reactions:
                async for user in reaction.users():
                    users.add(user)
            await ctx.send(f"users: {', '.join(str(user.id) for user in users)}")
            print(msg_react)
            c = 5
            msg2 = await ctx.send("Trận đấu sẽ diễn ra sau {} giây.".format(c))
            while True:
                c -=1
                await msg2.edit(content="Trận đấu sẽ diễn ra sau {} giây.".format(c))
                await asyncio.sleep(1)
                if c ==0:
                    break

            # users_react.pop(users_react.index(self.client.user)=               
            # print(users_react)
            # quiz_w = {
            #     "Đây là anime gì ?":{
            #         "answers": ["Thiên sứ nhà bên", "Anh Chàng Băng Giá Và Cô Nàng Lạnh Lùng"],
            #         "correct": 0,
            #         "times": 10,
            #         "points": 5
            #         },
            #     "Đây là anime gì 2":{
            #         "answers": ["Thiên sứ nhà bên", "Anh Chàng Băng Giá Và Cô Nàng Lạnh Lùng"],
            #         "correct": 0,
            #         "times": 15,
            #         "points": 1
            #         }
            # }
            # for key, value in quiz.items():
            #     print("{}| Times: {}  | Points: {}".format(
            #     key,
            #     value["times"],
            #     value["points"]
            #     ))
            # for i in value["answers"]:
            #     print(i)
            # ans = input()
            # if value["correct"] == int(ans)-1:
            #     print("dung roi")
            # else:
            #     print("sai roi")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)


    async def get_quiz_content():
        with open(os.path.join("json","quiz","quiz.json"),"r", encoding="utf8") as f:
            return json.loads(f.read())
async def setup(client):
    await client.add_cog(quiz(client))



if __name__ == "__main__":
    print("Mahiru#1542")
# from redvid import Downloader
# from moviepy.editor import VideoFileClip
# import os
# import requests
  
# subreddit = 'jakertown'
# limit = 100
# timeframe = 'month' #hour, day, week, month, year, all
# listing = 'top' # controversial, best, hot, new, random, rising, top
  
# def get_reddit(subreddit,listing,limit,timeframe):
#     try:
#         base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
#         request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
#     except:
#         print('An Error Occured')
#     return request.json()
  
# r = get_reddit(subreddit,listing,limit,timeframe)
# for filename in os.listdir("./temp"):
#     if filename.endswith(".mp4"):
#         os.remove(os.path.join("temp",filename))
# reddit = Downloader()
# reddit.auto_max = True
# reddit.max_s = 4 * (1 << 20)
# reddit.path = os.path.join("temp")
# reddit.url = f"{r['data']['children'][0]['data']['url']}"
# reddit.download()


# for filename in os.listdir("./temp"):
#     if filename.endswith(".mp4"):
#         videoClip = VideoFileClip(os.path.join("temp",filename))
#         videoClip.write_gif(os.path.join("temp","my-life.gif"))


# to_extract = ['title','url','score','num_comments','view_count','ups','downs','selftext',"approved_at_utc","is_video"]
 
# for e in to_extract:
#     print(f"{e}: {r['data']['children'][0]['data'][e]}")




quiz = {
    "Đây là anime gì ?":{
        "answers": ["Thiên sứ nhà bên", "Anh Chàng Băng Giá Và Cô Nàng Lạnh Lùng"],
        "correct": 0,
        "times": 10,
        "points": 5
        },
    "Đây là anime gì 2":{
        "answers": ["Thiên sứ nhà bên", "Anh Chàng Băng Giá Và Cô Nàng Lạnh Lùng"],
        "correct": 0,
        "times": 15,
        "points": 1
        }
}



for key, value in quiz.items():
    print("{}| Times: {}  | Points: {}".format(
        key,
        value["times"],
        value["points"]
    ))
    for i in value["answers"]:
        print(i)
    ans = input()
    if value["correct"] == int(ans)-1:
        print("dung roi")
    else:
        print("sai roi")




        

import shutil

shutil.rmtree('config')

from instabot import Bot  

bot = Bot()
bot.login(username = "__shehzaadiiii__", password = "01729417185274")

bot.download_stories('thecrimsonheat/2585043278678034839/')
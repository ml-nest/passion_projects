from instabot import Bot
from time import sleep
import random
import time
import shutil


shutil.rmtree('config')



bot = Bot(unfollow_delay = 30)
bot.login(username = "__shehzaadiiii__", password = "01729417185274")

following = bot.get_user_following("__shehzaadiiii__")
i = 0
for user in reversed(following[:-500]): 
	username = bot.get_username_from_user_id(user)
	print("Attempting to unfollow: ", username)
	if bot.unfollow(username):
		i += 1
		print("Unfollowed - "+str(i)+"  ", username)
	else:
		print("Failed to unfollow - ", username)
	if(i >= 50):
		break

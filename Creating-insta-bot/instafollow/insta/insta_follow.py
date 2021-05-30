from instabot import Bot
from time import sleep
import random
import time
import shutil


file_contents = open("config/skipped.txt").read()
skip_list = file_contents.splitlines()

shutil.rmtree('config')

#bot = Bot(follow_delay = 20, filter_users=True, filter_private_users=True)
bot = Bot(follow_delay = 20)
bot.login(username = "__shehzaadiiii__", password = "01729417185274")

def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


my_following = bot.get_user_following('__shehzaadiiii__')
my_following = my_following + skip_list + bot.get_user_followers('__shehzaadiiii__')

accounts = []
accounts.append("chotiibachiii")

net_follower = []
for acc in accounts:
    followers = bot.get_user_followers(acc)
    net_follower = net_follower + followers

net_follower = unique(net_follower)
tobe_followed = [x for x in net_follower if x not in my_following]
print('people to be followed : '+ str(len(tobe_followed)))

old_skipped = 0

for i in tobe_followed:
    bot.follow(i)

    with open('config/followed.txt') as f:
        new_foll = f.readlines()
        
    print('New following : ' + str(len(new_foll)))
    if len(new_foll) == 50:
        textfile = open("config/skipped.txt").read()
        new_skip_list = textfile.splitlines()
        textfile = open("config/skipped.txt", "w")
        skip_list = skip_list + new_skip_list
        for element in skip_list:
            textfile.write(element + "\n")
        textfile.close()
        exit()
    """
    with open('config/skipped.txt') as f:
        new_skpped = f.readlines()
    
    if len(new_skpped)==old_skipped:
        x = random.randint(0,5000)/100
        print('sleeping for ' + str(x)+' sec.')
        time.sleep(x)
    else:
        old_skipped = len(new_skpped)
    """
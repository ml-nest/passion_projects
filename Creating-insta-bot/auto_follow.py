# Importing packages
from instabot import Bot
from time import sleep
import random
import time
import shutil
import pickle

from IPython.display import clear_output


with open('skip_list.pkl', 'rb') as f:
    skip_list = pickle.load(f)

shutil.rmtree('config')

bot = Bot(follow_delay = 20, filter_users=True, filter_private_users=True)
bot.login(username = "__shehzaadiiii__", password = "Bharat9417185274")
clear_output()

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
my_following = my_following + bot.get_user_followers('__shehzaadiiii__')
my_following = my_following + skip_list

accounts = []
accounts.append("devcolonyconfession")

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
    if len(new_foll) == 30:
        textfile = open("config/skipped.txt").read()
        new_skip_list = textfile.splitlines()
        textfile = open("config/skipped.txt", "w")
        skip_list = skip_list + new_skip_list
        for element in skip_list:
            textfile.write(element + "\n")
        textfile.close()

        file_contents = open("config/skipped.txt").read()
        skip_list = file_contents.splitlines()

        with open('skip_list.pkl', 'wb') as f:
            pickle.dump(skip_list, f)
            
        clear_output()
        break
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

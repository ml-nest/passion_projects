from instabot import Bot
# from time import sleep

bot = Bot();

 bot = Bot(follow_delay = 10, unfollow_delay = 10, max_follows_per_day = 10000, max_unfollows_per_day = 10000);

bot.login(username = "irrational__human", password = "9417185274");


def follow(bot, followers, followCount, amt):
	lower = followCount;
	#upper = min(followCount + amt, len(followers));
	count = 0;
	#follow
	for user in followers[lower:]: 
		if count >= amt:
			return count;
		username = bot.get_username_from_user_id(user);
		print("Attempting to follow:", username);
		if bot.follow(username):
			print("Followed! -", username);
			count += 1;
		else:
			print("Not Followed! -", username);
		
# 	return count;

# def unfollow(bot, amt):
# 	following = bot.get_user_following("postleg__");
# 	i = 0;
# 	for user in reversed(following[:-100]): 
# 		username = bot.get_username_from_user_id(user);
# 		print("Attempting to unfollow:", username);
# 		if bot.unfollow(username):
# 			i += 1;
# 			print("Unfollowed -", username);
# 		else:
# 			print("Failed to unfollow -", username);
# 		if(i >= amt):
# 			break;

# 	return True;

# def filter(bot, amt):
# 	following = bot.get_user_following("postleg__");

# 	addToAcc = [];

# 	for user in following[:amt]: 
# 		username = bot.get_username_from_user_id(user);
# 		user_info = bot.get_user_info(user)
# 		bio = user_info['biography'];
# 		username = user_info['username'];
# 		name = user_info['full_name'];
# 		followers = user_info['follower_count'];
# 		following = user_info['following_count'];
# 		if "meme" in bio.lower() or "meme" in name.lower() or "meme" in username.lower()	:
# 			if followers > 1000 and followers < 9000:
# 				if following/followers < 1.2:
# 					addToAcc.append(username);
# 	return addToAcc;

#

# accounts = [];
# accounts.append("moisty_meme_bros"); #automate this part!

# amt = 120;

# for acc in accounts:

# 	followers = bot.get_user_followers(acc);
# 	followCount = 1200;

# 	while followCount <= len(followers):

# 		sleep(3000);

# 		followCount += follow(bot, followers, followCount, amt);

# 		sleep(3600); #delay for an hour


# 		unfollow(bot, amt);
		
# 		accounts.append(filter(bot,amt));
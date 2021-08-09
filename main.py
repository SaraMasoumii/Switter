import os

from application import *
from database import *

a = Application()

def clear():
	os.system('cls||clear')

def tweet():
	text = input('- Enter your Tweet: ')
	a.tweet(text)
	print('Your tweet has successfully tweeted.')

def mention(parTweet: Tweet):
	text = input('- Enter your mention: ')
	a.mention(text, parTweet)
	print('Your mention has successfully mentioned')

def retweet(parTweet: Tweet):
	a.retweet(parTweet)
	print('The tweet has successfully retweeted')

def like(parTweet: Tweet):
	if a.hasLiked(parTweet):
		a.unlike(parTweet)
		print('The tweet has successfully unliked')
	else:
		a.like(parTweet)
		print('The tweet has successfully liked')

def printTweet(tweet: Tweet):
	print(f"Date: {tweet.date}")
	if tweet.retweeter != '0':
		print(f"ReTweeted by @{tweet.retweeter}:")
	print(f"@{tweet.username}:")
	print(f"{tweet.text}\n")

def printLike(like: Like):
	print(f"@{like.username}")

def showLikes(tweet: Tweet):
	likes = a.getLikesFromTweet(tweet)
	if len(likes) == 0:
		print("No one has liked this tweet yet!")
	else:
		for like in likes:
			printLike(like)

def showTweets(tweets: List[Tweet]):
	if len(tweets) == 0:
		print("Nothing to show here!")
		return
	idx = len(tweets) - 1
	while True:
		tweet = tweets[idx]
		clear()
		printTweet(tweet)
		while True:
			cm = input("- Choose a command (next/prev/back/retweet/like/mention/likes/mentions): ")
			if cm == 'next':
				if idx - 1 >= 0:
					idx -= 1
					break
				else:
					print("You have reached the end!")
					continue
			elif cm == 'prev':
				if idx + 1 < len(tweets):
					idx += 1
					break
				else:
					print("You have reached the top!")
					continue
			elif cm == 'back':
				clear()
				return
			elif cm == 'like':
				like(tweet)
			elif cm == 'retweet':
				retweet(tweet)
			elif cm == 'mention':
				mention(tweet)
			elif cm == 'likes':
				showLikes(tweet)
			elif cm == 'mentions':
				mentions = a.getMentionsFromTweet(tweet)
				showTweets(mentions)
				break
			else:
				print("Invalid Command!\nPlease try again!")


clear()
print('** Welcome to Switter! ** \n')
print('Created by Sarah Masoumi.\n')

while True:
	while not a.isLoggedIn():
		cm = input("- Choose a command (login/register): ")
		clear()
		if cm == 'login':
			username = input('- Username: ')
			password = input('- Password: ')
			try:
				a.login(username, password)
				break
			except:
				print('\nPlease try again!\n')
		elif cm == 'register':
			username = input('- Enter your username: ')
			password = input('- Enter your password: ')
			check_password = input('- ReEnter your password: ')
			if password != check_password:
				print("Passwords don't match!\nPlease try again!")
			else:
				try:
					a.register(username, password)
					break
				except:
					print('Please try again!')
		else:
			print("Invalid Command!\nPlease try again!")
			continue

	clear()
	print("Logged In!\n")

	while True:
		cm = input("- Choose a command (timeline/tweet/logout): ")
		if cm == 'timeline':
			showTweets(a.getTimeline())
		elif cm == 'tweet':
			tweet()
		elif cm == 'logout':
			a.logout()
			clear()
			print("Logged Out!\n")
			break
		else:
			print("Invalid Command!\nPlease try again!")
			continue

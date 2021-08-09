import os
import sys
from application import *
from database import *

a = Application()

def clear():
	os.system('cls||clear')

def printTweet(tweet: Tweet):
	print(f"Date: {tweet.date}\n")
	if tweet.retweeter != '0':
		print(f"ReTweeted by @{tweet.retweeter}:\n")
	print(f"@{tweet.username}:\n")
	print(f"{tweet.text}:\n")

def showLikes(tweet: Tweet):
	likes = a.getLikesFromTweet(tweet)

def showTweets(tweets: List[Tweet]):
	if len(tweets) == 0:
		print("Nothing to show here!\n")
		return
	idx = len(tweets) - 1
	while True:
		clear()
		tweet = tweets[idx]
		printTweet(tweet)
		while True:
			cm = input("- Choose a command (next/prev/back/like/retweet/mention/showlikes/showmentions): ")
			if cm == 'next':
				if idx - 1 >= 0:
					idx -= 1
					break
				else:
					print("\nYou have reached the end!\n")
					continue
			elif cm == 'prev':
				if idx + 1 < len(tweets):
					idx += 1
					break
				else:
					print("\nYou have reached the top!\n")
					continue
			elif cm == 'back':
				clear()
				return
			elif cm == 'like':
				pass
			elif cm == 'retweet':
				pass
			elif cm == 'mention':
				pass
			elif cm == 'showlikes':
				pass
			elif cm == 'showmentions':
				mentions = a.getMentionsFromTweet(tweet)
				showTweets(mentions)

def tweet():
	text = input('Enter your Tweet:')
	a.tweet(text)
	print('Your tweet is successfully tweeted.')


def mention(parTweet: Tweet):
	text = input('Enter your mention:')
	a.mention(text, parTweet)
	print('Your mention is successfully mentioned')


def retweet(parTweet: Tweet):
	a.retweet(parTweet)
	print('The tweet is successfully retweeted')

def like(parTweet: Tweet):
	a.like(parTweet)

clear()
print('** Welcome to Switter! ** \n')
print('Created by Sarah Masoumi.\n')
while not a.isLoggedIn():
	cm = input("- Choose a command (login/register): ")
	clear()
	if cm == 'login':
		while True:
			username = input('- Username: ')
			password = input('- Password: ')
			try:
				a.login(username, password)
				break
			except:
				print('\nPlease try again!\n')
	elif cm == 'register':
		while True:
			username = input('- Enter your username: ')
			password = input('- Enter your password: ')
			check_password = input('- ReEnter your password: ')
			if password != check_password:
				print("\nPasswords don't match!\nPlease try again!\n")
			else:
				try:
					a.register(username, password)
					break
				except:
					print('\nPlease try again!\n')
	else:
		print("Invalid Command!\nPlease try again!\n")
		continue

while True:
	cm = input("- Choose a command (timeline/tweet/logut): ")
	if cm == 'timeline':
		showTweets(a.getAllTweets())
	elif cm == 'tweet':
		pass
	elif cm == 'logout':
		a.logout()
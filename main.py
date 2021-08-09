import os
import sys
from application import *
from database import *


def clear():
    os.system('cls||clear')


def printTweet(tweet: Tweet):
    print(f"Date: {tweet.date}\n")
    if tweet.retweeter != '0':
        print(f"ReTweeted by @{tweet.retweeter}:\n")
    print(f"@{tweet.username}:\n")
    print(f"{tweet.text}:\n")


def showTweets(tweets: List[Tweet]):
    if len(tweets) == 0:
        print("Nothing to show here!")
        return
    idx = len(tweets) - 1
    while True:
        showTweets(tweets[idx])



def tweet(text: str):
    a.tweet(text)
    print('Your tweet is successfully tweeted.')


def mention(text: str, parTweet: Tweet):
    a.mention(text, parTweet)
    print('Your mention is successfully mentioned')


def retweet(parTweet: Tweet):
    pass

def like():
    pass


a = Application()
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



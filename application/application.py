from datetime import datetime
from typing import List

from database.database import Database

from application.like import Like
from application.tweet import Tweet
from application.user import User


class Application:

	def __init__(self) -> None:
		self.database = Database('application/schema.txt')
		self.user = None
		self.latestTweetID = len(self.getAllTweets())

	def getDate(self): 
		return datetime.today().strftime('%Y-%m-%d')

	def login(self, username: str, password: str) -> None:
		list = self.database.query(f"SELECT FROM Users WHERE username={username} AND password={password}")
		if len(list) == 0:
			raise ValueError('Invalid Username or Password!')
		self.user = User(username=username, password=password)

	def logout(self) -> None:
		self.user = None

	def register(self, username: str, password: str) -> None:
		try:
			self.database.query(f"INSERT INTO Users VALUES ({username},{password},{self.getDate()})")
		except:
			raise ValueError("Invalid Data!")
		self.user = User(username=username, password=password)
		
	def getTweetsFromUser(self, user: User) -> List[Tweet]:
		list = self.database.query(f"SELECT FROM Tweets WHERE username={user.username}")
		tweets = []
		for dic in list:
			tweet = Tweet(**dic)
			tweets.append(tweet)
		return tweets

	def getAllTweets(self) -> List[Tweet]:
		list = self.database.query("SELECT FROM Tweets")
		tweets = []
		for dic in list:
			tweet = Tweet(**dic)
			tweets.append(tweet)
		return tweets

	def getLikesFromTweet(self, tweet: Tweet) -> List[Like]:
		list = self.database.query(f"SELECT FROM Likes WHERE id={tweet.id}")
		likes = []
		for dic in list:
			like = Like(**dic)
			likes.append(like)
		return likes

	def getMentionsFromTweet(self, tweet: Tweet) -> List[Tweet]:
		list = self.database.query(f"SELECT FROM Tweets WHERE parID={tweet.parID}")
		mentions = []
		for dic in list:
			mention = Tweet(**dic)
			mentions.append(mention)
		return mentions
	
	def _auth(func):
		def authorizedFunc(self, *args):
			if self.user == None:
				raise ValueError('You should login first!')
			return func(self, *args)
		return authorizedFunc

	@_auth
	def tweet(self, text: str) -> Tweet:
		convertedText = text.replace(' ', '$')
		tweet = Tweet(id=str(self.latestTweetID + 1), text=text, username=self.user.username, retweeter='0', date=self.getDate(), parID='0')
		self.database.query(f"INSERT INTO Tweets VALUES ({tweet.id},{convertedText},{tweet.username},{tweet.retweeter},{tweet.date},{tweet.parID})")
		self.latestTweetID += 1
		return tweet

	@_auth
	def mention(self, text: str, parTweet: Tweet) -> Tweet:
		convertedText = text.replace(' ', '$')
		tweet = Tweet(id=str(self.latestTweetID + 1), text=text, username=self.user.username, retweeter='0', date=self.getDate(), parID=parTweet.id)
		self.database.query(f"INSERT INTO Tweets VALUES ({tweet.id},{convertedText},{tweet.username},{tweet.retweeter},{tweet.date},{tweet.parID})")
		self.latestTweetID += 1
		return tweet
	
	@_auth
	def retweet(self, tweet: Tweet) -> Tweet:
		convertedText = tweet.text.replace(' ', '$')
		tweet = Tweet(id=str(self.latestTweetID + 1), text=tweet.text, username=tweet.username, retweeter=self.user.username, date=self.getDate(), parID='0')
		self.database.query(f"INSERT INTO Tweets VALUES ({tweet.id},{convertedText},{tweet.username},{tweet.retweeter},{tweet.date},{tweet.parID})")
		self.latestTweetID += 1
		return tweet

	@_auth
	def like(self, tweet: Tweet) -> Like:
		like = Like(id=tweet.id, username=self.user.username)
		self.database.query(f"INSERT INTO Likes VALUES ({like.id},{like.username})")
		return like

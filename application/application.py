from typing import List

from database.database import Database

from application.tweet import Tweet
from application.user import User


class Application:

	def __init__(self) -> None:
		self.database = Database('application/schema.txt')

	def login(self, username: str, password: str) -> None:
		self.user = User(username, password)
		pass

	def logout(self) -> None:
		pass

	def register(self, username: str, password: str) -> None:
		user = User(username, password)
		
	def getTweetsFromUser(self, user: User) -> List[Tweet]:
		list = self.database.query(f"SELECT FROM Tweets WHERE username={user.username}")
		tweets = []
		for dic in list:
			tweet = Tweet(dic)
			tweets.append(tweet)
		return tweet

	def getAllTweets(self) -> List[Tweet]:
		pass

	def getLikesFromTweet(self, tweet: Tweet) -> List[Like]:
		pass

	def getMentionsFromTweet(self, tweet: Tweet) -> List[Tweet]:
		pass

	def tweet(self, text: str):
		pass

	def mention(self, text: str, parTweet: Tweet):
		pass

	def retweet(self, tweet: Tweet):
		pass

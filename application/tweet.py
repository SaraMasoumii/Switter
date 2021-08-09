from typing import Dict


class Tweet:

	def __init__(self, **kwargs) -> None:
		self.id = kwargs['id']
		self.text = kwargs['text'].replace('$', ' ')
		self.username = kwargs['username']
		self.retweeter = kwargs['retweeter']
		self.date = kwargs['date']
		self.parID = kwargs['parID']
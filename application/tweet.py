from typing import Dict


class Tweet:
	
	def __init__(self, id: str, text: str, username: str, retweeter: str, date: str, parID: str = None) -> None:
		self.id = id
		self.text = text
		self.username = username
		self.retweeter = retweeter
		self.date = date
		self.parID = parID

	def __init__(self, dict: Dict[str, str]) -> None:
		self.id = dict['id']
		self.text = dict['text']
		self.username = dict['username']
		self.retweeter = dict['retweeter']
		self.date = dict['date']
		self.parID = dict['par_id']
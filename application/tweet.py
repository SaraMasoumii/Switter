class Tweet:
	
	def __init__(self, id: str, text: str, author: str, date: str, parID: str = None) -> None:
		self.id = id
		self.text = text
		self.author = author
		self.date = date
		self.parID = parID
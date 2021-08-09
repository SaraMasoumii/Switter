class User:
	
	def __init__(self, **kwargs) -> None:
		self.username = kwargs['username']
		self.password = kwargs['password']
		self.date = kwargs['date']
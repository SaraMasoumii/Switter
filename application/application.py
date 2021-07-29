from database.database import Database


class Application:

	def __init__(self) -> None:
		self.database = Database('application/schema.txt')

	def register(self, username: str, password: str) -> None:
		# 
		pass

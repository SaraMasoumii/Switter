
from typing import List

class File:

	def __init__(self, path: str) -> None:
		self.path = path

	def read(self):
		with open(self.path, 'r') as file:
			for line in file:
				yield line
		yield '\n'

	def write(self, lines: List[str], append: bool = False) -> None:
		mode = 'w'
		if append:
			mode = 'a'
		with open(self.path, mode) as file:
			for line in lines:
				file.write(line + '\n')
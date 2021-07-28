
from typing import List

class File:

	def __init__(self, path: str) -> None:
		self.path = path

	def read(self):
		with open(self.path, 'r') as file:
			for line in file:
				yield line.rstrip()
		yield ''

	def write(self, lines: List[str], append: bool = False) -> None:
		mode = 'w'
		if append:
			mode = 'a'
		with open(self.path, mode) as file:
			for line in lines:
				file.write(line + '\n')

	def replace(self, old: str, new: str) -> None:
		with open(self.path, 'r') as file :
  			data = file.read()
		data = data.replace(old, new)
		data = data.replace('\n\n', '\n')
		with open(self.path, 'w') as file:
  			file.write(data)
	
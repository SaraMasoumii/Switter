import datetime
import re

class Field:

	def __init__(self, type: str, unique: bool) -> None:

		self.type = type
		self.unique = unique


	def isValueble(self, value: str) -> bool:

		if ' ' in value:
			return False

		t = self.type
		if t == 'INTEGER':
			try:
				int(value)
				return True
			except:
				return False

		elif t == 'BOOLEAN':
			return value == '1' or value == '0'

		elif t == 'TIMESTAMP':

			if type(value) != str:
				return False

			try:
				datetime.datetime.strptime(value, '%Y/%m/%d')
				return True

			except ValueError:
				return False

		elif re.match('^CHAR\((\d+)\)$', t):

			l = int(re.findall("CHAR\((\d+)\)", t)[0])
			return len(value) <= l

		return False
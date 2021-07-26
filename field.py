import datetime
import re

class Field:
	
	def __init__(self, type: str, unique: bool) -> None:

		self.type = type
		self.unique = unique


	def isValueble(self, value: str) -> bool:

		t = self.type
		if t == 'INTEGER':
			try:
				int(t)
				return True
			except:
				return False

		elif t == 'BOOLEAN':
			return t == '1' or t == '0'

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
			return type(value) == str and len(value) <= l

		return False
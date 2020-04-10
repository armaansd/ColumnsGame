class Faller:
	def __init__(self,info):
		self.falling = True
		self.gems = (info.split(" "))
		self.in_col = int(self.gems[1])
		self.info = {}
		in_row = -1
		for i in reversed(range(3,)):
			self.info[self.gems[i+2]] = (in_row, self.in_col)
			in_row -= 1

	def print(self):
		print(self.info)
		

import Faller

class Matrix:
	def __init__(self,row,col):
		self.row = row
		self.col = col
		self.grid = [[0 for i in range(col)] for j in range(row)]

	def drop(self,faller):
		if not faller.falling:
			return

		for gem,coor in faller.info.items():
			r,c = coor
			if r+1<self.row:
				if self.grid[r+1][c] == 0: 
					r += 1
					faller.info[gem] = r,c
					if r >= 0:
						self.grid[r][c] = gem
						if r > 0:
							self.grid[r-1][c] = 0
				else:
					faller.falling = False
			else:
				faller.falling = False




	def print(self):
		for i in range(self.row):
			print('|',end="")
			for j in range(self.col):
				if self.grid[i][j] == 0:
					print("   ",end="")
				else:
					print(" {} ".format(self.grid[i][j]),end="")
			print('|')
		print("",self.col*"___","")

	def print_plain(self):
		print(self.grid)




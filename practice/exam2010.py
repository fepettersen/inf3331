class Foo:
	def __init__(self,i,j):
		self.i,self.j = i,j

	def __str__(self):
		return "(%d,%d)"%(self.i,self.j)

	def __setitem__(self,idx,v):
		if idx ==0:
			self.i= v
		elif idx ==1:
			self.j = v
		else:
			raise RuntimeError("index out of bounds [0,1]")

class Bar(Foo):
	def __init__(self,i,j):
		Foo.__init__(self,i,j)

	def __repr__(self):
		return "Bar(%d,%d)"%(self.i,self.j)

	def __getitem__(self,idx):
		if idx ==0:
			return self.i
		elif idx ==1:
			return self.j
		else:
			raise RuntimeError("index out of bounds [0,1]")

	def __eq__(self,b):
		if self.i==b[0] and self.j==b[1]:
			return True
		else:
			return False
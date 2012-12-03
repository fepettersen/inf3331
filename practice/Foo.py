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


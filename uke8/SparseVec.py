class SparseVec:

	def __init__(self,a):
		self.a=a
		self.nonzeros = {}
		if type(a)!=int:
			print "Converting %f to %d"
			self.a = int(a)
		self.x = [0]*a
		
	def __setitem__(self,i,value):
		if i>=len(self.x):
			print "Index Error! Index out of range"
			sys.exit(1)
		self.x[i] = value
		if value !=0:
			self.nz(i,value)
			
	def nz(self,i,value):
		self.nonzeros[i]=value
		
	def __add__(self,other):
		c=[]
		if len(self.x)!=len(other.x):
			if len(self.x)<len(other.x):
				c = other.x
				for i in range(len(self.x)):
					c[i] = other.x[i]+self.x[i]
			elif len(other.x)<len(self.x):
				c = self.x
				for i in range(len(other.x)):
					c[i] = other.x[i]+self.x[i]
		else:
			c = [self.x[i]+other.x[i] for i in range(len(self.x))]
		return c
	'''
	def __print__(self,arg):
    g = len(arg)
    __builtins__.print('g = ',g)
    ##return __builtins__.print(*args, **kwargs)
    '''

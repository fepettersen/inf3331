class SparseVec:

	def __init__(self,a):
		self.a=a
		self.nz = {}
		self.current = 0
		
	def __setitem__(self,i,value):
		if i>=self.a:
			import sys
			print "Index Error! Index out of range"
			sys.exit(1)
		#self.nz[i] = value
		if value !=0:
			self.nz[i]=value
			
	def nonzeros(self):
		return self.nz
	
	def __getitem__(self,i):
		if i>=self.a:
			import sys
			print "Index Error! Index out of range"
			sys.exit(1)
		if i in self.nz.keys():
			return self.nz[i]
		else:
			return 0
			
			
	def __add__(self,other):
		counter = 0
		max_size = max(self.a,other.a)
		c=SparseVec(max_size)
		while counter<max_size:
			if counter in self.nz.keys() and counter in other.nz.keys():
				c[counter] = self.nz[counter]+other.nz[counter]
			elif counter in self.nz.keys() and not counter in other.nz.keys():
				c[counter] = self.nz[counter]
			elif counter in other.nz.keys() and not counter in self.nz.keys():
				c[counter] = other.nz[counter]
			counter +=1
		return c
		
	def __str__(self):
		counter = 0
		lst = []
		while counter<self.a:
			if counter in self.nz.keys():
				lst.append('[%d]=%g'%(counter,self.nz[counter]))
			else:
				lst.append('[%d]=0'%counter)
			counter +=1
		s = " ".join(lst)
		return s
		
	def __iter__(self):
		return self
	
	def next(self):
		if self.current > self.a-1:
			raise StopIteration
		else:
			if self.current in self.nz.keys():
				a = self.nz[self.current]
			else:
				a=0
			self.current +=1
		return a,self.current -1
		
'''
>>> from SparseVec import SparseVec
>>> v = SparseVec(9)
>>> v[3] = 9
>>> v[6]=21
>>> for ai,i in v:
...     print 'a[%d]=%g ' % (i, ai)
... 
a[0]=0 
a[1]=0 
a[2]=0 
a[3]=9 
a[4]=0 
a[5]=0 
a[6]=21 
a[7]=0 
a[8]=0 
>>> print v
[0]=0 [1]=0 [2]=0 [3]=9 [4]=0 [5]=0 [6]=21 [7]=0 [8]=0
>>> u = SparseVec(7)
>>> u[3]=-2
>>> u[5]=3
>>> c = u+v
>>> print c.nonzeros()
{3: 7, 5: 3, 6: 21}
'''

"""
A class for simple operations with 3 dimensional vectors
"""
class Vec3D:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		"""return a formatted string"""
		return'(%g,%g,%g)'%(self.x,self.y,self.z)
	def __repr__(self):
		"""return the type of object"""
		return 'Vec3D(%g,%g,%g)'%(self.x,self.y,self.z)
	def __getitem__(self,i):
		"""Subscripting"""
		if i==0: return self.x
		elif i==1: return self.y
		elif i==2: return self.z
		else: print 'Index out of range'
	def __setitem__(self,i,a):
		"""Subscripting with assignment"""
		if i==0: self.x=a
		elif i==1: self.y=a
		elif i==2: self.z=a
		else: print 'Index out of range'
	def __add__(self,v):
		"""Vector-vector addition"""
		return self.x+v[0],self.y+v[1],self.z+v[2]
	def __sub__(self,v):
		"""Vector-vector subtraction"""
		return self.x-v[0],self.y-v[1],self.z-v[2]
	def __pow__(self,v):
		"""Vector -vector cross product"""
		return self.y*v[2]-self.z*v[1],-(self.x*v[2]-self.z*v[0]),self.x*v[1]-self.y*v[0]
	def __mul__(self,v):
		"""Vector-vector scalar (dot) product aka inner product"""
		return self.x*v[0] + self.y*v[1] + self.z*v[2]
	def len(self):
		"""Euclidian norm (length) of vector"""
		from math import sqrt
		return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
		
'''
Runtime example:
>>> from vec3d import Vec3D
>>> u = Vec3D(1, 0, 0)  # (1,0,0) vector
>>>  v = Vec3D(0, 1, 0)
  File "<stdin>", line 1
    v = Vec3D(0, 1, 0)
    ^
IndentationError: unexpected indent
>>> v = Vec3D(0, 1, 0)
>>> str(u)
'(1,0,0)'
>>> repr(u)
'Vec3D(1,0,0)'
>>> u.len() # Euclidian norm
1.0
>>> u[1]
0
>>> v[2] = 2.5
>>> print u**v
(0.0, -2.5, 1)
>>> u+v
(1, 1, 2.5)
>>> u-v
(1, -1, -2.5)
>>> u*v
0.0
'''

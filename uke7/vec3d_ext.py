"""
An extended class for simple operations with 3 dimensional vectors
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
		"""vector - vector or vector - scalar addition"""
		t = type(v)
		if t==int or t==float:
			return self.x+v,self.y+v,self.z+v
		elif t==list or t==tuple:
			print 'Operation not defined'
		else:	
			return self.x+v[0],self.y+v[1],self.z+v[2]
	def __radd__(self,v):
		"""vector - vector or vector - scalar addition"""
		t = type(v)
		if t==int or t==float:
			return self.x+v,self.y+v,self.z+v
		elif t==list or t==tuple:
			print 'Operation not defined'
		else:	
			return self.x+v[0],self.y+v[1],self.z+v[2]
	def __sub__(self,v):
		"""Vector-vector and vector -scalar subtraction"""
		t = type(v)
		if t==int or t==float:
			return self.x-v,self.y-v,self.z-v
		elif t==list or t==tuple:
			print 'Operation not defined'
		else:
			return self.x-v[0],self.y-v[1],self.z-v[2]
	def __rsub__(self,v):
		"""Vector-vector and vector - scalar subtraction"""
		t = type(v)
		if t==int or t==float:
			return v-self.x,v-self.y,v-self.z
		elif t==list or t==tuple:
			print 'Operation not defined'
		else:
			return self.x-v[0],self.y-v[1],self.z-v[2]
	def __pow__(self,v):
		"""Vector -vector cross product"""
		return self.y*v[2]-self.z*v[1],-(self.x*v[2]-self.z*v[0]),self.x*v[1]-self.y*v[0]
	def __mul__(self,v):
		"""Vector-vector scalar (dot) product aka inner product"""
		t = type(v)
		if t==int or t==float:
			return self.x*v,self.y*v,self.z*v
		elif t==tuple or t==list:
			print 'Operation is not defined'
		else:
			return self.x*v[0] + self.y*v[1] + self.z*v[2]
	def __rmul__(self,v):
		"""Vector-vector scalar (dot) product aka inner product"""
		t = type(v)
		if t==int or t==float:
			return self.x*v,self.y*v,self.z*v
		elif t==tuple or t==list:
			print 'Operation is not defined'
		else:
			return self.x*v[0] + self.y*v[1] + self.z*v[2]

	def len(self):
		"""Euclidian norm (length) of vector"""
		from math import sqrt
		return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
'''
>>> from vec3d_ext import Vec3D
>>> u = Vec3D(1,1,1)
>>> a = 3
>>> u*a
(3, 3, 3)
>>> a*u
(3, 3, 3)
>>> a+u
(4, 4, 4)
>>> u+a
(4, 4, 4)
>>> u-a
(-2, -2, -2)
>>> a-u
(2, 2, 2)
>>> 
'''

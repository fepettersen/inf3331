from numpy import *

class Integrator:
	def __init__(self,a,b,n=100):
		self.a,self.b,self.n = a,b,n
		self.points, self.weights = self.construct_method()

	def construct_method(self):
		raise NotImplementedError('no rule in class %s'%self.__class__.__name__)

	def integrate(self,f):
		s = 0
		for i in range(len(self.weights)):
			s+= self.weights[i]*f(self.points[i])

		return s

	def vectorized_integrate(self,f):
		return dot(self.weights,f(self.points))

class Midpoint(Integrator):
	def construct_method(self):
		a,b,n = self.a,self.b,self.n
		h = (b-a)/float(n)
		x = linspace(a+0.5*h,b-0.5*h,n)
		w = zeros(len(x)) +h
		return x,w

class Trapezoidal(Integrator):
	def construct_method(self):
		a,b,n = self.a,self.b,self.n
		h = (b-a)/float(n-1)
		x = linspace(a,b,n)
		w = zeros(len(x)) +h
		w[0] /=2.0
		w[-1] /= 2.0
		return x,w

class Simpson(Integrator):
	def __init__(self,a,b,n):
		Integrator.__init__(self,a,b,n)

	def construct_method(self):
		a,b,n = self.a,self.b,self.n
		if n%2!=1:
			print "n=%d must be odd, 1 is added"%n
			n+=1
		x = linspace(a,b,n)
		h = (b-a)/float(n-1)*2
		w = zeros(len(x))
		w[0:n:2] = h/3.0
		w[1:n:2] = h*2.0/3.0
		w[0] /=2.0
		w[-1] /= 2.0
		return x,w

class F:
	def __init__(self,m=3.1415926):
		self.m=float(m)

	def __call__(self,t):
		m = self.m
		return (1+(1/m))*t**(1/m)
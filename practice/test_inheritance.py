from Integrator import *

def f(x):
	return 2*x**2 -3

a,b,n = 0,1,51
m = Simpson(a,b,n)
func = F()
res= m.vectorized_integrate(func)

print "Simpsons method gives %g"%res
func.m =5
res = m.vectorized_integrate(func)
print "Simpsons method gives %g"%res
print repr(m)

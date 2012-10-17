import time,math
from numpy import *

def f_1(x):
	if type(x)==ndarray:
		f = zeros(shape(x))
		f[0:] = x[0:]+1
		return f
	else:
		return 1+x

def f_2(x):
	if type(x) == ndarray:
		f = zeros(shape(x))
		f[0:] = exp(-x[0:]*x[0:])*log(x[0:]+x[0:]*sin(x[0:])) #The math module didn't like vectors
		return f
	else:
		return math.exp(-x*x)*math.log(x+x*math.sin(x)) #Use math module expressions for speed

n = 1e7
a = 1.0; b = 3.0
h = (b-a)/(n+1)

x = linspace(a,b,n+1)
I_scalar_1 = 0
I_vec_1 = 0
I_scalar_2 = 0
I_vec_2 = 0

#------first integral scalar 
s_start_1 = time.clock()
i=1
while i<n:
	#run through and sum up f(a+i*h) for i=1,2,...,n-1
	I_scalar_1 +=f_1(x[i])
	i+=1
I_scalar_1 += 0.5*(f_1(a)+f_1(b)) 	#special formulae for the boundarys
I_scalar_1 *=h						#scale the result by h
s_stop_1 = time.clock()
time1 = s_stop_1-s_start_1

#------first integral vectorized
v_start_1 = time.clock()
#run through and sum up f(a+i*h) for i=1,2,...,n-1 vectorized
I_vec_1 = sum(f_1(x[1:-1]))
I_vec_1 += 0.5*(f_1(a)+f_1(b))	#special formula for the boundarys
I_vec_1 *= h
v_stop_1 = time.clock()
time2 = v_stop_1-v_start_1

#------second integral scalar
s_start_2 = time.clock()
i=1
while i<n:
	#run through and sum up f(a+i*h) for i=1,2,...,n-1
	I_scalar_2 +=f_2(x[i])
	i+=1
I_scalar_2 += 0.5*(f_2(a)+f_2(b))	#special formula for the boundarys
I_scalar_2 *=h
s_stop_2 = time.clock()
time3 = s_stop_2-s_start_2

#-------second integral vectorized
v_start_2 = time.clock()
#run through and sum up f(a+i*h) for i=1,2,...,n-1 vectorized
I_vec_2 = sum(f_2(x[1:-1]))
I_vec_2 += 0.5*(f_2(a)+f_2(b))		#special formula for the boundarys
I_vec_2 *= h
v_stop_2 = time.clock()
time4 = v_stop_2-v_start_2

print "----------First integral----------"
print "Scalar: %1.9f in %g seconds"%(I_scalar_1,time1)
print "Vectorized: %1.9f in %g seconds"%(I_vec_1,time2)

print "----------Second integral----------"
print "Scalar: %1.9f in %g seconds"%(I_scalar_2,time3)
print "Vectorized: %1.9f in %g seconds"%(I_vec_2,time4)

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke7$ python vectorize_integration.py 
----------First integral----------
Scalar: 5.999999400 in 17.95 seconds
Vectorized: 5.999999400 in 0.08 seconds
----------Second integral----------
Scalar: 0.127498531 in 27.24 seconds
Vectorized: 0.127498531 in 0.98 seconds
'''

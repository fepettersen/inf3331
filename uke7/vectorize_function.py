from numpy import *

def initial_condition(x):
	if type(x) == int or type(x) ==float:
	    return 3.0
	elif type(x) == ndarray:
		I = zeros(shape(x))
		I[0:]=3.0
		return I
	else:
		return None
		
x = 0
Init_scalar = initial_condition(x)
y = zeros(15)
Init_vec = initial_condition(y)
print "Scalar result: ", Init_scalar
print "Vectorized result: ", Init_vec 

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke7$ python vectorize_function.py 
Scalar result:  3.0
Vectorized result:  [ 3.  3.  3.  3.  3.  3.  3.  3.  3.  3.  3.  3.  3.  3.  3.]
'''

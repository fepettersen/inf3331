from numpy import *
import sys,time

try:
	N = int(sys.argv[1])
except:
	print "Provide number of throws on commandline"
	sys.exit(1)
	

start_vec = time.clock()
d1 = random.random_integers(1,6,N)		# Draws N random integers between 1 and 6
d2 = random.random_integers(1,6,N)		# same
						
a1 = where(d1==6)						# saves the indeces where the throw results in a 6
a2 = where(d2==6)						# same
d3 = mod(d1+d2,12)						# finds out where both dice gave a 6
a3 = where(d3==0)						# finds how many times we threw two 6'es

prob_vec =  (size(a1)+size(a2)-size(a3))/float(N) # Probability of throwing one or more 6

stop_vec = time.clock()
timediff_vec = stop_vec-start_vec

start_scalar = time.clock()
p = 0;
for i in range(1,N+1):					# Same as in dice2.py
	a = random.randint(1,7)				# Numpy's randint does not include the upper limit
	b = random.randint(1,7)
	if a==6 or b==6:
		p+=1

prob_scalar = float(p)/float(N)
stop_scalar = time.clock()
timediff_scalar = stop_scalar-start_scalar
exact = 11.0/36
print "Time spent on %d throws by NumPy: %g"%(N,timediff_vec)
print "Time spent on %d throws by normal Python: %g"%(N,timediff_scalar)
print "---------------------Results----------------------------------"
print "Vectorized: %g which has the error %g"%(prob_vec,exact-prob_vec)
print "Scalar: %g which has the error %g"%(prob_scalar,exact-prob_scalar)

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice2_NumPy.py 5000000
Time spent on 5000000 throws by NumPy: 0.48
Time spent on 5000000 throws by normal Python: 2.04
---------------------Results----------------------------------
Vectorized: 0.30547 which has the error 8.51556e-05
Scalar: 0.30575 which has the error -0.000194044
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice2_NumPy.py 50000000
Time spent on 50000000 throws by NumPy: 4.9
Time spent on 50000000 throws by normal Python: 20.82
---------------------Results----------------------------------
Vectorized: 0.305589 which has the error -3.38444e-05
Scalar: 0.305685 which has the error -0.000129884
'''

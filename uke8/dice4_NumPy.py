from numpy import *
import sys,time
try:
	N = int(sys.argv[1])
except:
	print "Please specify the number of throws on the commandline."
	sys.exit(1)
result = zeros(N)
start_vec = time.clock()
dice = random.random_integers(1,6,size=(N,4))			# N throws of 4 dice
result[:] = dice[:,0]+dice[:,1]+dice[:,2]+dice[:,3]		# Sum of the dice
a = where(result<10)									# How many times was the sum 9 or less
total_vec = 10*size(a)-size(result)						# Money spent and prize money
stop_vec = time.clock()

start_scalar = time.clock()
prize = 10;
money = 1;
for i in range(1,N+1):									# Same as in dice4.py
	money -=1;
	a = random.randint(1,7);
	b = random.randint(1,7);
	c = random.randint(1,7);
	d = random.randint(1,7);
	result = a+b+c+d;
	if result<9:
		money +=prize;
	
stop_scalar = time.clock()
diff1 = stop_vec-start_vec
diff2 = stop_scalar-start_scalar
print "%d rounds of the game took %g s vectorized, and %g s scalar"%(N,diff1,diff2)
'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice4_NumPy.py 10000
10000 rounds of the game took 0 s vectorized, and 0.01 s scalar
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice4_NumPy.py 100000
100000 rounds of the game took 0.01 s vectorized, and 0.08 s scalar
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice4_NumPy.py 1000000
1000000 rounds of the game took 0.1 s vectorized, and 0.77 s scalar
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice4_NumPy.py 10000000
10000000 rounds of the game took 0.92 s vectorized, and 7.5 s scalar
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python dice4_NumPy.py 50000000
50000000 rounds of the game took 4.74 s vectorized, and 38.21 s scalar
'''

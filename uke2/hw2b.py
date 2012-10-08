import sys
from math import sin

r= 1;
if len(sys.argv) ==1 :
	print 'Please provide some numbers on the commandline'
	sys.exit()
else:
	print 'Hello, world!'
	while r<= len(sys.argv) -1:
		print 'sin(%g) = %.4f' % (float(sys.argv[r]),sin(float(sys.argv[r])))
		r +=1

'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke2$ python hw2b.py 3.14 5.3 0.001 2.75 1.1 32 4.0093
Hello, world!
sin(3.14) = 0.0016
sin(5.3) = -0.8323
sin(0.001) = 0.0010
sin(2.75) = 0.3817
sin(1.1) = 0.8912
sin(32) = 0.5514
sin(4.0093) = -0.7628
'''

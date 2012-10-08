import sys
from math import log as ln
r=1
if len(sys.argv) == 1:
	print 'Please provide some numbers on the commandline'
else:
	print 'Hello, world!'
	while r<=len(sys.argv)-1:
		if float(sys.argv[r])<0.0:
			print'ln(%g) is not defined for real numbers'  %float(sys.argv[r])
		else:
			print'ln(%g) = %.4f' %(float(sys.argv[r]),ln(float(sys.argv[r])))
		r +=1

'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke2$ python hw2c.py 3.14 5.3 0.001 2.75 -1.1 32 4.0093
Hello, world!
ln(3.14) = 1.1442
ln(5.3) = 1.6677
ln(0.001) = -6.9078
ln(2.75) = 1.0116
ln(-1.1) is not defined for real numbers
ln(32) = 3.4657
ln(4.0093) = 1.3886
'''

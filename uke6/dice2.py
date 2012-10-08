"""
Program which simulates throwing 2 dice n times and calculates the probability of scoring at least one 6
"""
import random, sys
try:
	n = int(sys.argv[1])
	number = int(sys.argv[2])
except:
	print "You suck!"
	sys.exit()
p = 0;
for i in range(1,n+1):
	a = random.randint(1,6)
	b = random.randint(1,6)
	if a==number or b==number:
		p+=1

print "The probability of scoring at least one %d is approximately %g" %(number,float(p)/n)

'''
We are looking for 11/36 = 0.3055555555...6
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke6$ python dice2.py 500000 6
The probability of scoring at least one 6 is approximately 0.305722
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke6$ python dice2.py 500000 6
The probability of scoring at least one 6 is approximately 0.305434
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke6$ python dice2.py 500000 6
The probability of scoring at least one 6 is approximately 0.305918
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke6$ python dice2.py 500000 6
The probability of scoring at least one 6 is approximately 0.305074
'''

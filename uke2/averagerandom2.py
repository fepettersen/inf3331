'''
default program:
#!/usr/bin/ env python
import sys, random
def compute(n):
     i = 0; s = 0
     while i <= n:
         s += random.random()
          i += 1
     return s/n

n = sys.argv[1] 
print 'the average of %d random numbers is %g" % (n, compute(n))
'''
#corrected program:

#!/usr/bin/env python  <--cannot have space
import sys, random
def compute(n):
     i = 0; s = 0
     while i <= n-1:	#<-- need n-1 to compute the correct average
	s += random.random()
	i += 1	# <-- Indentation error
     return s/n

n = int(sys.argv[1]) # <-- need to make the commandline arg. into int
print 'the average of %d random numbers is %g' % (n, compute(n))
# Used wrong fnutts to end the string in the above print argument
'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke2$ python averagerandom2.py 78
the average of 78 random numbers is 0.47043
'''

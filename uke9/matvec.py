import numpy as np		#import numpy

A = np.array([[1, 2, 3], [4, 5, 7], [6, 8, 10]], float)
b = np.array([-3, -2, -1], float)

print np.dot(A,b)		#let numpy do the multiplication

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke9$ python matvec.py 
[-10. -29. -44.]
'''

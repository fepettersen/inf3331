from scitools.numpytools import *
x = sequence(0, 1, 0.5)

# y = 2*x + 1:
y = x;  y *= 2;  y += 1

# z = 4*x - 4:
z = x;  z *= 4;  z -= 4
print x, y, z

'''
The problem is that numpy "uses" pointers. This means that the statement y=x sets y to point to the same values as x. Thus changing the values in y will also change the values in x. The same goes for z.
A quick (but not very elegant) fix is the following
'''
X = sequence(0, 1, 0.5)

# y = 2*x + 1:
Y = X.copy();  Y *= 2;  Y += 1

# z = 4*x - 4:
Z = X.copy();  Z *= 4;  Z -= 4
print "------ Repaired ----------"
print X,Y,Z

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke8$ python NumPy_assignment.py 
[ 0.  4.  8.] [ 0.  4.  8.] [ 0.  4.  8.]
------ Repaired ----------
[ 0.   0.5  1. ] [ 1.  2.  3.] [-4. -2.  0.]
'''

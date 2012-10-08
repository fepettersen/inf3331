import re

real = \
r"\s*(?P<number>-?(\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?)\s*"
c = re.compile(real)
some_interval = "[3.58652e+05 , 6E+09]"
groups = c.findall(some_interval)
print groups
lower = float(groups[0][c.groupindex['number']-1])
upper = float(groups[1][c.groupindex['number']-1])
#Fixed indeces in groups[]. len(groups)=2 ==> groups[2] out of bounds.
print "lower: " ,lower
print "upper: " ,upper

'''
As far as I understand this excercise, the fix was to change the indexing from groups[1], groups[2] to groups[0], groups[1] and subtract 1 from the groupindex.

fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke4$ python findallerror.py
[('3.58652e+05', '3.58652', '.58652', 'e+05'), ('6E+09', '6', '', 'E+09')]
lower:  3.58652
upper:  6.0
'''

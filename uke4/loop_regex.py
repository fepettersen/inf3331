import re
 # -*- coding: utf-8 -*-
loop1 = r'[0:12]'     # 0,1,2,3,4,5,6,7,8,9,10,11,12
loop2 = r'[0:12, 40]'  # 0,4,8,12


r1 = r'\[(\d+):(\d+),?\s*(\d+)?(?=[\]])\]'

groups = re.search(r1, loop1).groups()
print groups
#groups2 = re.search(r1, loop2).groups()
#print groups2
'''
if (len(groups[-1]) != 0):
	g0= float(groups[0])
	g1 =float(groups[1])
	g2= float(groups[2])
	A=[g0+g2*i for i in range(int((g1-g0)/g2)+1)]
	print A 
else:
	g0= float(groups[0])
	g1 =float(groups[1])
	A=[g0 +i for i in range(int((g1-g0)+1))]
	print A
'''
#------------------------
#r1 = r'\[(.+):(.+?),?(.*)\]' 
#r2 = r'\[(.+):(.+),?(.*)\]'
#range(int(groups[0]),int(groups[1])+1,int(groups[2]))
'''r1 and r2 fail because they look for numbers given on the form of the input: a bracet  followed by any character "a" and a colon : . A new character "b" an optional comma,(which could also be interpreted as a character) and an optional number c ended by a bracket .'''

'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke4$ python loop_regex.py 
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke4$ python loop_regex.py 
[0.0, 4.0, 8.0, 12.0]

'''

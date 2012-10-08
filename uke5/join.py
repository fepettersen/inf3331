def join(st0,*ls0):
	"""
	Joins strings on different sorts of input
	"""
	somelist = []; string = ''
	for i in ls0:
		if not isinstance(i,str):
			if type(i)==list or type(i)==tuple:
				for j in i:
					somelist.append(str(j))
			elif type(i) == float:
				somelist.append(str(i))
			elif type(i) == int:
				somelist.append(str(i))
		else:
			somelist.append(i)
	
	for e in range(len(somelist)):
		string += somelist[e]
		if somelist[e] != somelist[-1]:
			string+=st0
		
	return string

list1 = ['s1','s2','s3']
tuple1 = ('s4','s5')
exe = join(' ',13,list1, tuple1,'ks','mv')
#print exe

'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke5$ python join.py
 13 s1 s2 s3 s4 s5 ks mv 

'''

"""
Simulation of hazard game
Input is number of times to play the game (assuming you keep playing regardless of how much you loose), how much money you start with, what sum you need to throw less than to win and the size of the prize.
"""
import random,sys
try:
	n = int(sys.argv[1])
	extra = int(sys.argv[2])
	threshold = int(sys.argv[3])
	prize = int(sys.argv[4])
except:
	print"You suck!"
	sys.exit()

money = 1+extra;
for i in range(1,n+1):
	money -=1;
	a = random.randint(1,6);
	b = random.randint(1,6);
	c = random.randint(1,6);
	d = random.randint(1,6);
	result = a+b+c+d;
	if result<threshold:
		money +=prize;
counter = 0
money1 = 1+extra
while money1>0 and counter <n:
	money1 -=1;
	a = random.randint(1,6);
	b = random.randint(1,6);
	c = random.randint(1,6);
	d = random.randint(1,6);
	result = a+b+c+d;
	if result<threshold:
		money1 +=prize;
	counter += 1;

print"Starting with %d of some currency you are now left with %d after playing the game %d times. \n"%(1+extra,money,n)
print "Giving up when you are out on money gives you %d turns. \n"% counter

'''
It seems like this is a game one should stay away from
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke6$ python dice4.py 100 0 9 10
Starting with 1 of some currency you are now left with -19 after playing the game 100 times. 

Giving up when you are out on money gives you 1 turns. 
'''

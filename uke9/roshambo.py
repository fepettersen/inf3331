"""
Play a game of rock-paper-scissors in the terminal
"""
import re, random, sys

print 'Welcome to rocks paper scissors!'
n = int(raw_input('How many points to win? '))
php = 0		#petty human points
acp = 0		#awesome computer points

def determine_move(h):
	"""Determine the user input through regular expressions"""
	rock_pattern = r'\br.*'
	scissor_pattern = r'\bs.*'
	paper_pattern = r'\bp.*'
	rock = re.search(rock_pattern,h,re.IGNORECASE)
	paper = re.search(paper_pattern,h,re.IGNORECASE)
	scissor = re.search(scissor_pattern,h,re.IGNORECASE)
	if rock:
		return 1
	else:
		return 2 if paper else 3
		
def verbose(lst):
	"""Translate the moves of the players into words"""
	new_lst = [0]*len(lst)
	for i in range(len(lst)):
		if lst[i] == 1:
			new_lst[i]='Rock'
		elif lst[i] == 2:
			new_lst[i] = 'Paper'
		else:
			new_lst[i] = 'Scissors'
	return new_lst

while php < n and acp < n:
	"""Plays the game until one player reaches the predetermined score"""
	try:
		h = determine_move(raw_input('Choose (R)ock, (P)aper, or (S)cissors? '))
		c = random.randint(1,3)		#1=rock	2=paper	3=scissor
		h_move,c_move = verbose([h,c])
		if c==1 and h==2 or c==2 and h==3 or c==3 and h==1: #Cases where the human player wins
			php+=1
			print 'Human: %s    Computer: %s     Human wins this round' %(h_move,c_move)
		elif c==1 and h==3 or c==2 and h==1 or c==3 and h==2: #Cases where the computer wins
			acp+=1
			print 'Human: %s    Computer: %s     Computer wins this round' %(h_move,c_move)
		else:				#Tie
			print 'Human: %s    Computer: %s     Tie, the round continues' %(h_move,c_move)
	except EOFError:   # Catch the Ctrl-D
		print '\n You ended the game, no one wins'
		sys.exit(1)
		
winner = 'Computer' if acp>php else 'Human'
print 'game over! %s wins the game'%winner

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke9$ python roshambo.py 
Welcome to rocks paper scissors!
How many points to win? 3
Choose (R)ock, (P)aper, or (S)cissors? Rock
Human: Rock    Computer: Scissors     Human wins this round
Choose (R)ock, (P)aper, or (S)cissors? PAper
Human: Paper    Computer: Rock     Human wins this round
Choose (R)ock, (P)aper, or (S)cissors? S
Human: Scissors    Computer: Rock     Computer wins this round
Choose (R)ock, (P)aper, or (S)cissors? s
Human: Scissors    Computer: Paper     Human wins this round
game over! Human wins the game
'''

# -*- coding: utf-8 -*-
from random import randint 
import re

def determine_move(h):
    """Determine the user input through regular expressions"""
    beginner_pattern = r'\bb.*'
    intermediate_pattern = r'\bi.*'
    advanced_pattern = r'\ba.*'
    beginner = re.search(beginner_pattern,h,re.IGNORECASE)
    intermediate = re.search(intermediate_pattern,h,re.IGNORECASE)
    advanced = re.search(advanced_pattern,h,re.IGNORECASE)
    if beginner:
        return 10
    elif intermediate:
        return 25 
    elif advanced:
          return 100
    else:
          print'Sorry, level not recognized. continuing with default level\
          (beginner)'
          return 10

def determine_operand(h):
    """Determine the user input through regular expressions"""
    sub_pattern = r'\bs.*'
    mul_pattern = r'\bm.*'
    div_pattern = r'\bd.*'
    sub= re.search(sub_pattern,h,re.IGNORECASE)
    mul = re.search(mul_pattern,h,re.IGNORECASE)
    div = re.search(div_pattern,h,re.IGNORECASE)
    if sub:
        return 0
    elif mul:
        return 1 
    elif div:
        return 2
    else:
        return 3
          
def restart(answer,score,i):
    """restarts the ongoing quiz"""
    pattern = r'\br.*'
    restart_pattern =  r'\by.*'
    reset =re.search(pattern,answer,re.IGNORECASE)
    if reset:
            ans = raw_input('Are you sure you want to restart the quiz? [Y/N]: ')
            Ans = re.search(ans,restart_pattern,re.IGNORECASE)
            if Ans:
                score = 0
                i = 0
    return score, i
    
correct = 0
games = input("How many questions do you want? ")
level = raw_input("Which level would you like? (B)eginner, (I)ntermediate\
 or (A)dvanced ")
operator = raw_input("What kind of questions do you want? (A)ddition, (S)ubtraction, \
(M)ultiplication or (D)ivision ")
j = determine_operand(operator)
operation = ['-','*','/','+']
limit = determine_move(level)
print "Answer a question with restart to restart the quiz \n"
i=0

while i<=games:
    i+=1
    prod = 0
    n1 = randint(1, limit)
    n2 = randint(1, limit)
    if j==0:
        prod = n1 - n2
    elif j==1:
        prod = n1*n2
    elif j==2:
        prod = float(n1/n2)
    else:
        prod = n1+n2
    ans = raw_input("What's %d %s %d? " % (n1,operation[j], n2))
    correct,i = restart(ans,correct,i)
    if eval(ans) == prod:
        print "That's right -- well done.\n"
        correct = correct + 1
    else:
        print "No, I'm afraid the answer is %d.\n" % prod



print "\nI asked you %d questions.  You got %d of them right." % (games,correct)

if (float(correct/games)>=2./3):
    print "Well done!"
elif (float(correct/games)<=2./3) and (float(correct/games)>=1./3):
    print "You need more practice"
else:
    print "Please ask your math teacher for help!"
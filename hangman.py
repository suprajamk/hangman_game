#!/usr/bin/python

def getword():
	import random
	f=open('words.txt','r')
	lines=f.readlines()
	return random.choice(lines).strip()

def getindices(word,char):
	return [i for i, ltr in enumerate(word) if ltr == char]

guessword=list(getword())
print len(guessword)*'_'
tobeguessed=list(len(guessword)*'_')
lives=7
print "You have 7 lives!!!"
while lives !=0 :
	if ('_' in tobeguessed):
		userinput=raw_input("Please guess a letter: ")
		matchedinput = getindices(guessword,userinput)

		if matchedinput:
			for i in matchedinput:
				tobeguessed[i]=guessword[i] 
				print tobeguessed
		else:
			lives-=1;
			if lives == 0 :
				print "Sorry u lose!"
			else:
				print "Sorry u lose a life! You have " + str(lives) + " left!"

	else:
		print "You win!"
		lives = 0

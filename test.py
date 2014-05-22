"""
vacation_spots = {"CHRIS": "Tahoe", "CASSIE": "Hawaii", "ROBERT": "Zoo",}

print("This program will identify where you want to travel to")

while(True):

	name = raw_input("Please enter your name: ")
	if name.upper() in vacation_spots: 
		print("This person wants to go here: " + vacation_spots[name.upper()])
	else:
		add_newname = raw_input("Name does not exsist would you like to add it to the dictionary? (yes/no)")
		if add_newname == "yes":
			location = raw_input ("Where would you like to go?")
			vacation_spots[name.upper()] = location
			print("Information saved for "+ name +" who wants to go to " + location + "!")
"""

"""
import random

Heads = 0
Tails = 0 

print("This program simulates a coin toss")

while(True):
	Heads = 0
	Tails = 0 

	Amount_toss = raw_input("How many coin flips do you want the program to do?: ")

	for i in xrange(0, int(Amount_toss)):
		rando = random.randint(1,100) 
		if rando <= 51:
			print("Heads")
			Heads = Heads + 1

		else:
			print ("Tails")
			Tails = Tails + 1
	print("Heads: " + str(Heads))
	print("Tails: " + str(Tails))
	if Heads > Tails:
		print("Heads is the winner")
	elif Heads < Tails:
		print ("Tails is the winner")
	else:
		print ("They are the same")


	go_again = raw_input("Would you like to go again? (yes/no): ")
	if go_again.lower() == "no":
		break
print("the program has been closed")

"""
"""


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
"""
"""
#square all elemnts then add the sum of squares
print 1**2
a = 1**2
print 2**2
b = 2**2
print 3**2 
c = 3**2
print 4**2
d = 4**2
print 5**2
e = 5**2
radnumbers = (a + b + c + d + e)

print('radnumbers: ' + str(radnumbers))

a = 1 + 3 + 27 + 2 + 2123
print(a)
"""

"""
def printSixes():
  	for i in range(1,100):
  		if i % 2 == 0:
  			print ("i is even")
		else:
			print ("i is odd")
"""
"""
Heads = 0
Tails = 0 

print("This program simulates a coin toss")

while(True):
	Heads = 0
	Tails = 0 

	Amount_toss = raw_input("How many coin flips do you want the program to do?: ")

	for i in xrange(0, int(Amount_toss)):
		rando = random.randint(1,100) ## choice. 
		if rando <= 51:
			print("Heads"),
			Heads = Heads + 1

		else:
			print ("Tails")
			Tails = Tails + 1
	print("Heads: " + str(Heads))
	print("Tails: " + str(Tails))
	if Heads > Tails:
		print("Heads is the winner")
	elif Heads < Tails:
		print ("Tails is the winner")
	else:
		print ("They are the same")


	go_again = raw_input("Would you like to go again? (yes/no): ")
	if go_again.lower() == "no":
		break
print("the program has been closed")
"""

"""
#import random
import random


#start the loop
while(True):
	heads = 0
	tails = 0
	rando = random.randint(1,100)
	Amount_toss = raw_input("How many coin flips do you want the program to do?: ")
    	for i in xrange(0, int(Amount_toss)):
			rando = random.randint(1,100) 
			if rando <= 51:
				heads +=1
				print("heads")
			else:	
				tails +=1
				print("tails")

	print("Heads came up", heads, "times")
  	print("Tails came up", tails, "times")
  	go_again = raw_input("Would you like to go again? (yes/no): ")
	if go_again.lower() == "no":
		break
print("the program has been closed")

"""
"""
import random
while(True):
	number_desired = raw_input("How many cards would you like to be randomly generated?: ")
	rank = ("1", "2", "3","4","5","6","7","8","9","10","11","12","13")
	suits = ("21","22","23","24")
	suits1 = {"21":"hearts", "22":"spades", "23":"diamonds", "24":"clubs"}
	
	deck = {}
	for i in xrange(0, int(number_desired)):
		rank = random.randint(1,13)
		print(rank)
		
		

	for j in xrange(0, int(number_desired)):
		suits = random.randint(21,24)
		
		if suits == 21:
			print("hearts")
		if suits == 22:
			print("spades")
		if suits == 23:
			print("diamonds")
		if suits == 24:
			print("clubs")
			
"""
"""
import random

def pick_suits(n):
	suits = ["hearts", "spades", "diamonds", "clubs"]
	return suits(n)
def pick_rank(n):
	rank = ["1", "2", "3","4","5","6","7","8","9","10","11","12","13"]
	return rank(n)



while(True):

	def numberruns(n)=
		number_desired = raw_input("How many cards would you like to be randomly generated?: ")
		return(int(number_desired)) 

key = 0 
deck = {}

for i in xrange(0, int(number_runs)):
		rank = random.randint(1,13)
		print(rank)
"""
"""
import turtle
wn = turtle.screen()
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)

"""
"""
def printSixes():
  for i in range(1,101):
    if(i % 6 == 0):
      print(i)

"""

import random

while(True):
	raw_number = raw_input("How many cards would you like to be randomly generated?: ")
	number_desired = int(raw_number)
	rank = ["ace", "2", "3","4","5","6","7","8","9","10","jack","queen","king"]
	suits = ["hearts", "spades", "diamonds", "clubs"]
	deck = {}

	
	
	
	for j in xrange(0, number_desired):
		rando = random.randint(0,12)
		#print(rank[rando])
		suit_index = random.randint(0,3)
		#print (suits[suit_index])
		print((rank[rando]) + "of" + (suits[suit_index]) ) 

    
		
			


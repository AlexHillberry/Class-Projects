# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Alex Hillberry>
# Creation Date: <07/26/2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.


import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	# This print function does nothing; correction would be to \n after the 3 ''' above and close parenthesis or close
 	# and reprint on a new line with print(" ").
	print()
	# pep8 suggests function names be lowercase, this could read def choose_cave():
def chooseCave():
    cave = ''
	# indentation should be left aligned
while cave != '1' and cave != '2':
	print('Which cave will you go into? (1 or 2)')
	cave = input()
	# A return cannot belong in a while loop because the loop's exit is a boolean operator. An if statement could use
	# return for instance. # Additionally, it is returning caves, not cave.
	return caves
	# This should read def check_cave(chosen_cave):
def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		# missing both parenthesis for print statement.
		print'Gobbles you down in one bite!'

playAgain = 'yes'
	# Should read while playAgain == 'yes' or 'y': the second playAgain is redundant.
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		# Should read "Thanks for Playing"
		print("Thanks for planing")


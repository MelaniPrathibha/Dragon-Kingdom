import random 
import time

def display_intro():	#display introduction
	print("""You are in the Kingdom of Dragons.
In front of you, you see four caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragons are hungry and will eat you on sight.""")

def choose_cave():	#Ask from user to enter a valid cave number
	cave = ''     # local variable with empty string 
	caves = ['1','2','3','4']    
	while cave not in caves:          
		print('Which cave will you go into? (1,2,3,4)')          
		cave = input()     
	return cave 

def check_cave(chosen_cave):	#check whether user entered cave is friendly or not
	print('You approach the cave...') 
	time.sleep(2) 		#pause the program for two seconds to build some suspense in the game
	print('A large dragon jumps out in front of you! ') 
	print('He opens his jaws and...')      
	time.sleep(2)
	friendlyCave = random.randint(1, 4)	#Change the friendly cave randomly

	if chosen_cave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down!')

play_again = 'y' 				#allow user to play again as much as he want
while play_again.lower() == 'y':
	#call the functions
	display_intro()
	cave_number  = choose_cave()
	check_cave(cave_number)
	print("Do you want to play again? (y/n)")	#ask whether the user needs to play or not
	play_again = input()


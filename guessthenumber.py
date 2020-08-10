# "Guess The Number" Game
# Project Created by Himanshu Raj (Follow me on Instagram @himanshuhsr)
# Posted on - Kernel Bytes 

# First create a function for the last section of the game when either user will guess the right number or user will exceed 
# the maximum guess limit then this function will come into action. This will give two options either to opt for 
# restart the game or exit.
def last(username):
	# Print Username
	print(f"Hello! {username}.")
	# Ask for input as 1 for restart and 2 for exit
	lastcall=int(input("Enter your choice 1 for restart 2 for exit"))

	# Check the user input is it 1 or 2 or entered a wrong number if entered 1 then call the main() function for 
	# restarting the game. If input is 2 then use "raise SystemExit" for exit from the game. If Entered number other than
	# 1 or 2 then give a warning that you have entered wrong choice and recall the last() function for getting input again.
	if (lastcall==1):
		print("Restarting the game......")
		main()
	if (lastcall==2):
		print("Closing the game....")
		raise SystemExit
	else:
		print("You have entered a wrong choice. Try again!")
		last(username)



def main():

	# Import the random library so that you can use for selecting a random number
	import random
	# Set the GuessesTaken = 0 initially it will be used to calculate the guess limit.
	guessesTaken = 0

	# Print Welcome Message
	print("Hello! Welcome to the 'Guess The Number' game")
	# Ask the username
	username=str(input("Enter the Name Please : "))

	# Put an alert message of starting the game
	print(f"Well {username}! Let's start the game.")

	# Ask for selecting the level of game with number 1 for 'Easy', 2 for 'Medium' and 3 for 'Difficult'.
	print("Select the level of game. For 'Easy' enter 1, for 'Medium' enter 2, for 'Difficult' enter 3.")
	# Take the userinput for medium
	medium=int(input("Enter your choice: "))

	# Now check the input what user have selected and set the last number for consideration during selecting random
	# number and maximum guess allowed for 'Easy' lastnumber = 20, maximum guess allowed to 4 similarly for 'Medium' 50 & 6 , 
	# for 'Difficult' 100 & 10. If user will enter number other than 1,2 & 3 put a warning message and restart the game.
	if (medium==1):
		lastnumber=20
		maxguess=4
		print(f"{username}, you have selected 'Easy' level.")
	elif (medium==2):
		lastnumber=50
		maxguess=6
		print(f"{username}, you have selected 'Medium' level.")
	elif (medium==3):
		lastnumber=100
		maxguess=10
		print(f"{username}, you have selected 'Difficult' level.")
	els
		print("You have entered a wrong choice. Try Again!")
		print("Restarting the game....")
		main()

	# Now select a random number as per level using randint function by passing two parameter the lower and upper limit
	number = random.randint(1, lastnumber)
	# Put a notification message of playing game along with rules i.e, how many guess is allowed and between which they have to guess.
	print(f"WELL {username} LET'S PLAY GAME!")
	print(f"I am going to select a number in my mind between 1-{lastnumber}.")
	print(f"You have {maxguess} chance to guess what is in my mind. If you done so then you will win or otherwise you will loose.")
	
	# Now use while loop for checkimg the maximum guess allowed
	while guessesTaken<maxguess:
		# Ask for input of guess
		print("Take a guess. What is in my mind?")
		guess = int(input("Enter your guess: "))
		
		# After each guess increase the guessTaken by 1
		guessesTaken = guessesTaken +1

		# Check that the guess is greater or less or equal to the number selected. If greater put a hint that your guess is high
		# , if guess is low put hint as your guess is low, if equal then end the while loop. Otherwise this loop will terminate
		# after exceeding the maximum guess allowed as per level.
		if guess<number:
			print(f"{username}, Your guess is low. Try again!")
		if guess>number:
			print(f"{username}, Your guess is high. Try again!")
		if guess==number:
			break

	# If guess is equal to number then put the congratulation message and let them know how many guess they taken to guess rigght number.
	if guess==number:
		print(f"Great Job {username}! You guessed right in just {guessesTaken} guesses.")
		print(f"Congratulations {username}! You won the game.")

	# If guess is not equal to number put the sorry message and let them know they have loose the game. Initiate the last() function for 
	# restart the game or exit. Pass the username as parameter so that you can use username in last() function.
	if guess!=number:
		print(f"Sorry {username}! You failed to guess the number. I have selected {number} in my mind.")
		print(f"{username}! You loose the game. Better Luck Next Time!")
	last(username)

# Start this project by calling main() function.
main()

# If you liked this project please share it with your friend. Upload to GitHub as one of your project and don't forget
# to follow "Kernel Bytes" on Facebook and Instagram for more interesting projects. Also put your doubts in comment section.

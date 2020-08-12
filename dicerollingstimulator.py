# Dice Rolling Stimulator. This will roll the dice for you and print out the number on dice by selecting random number.
# Program written by Himanshu Raj for Kernel Bytes. Folllow me on instagram @himanshuhsr

# First of all create a function
def main():
        # Import 'random' library it will be used for generating random numbers
        import random
        # Set the n to y it will help you in rolling the dice for the first time.
        n='y'
        #Print Welcome Message and rules of "Rolling Dice".
        print("Welcome to the Dice Stimulator!\n")
        print("\n Rules : \n 1. Press y for rolling the dice.\n 2. Press n for exit.\n")
        # Ask the user his/her name for customizing the messages or comments.
        name= str(input("\n Enter Your Name : ") )
        print("\n")
        # Put the rolling intiation message 
        print(f"Hey {name}!, Rolling the dice for you.....\n")
        # Use while loop for making decision that if n is equal to y then only roll the dice again
        while n == 'y':
                # Use "randint" function for generating random number between 1 and 6
                number= random.randint(1,6)
                # Customise the message according for printing the random number
                if number == 1 or number == 2:
                        print(f"Hey {name}, Bad Luck! You have got {number} on the dice.\n")
                elif number == 3 or number == 4:
                        print(f"Hey {name}, Not Bad! You have got {number} on the dice.\n")
                elif number == 5 or number == 6:
                        print(f"Hey {name}, Wow Lucky one! You have got {number} on the dice.\n")
                # After printing the dice rolling result ask for the next move and check the input and take decisions accordingly
                n = str(input(f"Hey {name}! Enter 'y' for rolling the dice again and 'n' for exit. "))
                print("\n")
                if n == 'y' or n == 'n':
                        # If users enter n then exit the dice rolling stimulator
                        if n=='n':
                                print(f"Hey {name}, Exiting the game....\n")
                                raise SystemExit
                        if n == 'y':
                                pass
                # If user enters character other than y or n restart the stimulation.
                else:
                        print(f"Hey {name}! You have entered wrong choice. We are restarting the game.....\n")
                        main()


main()

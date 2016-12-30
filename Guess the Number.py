# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# initialize global variables
num_range = 100
number_of_guesses = 7
secret_number = 0

# helper function to start and restart the game
def new_game():
    ### resets game to new game state ###
    global num_range, number_of_guesses, secret_number 
    if num_range == 100:
        secret_number = num_range - random.randrange(0, 100)
        number_of_guesses = 7
        print ""
        print "New game. Range is 0 to 100."
        print "Number of guesses remaining is", number_of_guesses 
        print ""
        return num_range, number_of_guesses, input_guess
    elif num_range == 1000:
        number_of_guesses = 10
        secret_number = num_range - random.randrange(0, 1000)
        print ""
        print "New game. Range is 0 to 1000."
        print "Number of guesses remaining is", number_of_guesses 
        print ""
        return num_range, number_of_guesses, input_guess
    else:
        return "Error with new game"
    

# define event handlers for control panel
def range100():
    ### resets range to [0, 100) ###
    global num_range, number_of_guesses
    num_range = 100
    return number_of_guesses, num_range, secret_number, new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    ### resets range to [0, 1000) ###
    global num_range, number_of_guesses
    num_range = 1000
    return number_of_guesses, num_range, secret_number, new_game()

def input_guess(guess):
    # main game logic
    ### computes number of guesses remaining ###
    global number_of_guesses
    ### determines if player won game ###
    try:
        player_guess = int(guess)
        number_of_guesses -= 1
        result = player_guess - secret_number
        print "Player guess was", player_guess    
        if result < 0:
            print "Higher!"
            guesses_remaining()
        elif result > 0:
            print "Lower!"
            guesses_remaining()
        elif result == 0:
            print "Correct!"
            print ""
            new_game()
        else:
            print "There was an error with player guess"
    except:
        print "Please enter a number and try again."
        print ""
    
def guesses_remaining():
    ### displays number of guesses remaining ###
    if number_of_guesses > 0:    
        print "Number of guesses remaining is", number_of_guesses
        print ""
    elif number_of_guesses == 0:
        print "You ran out of guesses."
        print "The correct number was", secret_number
        print ""
        new_game()  

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.add_input("Player guess", input_guess, 100)


# call new_game and start frame
new_game()
frame.start()

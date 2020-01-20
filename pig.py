"""My name: Liang Chen
   My PennID: 76922404
   I worked through this homework alone without help."""
def roll():
    """This function returns a random number in the range of 1 to 6, inclusive."""
    import random
    x = random.randint(1,6) # Pick a number from 1 to 6 randomly, including 1 and 6.
    return x # return the random roll number.  
        
def computer_move(computer_score,human_score):
    """This function requires the computer to roll several times, display the result of each roll. The function returns the total points for this turn.
    If computer rolls a number 6, then the score for this turn counts as zero by returning zero point by function, and computer ends this turn.
    If computer's scores are larger than or equal to human's scores, then computer chooses to roll three times, otherwise it chooses to roll five times for a better chance to win"""
    play_times = 0
    global total_computer_score # total_computer_score and total_human_score represent the total scores for computer and human after each turn. And after each turn, these two variables add the last turn's scores. In other words, these two variables are accumulative and can lead to the final results. 
    global total_human_score # make them global variables, total_computer_score and total_human_score.
    if total_computer_score >= total_human_score:
        while play_times < 3: # If current total computer score is larger than or equal to total human score, then computer rolls three times for this turn.
            current_roll = roll()
            print("The current roll number for computer is",current_roll)
            if current_roll == 6: 
                print("This turn ends. The total computer's score for this turn is 0 point(s)")
                return 0  # if at any roll, the roll number is 6, then return zero point to computer_score variable, which means computer score for this turn is zero point, and then directly exit the entire computer_move function.
                break
            computer_score = current_roll + computer_score # The variable computer_score is a local variable. It adds each roll number to itself and only represents the total computer score for a single turn. In other words, it is not accumulative through the whole program. 
            print("The current computer's score is",computer_score,"point(s)")
            play_times += 1
        if current_roll != 6: # If the roll number is 6, then do not exit the computer_move function here. Instead, it should exit above where the condition "if current_roll == 6" lies.
            print("This turn ends. The total computer's score for this turn is",computer_score,"point(s)")
        return computer_score # return the local variable computer_score
    if total_computer_score < total_human_score:
        while play_times < 5: # If current total computer score is smaller than total human score, then computer rolls five times for this turn to show the computer can play aggressively.
            current_roll = roll()
            print("The current roll number for computer is",current_roll)
            if current_roll == 6:
                print("This turn ends. The total computer's score for this turn is 0 point(s)")
                return 0
                break
            computer_score = current_roll + computer_score
            print("The current computer's score is",computer_score,"point(s)")
            play_times += 1
        if current_roll != 6:
            print("This turn ends. The total computer's score for this turn is",computer_score,"point(s)")
        return computer_score

    
def human_move(computer_score,human_score):
    """The function asks the user if he or she wants to roll again, the user must at least roll once. After rolling each time, the current scores will be displayed.
    After each roll, the user is asked if he or she wants to continue to roll. If the user chooses to roll again and doesn't roll a 6,
    then the function adds the roll number to the total scores. If the user chooses to roll again and does roll a 6, the function returns zero point and this turn ends.
    If the user chooses not to roll again, the function returns the total score for this turn and this turn ends."""
    count = 0
    while 1 == 1 :
        answer = ask_yes_or_no("Do you want to roll again? ") # call ask_yes_or_no helper function to see if the player wants to roll a number again.
        if answer == False:
            while count == 0: # This while loop makes sure that the player at least roll once for each turn. The count variable is a suporting variable which can change accordingly. 
                answers = ask_yes_or_no("You must at least roll once. Please enter Yes or No: ")
                if answers == True:
                    answer = True
                    count = 1
            if count != 1:
                break
        if answer == True:
            current_roll = roll()
            print("The current roll number for you is",current_roll)
            if current_roll == 6: 
                print("This turn ends. Your total score for this turn is 0 point(s)")
                return 0  # if roll number is 6, then return zero point.
                break    # if roll number is 6, exit the human_move function.
            human_score = human_score + current_roll # The variable human_score is a local variable. It adds each roll number to itself and only represents the total human score for a single turn. In other words, it is not accumulative through the whole program. 
            print("Your current score is",human_score,"point(s)")
            count += 2
            
    if current_roll != 6: # if roll number is 6, do not exit the function here. Instead, exit above where the if condition "if current_roll == 6" lies.
        print("This turn ends. Your total score for this turn is",human_score,"point(s)")
        
    return human_score
           
def print_instructions():
    """This function tells the user the rules of game."""
    print("  Hello! Welcome to the Pig Game. The rules of the game are followings:")
    print("  Two players are required for this game. Two players take turn. For each turn, a player rolls a six-sided die. The player can roll as many times as he or she wishes. Each time the player rolls the die, the number on the die will count as the player's score.")
    print("  Upon end of each turn, the player will get a total score. However, in each turn, if the player rolls a number 6, the player has to stop and her total score for this turn will be zero. Eventually, whoever reaches or exceeds 50 points wins.")
    print("  According to the rules above, the first player has an advantage. To make the game more fair, if the first player first reaches 50 points or more, the second player gets one additional turn. However, if the second player first gets 50 points or more, the first player does not get an additional turn.")
    print("  If two players are tied with 50 points or more, each gets another turn until the tie is broken.")
    print("  Each player must roll the die at least once. At the player's each turn, the game will display the current score for each player as well as the score difference. If there is ever a tie, the game will tell you. At the end of the game, the final result will be displayed.")
    print("  You play against the computer.")
    print(" ")
    print(" ")
def show_current_status(total_computer_score,total_human_score):
    """This function prints the user's current scores and the computer's current scores. The function also pritnts how far the user is ahead of or behind the computer. The function also detects if there is a tie."""
    print("  ")
    print("After this turn, current computer's score is",total_computer_score,"point(s), current human's score is",total_human_score,"point(s)")
    if total_human_score > total_computer_score: # if the value of total_human_score variable is larger than the value of total_computer_score variable, then print the following.
        print("You are ahead",total_human_score - total_computer_score,"point(s)")
    if total_human_score < total_computer_score: # if the value of total_human_score variable is smaller than the value of total_computer_score variable, then print the following.
        print("The computer is ahead",total_computer_score - total_human_score,"point(s)")
    if total_human_score == total_computer_score: # if the value of total_human_score variable is equal to the value of total_computer_score variable, then print the following.
        print("There is a tie!")
def is_game_over(total_computer_score,total_human_score):
    """This function returns True if either player has 50 or more and the players are not tied, otherwise it returns False."""
    if total_computer_score >= 50 or total_human_score >= 50:
        if total_computer_score != total_human_score:
            return True # if either the value of total_human_score or total_computer_score variable is larger than 50 and the values of the variable are not same, then return True. Otherwise, return False.
        else:
            return False
    else:
        return False
    
def show_final_results(total_computer_score,total_human_score): 
    """This function tells whether the user is won or lost, and prints that the user wins or loses by how many points."""
    if total_computer_score > total_human_score: # if the value of total_human_score variable is smaller than the value of total_computer_score variable, then print the following.
        print("  ")
        print("  ")
        print("The game is over. The computer wins. You lose by",total_computer_score - total_human_score,"point(s)")
    if total_computer_score < total_human_score: # if the value of total_human_score variable is larger than the value of total_computer_score variable, then print the following.
        print("The game is over. You win by",total_human_score - total_computer_score,"point(s)")

def ask_yes_or_no(prompt):
    """This function is a helper function. This function is reused several times. It is used in human_move function. It is called to ask the user if he or she wants to roll again.
    It is also called to remind the user that he or she should at least roll once if the user chooses not to roll at all in his or her turn. The function is also called in the main function
    to ask the user if he or she wants to play this game again after the game is over."""
    result = input(prompt) 
    while result == "": # This line of code is trivial but necessary, if the player accidentally presses the "return" button on the keyboard, then it will keep asking the question. Without this line of code, under the condition of the player accidentally presses the "return" button on the keyboard, the program will go wrong. 
        result = input(prompt)
    if result[0] == "Y" or result[0] == "y": # If the answer begins with Y or y, then return True. 
        return True
    if result[0] == "N" or result[0] == "n": # If the answer begins with N or n, then return False. If the answer does not begin with either one of Y or y or N or n, then the function returns None.
        return False
    

    
def main():
    """This is the main function. The first function the program will run is this main function."""
    while 1 == 1:
        global total_computer_score 
        global total_human_score # Make total_computer_score and total_human_score these two variables global.
        total_computer_score = 0 
        total_human_score = 0 # Set and reset the total_computer_score and total_human_score variables to zero whenever the game starts over again.
        print_instructions()
        while 1 == 1:
            computer_score = 0
            human_score = 0 # Set and reset the computer_score and human_score variables to zero for each turn because they should not be cumulative throughout the program.
            total_computer_score = total_computer_score + computer_move(computer_score,human_score) # Make total_computer_score a cumulative variable. In other words, it should be updated to the current total score after computer's each turn.
            show_current_status(total_computer_score,total_human_score)
            total_human_score = total_human_score + human_move(computer_score,human_score) # Make total_human_score a cumulative variable. In other words, it should be updated to the current total score after player's each turn.
            show_current_status(total_computer_score,total_human_score)
            if is_game_over(total_computer_score,total_human_score) == True: # If the game is over then break the loop and directly go to show final results function.
                break
            if is_game_over(total_computer_score,total_human_score) == False: # If the game is not over, go on to the next turn.
                print(" ")
        show_final_results(total_computer_score,total_human_score)
        play_again = 0
        while 1 == 1:
            play_again = ask_yes_or_no("Do you want to play again?") # After the game is over, ask the player if he or she wants to play again.
            if play_again == True: # If the player wants to play again, then break this loop and re-enter the outer loop and plays again.
                break
            if play_again == False: # If the player does not want to play again, then break the outermost loop of the main function, in other words, break all of the loops, and exit the game.
                print("You have exited the game.") 
                break
        if play_again == False:
            break
if __name__ == "__main__": # The program will first start here and this make sure that the main function is the first function that will be executed.
    main()
    

"""My name: Liang Chen
   My PennID: 76922404
   I worked through this homework alone without help.
   Inputs that lead to win: 1,1,1,1,1,1,1,1,40,1,1,40,1,9,0
   Inputs that lead to loss: 10,10,10,10,10,1,1,1,1,1,1,1,1,1,1,40,0"""
altitude = 100.0 # Give initial values to variables altitude, velocity, fuel and second.
velocity = 0.0
fuel = 100.0
second = 0
playing = True # Assign the Boolean value True to the variable playing.
while playing == True:  # This while loop can function according to player's needs at the end of the game. If player wants to play again, then keep staying inside the loop by assigning true to the variable playing, or else exit the loop by assigning false to the variable playing. This can be shown later.
    while altitude > 0: # This while loop can function as long as the altitude is above zero. When altitude is equal to or below zero after several loops, then exit this while loop.
        if altitude == 100.0: # This part of codes allows players to see the initial values of altitude, velocity and fuel amount every time at the beginning of the game so that they can start to play properly based on these values.
            print('\n')
            print("The current altitude is "+str(round(altitude,2))+" m")
            print("The current velocity is "+str(round(velocity,2))+" m/s")
            print("The current fuel amount is "+str(round(fuel,2))+" liters")
            print('\n')
        number = input("Please sepcify how much fuel you want to burn at this second: ") # This part of code allows players to input the amount of fuel they want to burn every time. Because it is inside the "while altitude == 0" loop, as long as the altitude is above zero, players can input the amount at every round.
        try: # This "try... except" part of codes allows to solve some special cases in which players try "cheating" the game by specifying an illegal amount of fuel to burn. These speical cases aee elaborated as follows.
            number = float(number) # Change the type of variable "number" from string to float.
            if number < 0: # If a negative amount of fuel is burnt, then treat it as if they burnt zero fuel.
                number = 0
            if number > fuel: # If players try to burn more fuel than they have, burn all their fuel.
                number = fuel
            fuel = fuel - number # Update the fuel amount under the special cases and normal cases.
            velocity = velocity + 1.6 - 0.15 * number # Calculate the value of velocity for every time.
            altitude = altitude - velocity # Calculate the value of altitude for every time.
            second = second + 1 # Update the time that is needed for landing. Each round increases one second.
            print("The current altitude is "+str(round(altitude,2))+" m") # Print the values of current altitude, velocity and fuel amount in each round. And round the values to two decimal places.
            print("The current velocity is "+str(round(velocity,2))+" m/s")
            print("The current fuel amount is "+str(round(fuel,2))+" liters")
            print('\n')
        except ValueError: 
            print("Your input is not a number. Please enter again.") # "except ValueError" means that if the input is not a number in this case, which means the type of input cannot be changed into float by the code in the first line under the "try" command, then print "Your input is not a number. Please enter again" and then go back to the "while altitude > 0" command and start again.
    if velocity < 10: # After exiting the "while altitude > 0" loop, if the value of velocity is less than 10m/s, then print "You have a safe landing."
        print("You have a safe landing.")
    else: # If the value of velocity is equal to or greater than 10m/s, then print "You do not have a safe landing."
        print("You do not have a safe landing.")
    print("The final velocity is "+str(round(velocity,2))+" m/s") # Whether players have a safe landing or not, print the final values of velocity, landing seconds and how much fuel left. Round the values of velocity and fuel amount to two decimal places.
    print("There are "+str(round(fuel,2))+" liters left")
    print("The landing takes "+str(second)+" s")
    answer = input("Do you want to play again? ") # Create a variable answer to which a string can be inputed by using the input command. And ask players if they want to play again after the game.
    while answer[0] != "N" and answer[0] != "n" and answer[0] != "Y" and answer[0] != "y": # Find the first character of the string, if this character is not each of the following four characters: Y, y, N, n, then run the codes under this while loop.
        answer = input("Please enter Yes if you want to play again. Or else please enter No. Do you want to play again?") # Ask players if they want to play again. Here a friendly message "Please enter Yes if you want. Or else please enter No." is added in order to allow players to move forward more quickly by following this instruction. However, if players does not exactly follow this instruction, for example, if the players input yes with a lowercase of y, they can still restart the game according to the codes below. 
    if answer[0] == "N" or answer[0] == "n": # If players enter a word with the first letter being n or N, no matter what letters follow it, run the codes under this if statement.
        print('\n')
        print("You have exited the game.")
        playing = False # By assigning false to the variable playing, we exit the "while playing == True" loop which means we finish running all of the codes. The players exit the game.
    else: # This else excludes all of the situations discussed above in the "while" and "if" parts, which means if players enter a word with the first letter being y or Y, no matter what letters follow it, run the codes under this else statement.
        playing = True # Assign Boolean value True to the variable playing to keep staying inside the "while playing == True" loop, which means keep playing the game.
        altitude = 100.0 # Reassign initial values of altitude, velocity, fuel and second.
        velocity = 0.0
        fuel = 100.0
        second = 0

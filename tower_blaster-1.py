# Tower Blaster Game

def setup_bricks():
    """ This function creates a main pile of 60 bricks, represented as a list containing the integers 1 –60. Meanwhile, it creates a discard pile of 0 bricks, represented as an empty list.
        The function returns both of these two lists."""
    main_pile = []
    discard_pile = []
    for x in range(1,61): # Iterate from 1 to 60.
        main_pile.append(x)
    return (main_pile,discard_pile) #Return a main pile list of 1-60 and an empty discard pile list.
def shuffle_bricks(bricks):
    """This function shuffle the given bircks."""
    import random #Import random module.
    random.shuffle(bricks) #Shuffle the given bricks.
def check_bricks(main_pile,discard):
    """This function checks if there are any cards left in the given main pile of bricks. If not, the function shuffles the discard pile and moves these bricks to the main pile.
        Meanwhile, this function turns over the top card to be the start of the new discard pile."""
    if main_pile == []:
        shuffle_bricks(discard) #Shuffle the discard pile if the main pile is empty.
        for i in discard:
            main_pile.append(i)# Copy every element from the shuffled discard pile to the main pile.
        j = len(discard)
        for i in range(j): # Pop every element within the discard pile list.
            discard.pop(0)
        add_brick_to_discard(main_pile[0],discard) # Copy the top of the brick out of the main pile and put it to the discard pile.
        main_pile.pop(0)# Pop the top brick of the main pile.
def check_tower_blaster(tower):
    """This function checks if the bricks in either computer's tower or user's tower are in an ascending tower by returning a boolean value. If the given tower is in an ascending tower,
        the function returns True."""
    ascending_tower = sorted(tower) # Define an ascending tower by sorting the given tower.
    if ascending_tower == tower: # Check if the defined ascending tower is the same as the given tower, if it is the same, then return True.
        return True
def get_top_brick(brick_pile):
    """This function removes and returns the top brick from any given pile of bricks. This given pile of bricks can be the main pile or the discard pile or the computer's tower or the user's tower.
        The function returns an integer."""
    a = brick_pile[0]
    brick_pile.pop(0) # Pop the top brick of the given pile.
    return a # Return the top brick of the given pile before being popped.
def deal_initial_bricks(main_pile):
    """This function deals two sets of ten bricks each from the given main pile, one for initial computer's tower, another for initial user's tower. This function returns a tuple containing two lists"""
    computer_tower = []
    user_tower = []
    i = 0
    while i < 10:# Deal two sets of ten bricks from the main pile to computer's tower and user's tower in turn. When i is equal to 10 or bigger than 10, the while loop ends and the dealing of bricks is done.
        computer_tower.insert(0,get_top_brick(main_pile))
        user_tower.insert(0,get_top_brick(main_pile))
        i = i + 1
    return (computer_tower,user_tower)
def add_brick_to_discard(brick,discard):
    """This function adds the given brick to the top of the given discard pile."""
    discard.insert(0,brick) # insert the given brick to the top of the discard pile.
def find_and_replace(new_brick,brick_to_be_replaced,tower,discard):
    """This function finds the given brick to be replaced in the given tower and replace it with the given new brick, and this replaced brick gets put on top of the given discard pile.
        Meanwhile, this function checks and makes sure that the given brick to be replaced is truly a brick in the given tower. The function returns True if the given brick is replaced,
        ortherwise returns False."""
    for j in tower:#check if the brick to be replaced is in the given tower by iterating over the bricks from the tower.
        if j == brick_to_be_replaced: # if the brick to be replaced is indeed in the given tower, then replace this brick with the new brick and then put the replaced brick onto the top of the discard pile.
            user_index = tower.index(brick_to_be_replaced)
            tower[user_index] = new_brick
            add_brick_to_discard(brick_to_be_replaced,discard)
            return True # If the brick to be replaced is in the given tower, return True.
    return False # If the brick to be replaced is not in the given tower, return False.

def computer_play(tower,main_pile,discard):
    """This function elaborates how the computer is going to play, i.e., the computer's strategy of winning this game. There are some main rules that are explained here. Meanwhile, in some of these main rules,
        there are several additional rules that could increase the possibility for the computer to win the game. These additional rules are explained behind that specific part of codes. The first main rule is that
        the computer each time chooses a brick from the discard pile and replaces a brick by default unless it encounters some conditions. There are some conditions in which the computer instead chooses a brick from main pile
        and replaces a brick or directly puts the brick from the main pile into the discard pile(skips the turn). Those conditions are elaborated later. The second main rule is that when choosing a brick
        (either from the discard pile or the main pile), we compare this chosen brick to each one of the bricks in the given tower in order. If the chosen brick is bigger than the brick from the given tower,
        we skip this given brick and move on to compare with the next brick in the given tower. If the chosen brick is smaller than the brick from the given tower, we keep comparing the chosen brick to the next brick
        in the given tower, if the chosen brick is also smaller than the next one, we substitute the first one with our chosen brick. If the chosen brick is bigger than the next one(under the condition that the chosen brick is smaller
        than the first one), then we choose not to replace the first one with our chosen brick and we move on to the next brick and iterate the process above instead. The third main rule is that we categorize the discard pile into two sets. 
        One set is between 1 and 30(30 inclusive), the other is between 31 and 60(31 inclusive). If any brick from the former five bricks of the given tower is bigger than 30, then we replace this brick with the given brick
        from the first set of the discard pile. If any brick from the latter five bricks of the given tower is smaller than 20, then we replace this brick with the given brick from the second set of the discard pile. The fourth main rule is that
        the second main rule applies to both main pile and the discard pile. There are some important additional rules branching under these main rules that are explained further not here but behind that specific part of the codes below."""
    print("It's computer's turn.")
    if discard[0] == 1: #If the top of the brick from the discard pile is 1, directly put this brick to the first position of the given tower, i.e., the position with an index 0.
        print("The computer picks",discard[0],"from the discard pile")
        print("The computer replaces a brick")
        num = tower[0]
        tower[0] = get_top_brick(discard) # Get the top brick of the discard pile and put it to the first position of the given tower.
        add_brick_to_discard(num,discard) # Put the replaced brick on thr top of the discard pile.
    elif discard[0] == 60: #If the top of the brick from the discard pile is 60, directly put this brick to the last position of the given tower, i.e., the position with an index 9.
        print("The computer picks",discard[0],"from the discard pile")
        print("The computer replaces a brick")
        num = tower[9]
        tower[9] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the last position of the given tower.
        add_brick_to_discard(num,discard)# Put the replaced brick on thr top of the discard pile.
    elif 1 < discard[0] <= 30: # Following the third main rule, the discard pile is categorized into two sets. This is the first set (1-30, 30 inclusive).
        while 1==1:
            if tower[3] == 8 or tower[3] == 9 or tower[3] == 10 or tower[3] == 11:# A trivial additional rule is added here because after lots of running tests, this addtional rule can increase the possibility to win by avoiding the fourth place of the tower to be occupied by a relatively small number.
                print("The computer picks",discard[0],"from the discard pile")
                print("The computer replaces a brick")
                num = tower[3]
                tower[3] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the fourth position of the given tower.
                add_brick_to_discard(num,discard)# Put the replaced brick on thr top of the discard pile.
                break    
            if tower[4] == 9 or tower[4] == 10 or tower[4] == 11 or tower[4] == 12: #A trivial additional rule is added here because after lots of running tests, this addtional rule can increase the possibility to win by avoiding the fifth place of the tower to be occupied by a relatively small number.
                print("The computer picks",discard[0],"from the discard pile")
                print("The computer replaces a brick")
                num = tower[4]
                tower[4] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the fifth position of the given tower.
                add_brick_to_discard(num,discard)# Put the replaced brick on the top of the discard pile.
                break    
            for n in range(1,5):#This additional rule is to make sure that the bricks from the first half of the tower(not including the position with index 0) are not so small that may limit brick numbers like 15 - 30 to occupy the first half of the tower. For example, if a brick with number 3 occupies the fourth place of the tower,there is no way for the computer to win without replacing this brick because there are only two bricks with numbers 1 and 2 can be put in front of brick number 3 in order to win,but there are three places needed to be filled before the fourth place. This additional rule solves this kind of problem.
                num = 0
                if tower[n] < n + 5:
                    print("The computer picks",discard[0],"from the discard pile")
                    print("The computer replaces a brick")
                    num = tower[n]
                    tower[n] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard)# Put the replaced brick on the top of the discard pile.
                    break
            if num != 0:     
                break
            for p in tower[0:5]:# This part belongs to the third main rule in which we replace the bricks from the first half of the tower that are larger than 30 to make sure relatively small numbers to appear in the first half of the tower.
                num = 0
                if p > 30:
                    print("The computer picks",discard[0],"from the discard pile")
                    print("The computer replaces a brick")
                    num = tower[tower.index(p)]
                    tower[tower.index(p)] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard)# Put the replaced brick on the top of the discard pile.
                    break
            if num != 0:
                break
            part_of_strategy(tower,discard,main_pile) # This part leads to a self-created function in which the computer compares each of the bricks from the tower with the chosen brick from either main pile or discard pile and make decisions accordingly followed by the second main rule explained above.
            break
                        
    elif 30 < discard[0] < 60: # Following the third main rule, the discard pile is categorized into two sets. This is the second set (30-60).
        while 1==1:
            for p in tower[5:10]:# This part belongs to the third main rule in which we replace the bricks from the second half of the tower that are smaller than 20 to make sure relatively big numbers to appear in the second half of the tower.
                num = 0
                if p < 20:
                    print("The computer picks",discard[0],"from the discard pile")
                    print("The computer replaces a brick")
                    num = tower[tower.index(p)]
                    tower[tower.index(p)] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard)# Put the replaced brick on the top of the discard pile.
                    break
            if num != 0:
                break
            for n in range(7,10):
                num = 0
                if tower[n] <= 50:#This additional rule is to make sure that the bricks from positions of index 7 to 9 (the last three bricks) are equal to or bigger than 50 in order to make sure there will be very big numbers in the last three bricks.
                    print("The computer picks",discard[0],"from the discard pile")
                    print("The computer replaces a brick")
                    num = tower[n]
                    tower[n] = get_top_brick(discard)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard)# Put the replaced brick on the top of the discard pile.
                    break
            if num != 0:     
                break
            part_of_strategy(tower,discard,main_pile)# This part leads to a self-created function in which the computer compares each of the bricks from the tower with the chosen brick from either main pile or discard pile and make decisions accordingly followed by the second main rule explained above.
            break
             
def part_of_strategy(computer_tower,discard_pile,main_pile):
    """This self-created function belongs to a part of the computer's strategy. This function realizes the second main rule. The second main rule is that when choosing a brick (either from the discard pile or the main pile),
    we compare this chosen brick to each one of the bricks in the given tower in order. If the chosen brick is bigger than the brick from the given tower, we skip this given brick and move on to compare with the next brick in the given tower.
    If the chosen brick is smaller than the brick from the given tower, we keep comparing the chosen brick to the next brick in the given tower, if the chosen brick is also smaller than the next one, we substitute the first one with our chosen brick.
    If the chosen brick is bigger than the next one(under the condition that the chosen brick is smaller than the first one), then we choose not to replace the first one with our chosen brick and we move on to the next brick and iterate the process above instead.
    There are some conditions in which the computer decides to choose a brick from the main file instead of the discard file followed by the first main rule. These conditions are elaborated under this function.
    There are also several additional rules here that are explained below."""
    for p in computer_tower[0:10]:
        if p == 60 and computer_tower.index(p) != 9:#This additional rule makes sure if the brick with number 60 appears in the tower without locating in the last place of the tower, we replace this brick with a discard pile.
            print("The computer picks",discard_pile[0],"from the discard pile")
            print("The computer replaces a brick")
            num = p
            computer_tower[computer_tower.index(p)] = get_top_brick(discard_pile)# Get the top brick of the discard pile and put it to the given position of the given tower.
            add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.
            break
        if p == 1 and computer_tower.index(p) != 0:#This additional rule makes sure if the brick with number 1 appears in the tower without locating in the first place of the tower, we replace this brick with a discard pile.
            print("The computer picks",discard_pile[0],"from the discard pile")
            print("The computer replaces a brick")
            num = p
            computer_tower[computer_tower.index(p)] = get_top_brick(discard_pile)# Get the top brick of the discard pile and put it to the given position of the given tower.
            add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.
            break       
        if discard_pile[0] > p: # This is consistent with the second main rule. 
            if computer_tower.index(p) != 9:
                continue # If top brick from the discard pile is bigger than the brick from the tower, skip and move on to compare the next brick.
            if computer_tower.index(p) == 9:
                go_to_main_pile(computer_tower,discard_pile,main_pile)# If the top brick of the discard pile is bigger than all ten bricks from the tower, then the computer does not choose this brick. Instead, the computer chooses a brick from the main pile by applying this self-created go_to_main_file function.
                break
        if discard_pile[0] < p:# This is consistent with the second main rule. 
            if computer_tower.index(p) == 9:# If top brick from the discard pile is smaller than the last brick of the tower, replace this brick if this brick is not 60, otherwise the computer chooses a brick from the main pile instead by applying go_to_main_file function. 
                num = computer_tower[computer_tower.index(p)]
                if num != 60: 
                    print("The computer picks",discard_pile[0],"from the discard pile")
                    print("The computer replaces a brick")
                    computer_tower[computer_tower.index(p)] = get_top_brick(discard_pile)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.
                    break
                else:
                     go_to_main_pile(computer_tower,discard_pile,main_pile)# The computer chooses a brick from the main pile instead by applying this function. 
            if computer_tower.index(p) != 9:
                if discard_pile[0] > computer_tower[computer_tower.index(p)+1]:#If top brick from the discard pile is smaller than the brick from the tower, but it is bogger than the next brick from the tower, then skip this first brick and keep comparing the chosen brick from the discard pile with the next brick from the tower. 
                    continue
                if discard_pile[0] < computer_tower[computer_tower.index(p)+1]:#If top brick from the discard pile is smaller than the brick from the tower, and it is also smaller than the next brick from the tower, then replace the first brick with the chosen brick from the discard pile.
                    print("The computer picks",discard_pile[0],"from the discard pile")
                    print("The computer replaces a brick")
                    num = computer_tower[computer_tower.index(p)]
                    computer_tower[computer_tower.index(p)] = get_top_brick(discard_pile)# Get the top brick of the discard pile and put it to the given position of the given tower.
                    add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.
                    break
    

    
            
def go_to_main_pile(computer_tower,discard_pile,main_pile):
    """This function is a self-created function. This function is used when the computer decides to choose a brick from the main pile instead of the discard pile. There are two situations realized by this function.
    The first one is choosing a brick from the main pile and replace a brick from the tower with this chosen brick. The second situation is choosing a brick from main pile and directly putting it into the discard pile,
    i.e., the computer chooses to skip the turn. There are also some additional rules shown below."""
    if main_pile[0] == 1:#This is an additional rule. If the top of the brick from the main pile is 1, directly put this brick to the first position of the tower, i.e., the position with an index 0.
        print("The computer picks a brick from the main pile")
        print("The computer replaces a brick")
        num = computer_tower[0]
        computer_tower[0] = get_top_brick(main_pile)# Get the top brick of the main pile and put it to the first position of the given tower.
        add_brick_to_discard(num,discard_pile)   # Put the replaced brick on the top of the discard pile.
    elif main_pile[0] == 60:#This is an additional rule. If the top of the brick from the main pile is 60, directly put this brick to the last position of the tower, i.e., the position with an index 9.
        print("The computer picks a brick from the main pile")
        print("The computer replaces a brick")
        num = computer_tower[9]
        computer_tower[9] = get_top_brick(main_pile)# Get the top brick of the main pile and put it to the last position of the given tower.
        add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.      
    else:
        for q in computer_tower[0:10]:
            if main_pile[0] > q:# This is consistent with the second and the fourth main rule. 
                if computer_tower.index(q) != 9:
                    continue # If top brick from the main pile is bigger than the brick from the tower, skip and move on to compare the next brick.
                if computer_tower.index(q) == 9:
                    print("The computer picks a brick from the main pile")
                    add_brick_to_discard(get_top_brick(main_pile),discard_pile) # If the top brick of the main pile is bigger than all ten bricks from the tower, then computer skips the turn by directly putting the chosen brick from the main pile into the discard pile. 
                    break    
            if main_pile[0] < q:# This is consistent with the second and the fourth main rule. 
                if computer_tower.index(q) == 9:# If top brick from the main pile is smaller than the last brick of the tower, replace this brick if this brick is not 60, otherwise the computer skips the turn by directly putting the chosen brick from the main pile into the discard pile.  
                    num = computer_tower[computer_tower.index(q)]
                    if num != 60:
                        print("The computer picks a brick from the main pile")
                        print("The computer replaces a brick")
                        computer_tower[computer_tower.index(q)] = get_top_brick(main_pile)# Get the top brick of the main pile and put it to the given position of the given tower.
                        add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile.    
                        break
                    else:
                        print("The computer picks a brick from the main pile")
                        add_brick_to_discard(get_top_brick(main_pile),discard_pile) # The computer skips the turn by directly putting the chosen brick from the main pile into the discard pile.  
                        break
                if computer_tower.index(q) != 9:
                    if main_pile[0] > computer_tower[computer_tower.index(q)+1]:#If top brick from the main pile is smaller than the brick from the tower, but it is bogger than the next brick from the tower, then skip this first brick and keep comparing the chosen brick from the main pile with the next brick from the tower. 
                        continue
                    if main_pile[0] < computer_tower[computer_tower.index(q)+1]:#If top brick from the main pile is smaller than the brick from the tower, and it is also smaller than the next brick from the tower, then replace the first brick with the chosen brick from the main pile.
                        print("The computer picks a brick from the main pile")
                        print("The computer replaces a brick")
                        num = computer_tower[computer_tower.index(q)]
                        computer_tower[computer_tower.index(q)] = get_top_brick(main_pile)# Get the top brick of the main pile and put it to the given position of the given tower.
                        add_brick_to_discard(num,discard_pile)# Put the replaced brick on the top of the discard pile. 
                        break
            
def ask_brick_number(prompt):
    """This function makes sure when the user is asked about which brick in the tower he or she wants to replace, the user has to enter an integer."""
    while 1==1:
        result = input(prompt)
        try:
            result1 = int(result)
            return result1
        
        except ValueError:
            print("Your input is not an integer")
        
def main():
    """The program starts here by running the main function. The main function connects other functions and put them together as needed. The main function makes the computer and the user play one by one.
    If either computer or user gets a tower of ascending order which means it gets Tower Blaster, then the game is over. This main function also shows how the user is going to play. All of the user's turns
    are realized in the main function. Meanwhile, all user inputs are shown in this main function as well."""
    main_pile,discard_pile = setup_bricks() # Establish main pile list and discard pile list.
    shuffle_bricks(main_pile) # Shuffle main pile.
    computer_tower,user_tower = deal_initial_bricks(main_pile) # Establish computer's tower and user's tower by dealing bricks from main pile in turn.
    print("The initial tower for the computer is:",computer_tower)
    print("The initial tower for you is:",user_tower)
    add_brick_to_discard(main_pile[0],discard_pile) # Copy the top brick from the main file and put it into the top of the discard pile.
    main_pile.pop(0) # Pop the top brick of the main pile.
    print("The top brick on the discard file is:",discard_pile[0])
    while 1==1:
        computer_play(computer_tower,main_pile,discard_pile) # Computer's turn to play this game.
        if check_tower_blaster(computer_tower) == True:# Check if the computer's tower reaches stablility.
            print("The computer wins!")
            print("The final computer tower is:",computer_tower)
            break
        check_bricks(main_pile,discard_pile)#Check if the main pile is empty and needed to be filled with shuffled bricks from the discard pile.
        print("It's your turn.")
        print("Your tower is:",user_tower)
        print("The top brick on the discard pile is:",discard_pile[0])
        playing_outer = True
        while playing_outer == True:
            answer_pile = input("Do you want to choose bricks from main pile or discard pile? Please enter m for main pile or d for discard pile.") # It's user's turn. Ask if the user wants to choose a brick from the discard pile or the main pile.
            if answer_pile == 'd':
                while 1==1:
                    answer_brick_discard = ask_brick_number("Where do you want to place it? Please enter a brick number from your tower that you want to replace.")# Ask the user which brick is needed to be replaced.
                    new_brick = get_top_brick(discard_pile)
                    if find_and_replace(new_brick,answer_brick_discard,user_tower,discard_pile) == True:
                        break # If the brick number of the user's input is indeed in the given tower, then reuse the find_and_replace function to replace it with a new brick from the discard pile and then break the while loop to end this turn. If the number is not in the tower, ask again.
                    else:
                        add_brick_to_discard(new_brick,discard_pile) # If the brick number of the user's input is not in the given tower, then put the new brick from the discard pile back to the discard pile and re-enter a brick number.
                playing_outer = False
            elif answer_pile == 'm':
                print("The brick number you pick from main pile is",main_pile[0])
                playing_inner = True
                while playing_inner == True:
                    answer_use = input("Do you want to use? Please enter yes if you want to use it or no if you don't.") # Ask the user if the user wants to use the brick from the main pile.
                    if answer_use == 'yes':
                        while 1==1:
                            answer_brick_main = ask_brick_number("Where do you want to place it? Please enter a brick number from your tower that you want to replace.")# If the user wants to use the brick from the main pile, then ask the user which brick is needed to be replaced.
                            new_brick = get_top_brick(main_pile) # Get the top brick of the main pile.
                            if find_and_replace(new_brick,answer_brick_main,user_tower,discard_pile) == True:# # If the brick number of the user's input is indeed in the given tower, then reuse the find_and_replace function to replace it with a new brick from the main pile and then break the while loop to end this turn. If the number is not in the tower, ask again.
                                playing_inner = False
                                break
                            else:
                                add_brick_to_discard(new_brick,main_pile)#If the brick number of the user's input is not in the given tower, then put the new brick from the main pile back to the main pile and re-enter a brick number.
                    elif answer_use == 'no':
                        add_brick_to_discard(get_top_brick(main_pile),discard_pile)# If the user does not want to use this top brick from the main pile, then put this brick directly onto the top of the discard pile and skips this turn.
                        playing_inner = False
                playing_outer = False
        if check_tower_blaster(user_tower) == True:#Check if the user's tower reaches stability.
            print("You win!")
            print("The final computer tower is:",computer_tower)
            break
        check_bricks(main_pile,discard_pile)# Check if thr main pile is empty and needed to be filled with shuffled bricks from the discard pile.
if __name__ == '__main__': # This is the entry point of this program.
    main()

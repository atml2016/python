name = input("Type your name:")

print("Welcome" , name , "to this adventure!")

answer = input (
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
).lower() 

if answer == "left" :
    answer= input("You've come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across the river and were eaten by alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer== "right":
    answer= input("You've come to a bridge. Do you want to cross it or head back?. Type cross to cross and back to head back: ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet the stranger.Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You have won.")
        
        elif answer =="no":
            print("You lose.")
        
        else:
              print("Not a valid option. You lose.")
      


    elif answer == "back":
        print("You go back and lose. ")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
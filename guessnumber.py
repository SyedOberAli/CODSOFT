import random

Target_no = random.randint(1,100)

while True:
    Userchoice = input("Guess the target_no. or Press Q for Quit the game: ")
    if (Userchoice == "Q"):
        break
    
   
    Userchoice = int(Userchoice)

    if (Userchoice == Target_no ):
        print("SUCESSS!! You won the game.")
        break

    elif (Userchoice<1 or Userchoice>100):
        print("Please enter valid integer value between 1 to 100.")

    elif (Userchoice > Target_no):
        print("Your number was too large.Take a smaller guess.")

    else:
        print("Your number was too small.Take a bigger guess.")
        


print("----GAME FINISH!!!----")        

       
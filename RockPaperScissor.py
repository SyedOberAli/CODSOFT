import random

input_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock,Paper,Scissor =")
computer_choice = random.choice(input_list)
print(f"User_Choice = {user_choice},Computer_Choice = {computer_choice}")

if user_choice==computer_choice:
    print("----MATCH DRAW!!Since both user and computer enter same choice.----")

elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper covers rock,so computer wins!")
    else:
        print("Rock break the scissor,so user wins the match!")

elif user_choice=="Paper":
     if computer_choice=="Scissor":
         print("Scissor cuts the paper,so computer wins!")     
     else:
         print("Paper covers the rock,so user wins!")

elif user_choice=="Scissor":
    if computer_choice=="Rock":
        print("Rock break the scissor,so computer wins!")
    else:
        print("Scissor cuts the paper,so user wins!")

else:
    print("Please enter valid input!")            


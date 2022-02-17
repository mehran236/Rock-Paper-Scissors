import random
import pygame

pygame.mixer.init()
crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.play()

print("\t\t\t\t\t\t***ROCK PAPER SCISSOR***\n\t\t\t\t\t\tWelcome to the Game")
print("Game Developed by @MEHRAN AKHTAR")
x = int(input("Press 1 to see instructions & any key to play:"))
if x == 1:
    print("\t\t\t1.Total number of rounds:10\n\t\t\tYou have to choose the following-")
    print("\t\t\t*->R for Rock\tP for Paper\tS for Scissors")

lst = ["R", "P", "S"]
i = 1
user = 0
admin = 0
name = input("Enter the player name: ")
while i < 11:
    print("\t\t\t*Round", i)
    com_choice = random.choice(lst)
    user_choice = input("Input User Choice: ")

    if user_choice == "R" and com_choice == "R":
        print("Round TIE")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "R" and com_choice == "P":
        admin = admin + 1
        print("ADMIN won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "R" and com_choice == "S":
        user = user + 1
        print(name + " won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "P" and com_choice == "R":
        user = user + 1
        print(name + " won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "P" and com_choice == "P":
        print("Round TIE")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "P" and com_choice == "S":
        admin = admin + 1
        print("ADMIN won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "S" and com_choice == "R":
        admin = admin + 1
        print("ADMIN won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "S" and com_choice == "P":
        user = user + 1
        print(name + " won this round")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    elif user_choice == "S" and com_choice == "S":
        print("Round TIE")
        print(name + "_Chose-", user_choice, "Admin_chose-", com_choice)
    else:
        print("You entered wrong choice,so u are terminated from the game")
        break
    print("Admin:", admin, name + " :", user, "\n")
    i = i + 1
print("\t\t\t\t\t\t\t\t**Game Over**")
print("\t\t\t\t\t\t\t\tFinal results")
print(name + ":", user, "Admin:", admin)

if admin > user:
    print("You Lost this game")
elif admin < user:
    print("You won the game series")
else:
    print("Game Tie")

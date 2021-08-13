import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors Game!")
name = input("What should we call you?\n")
print(f"Hi {name}! Let's play.")
while True:
    user_win = 0
    comp_win = 0

    for i in range(1, 4):
        print(f"Round - {i}")
        my_choice = int(input("Enter your choice:\n0.Rock \n1.Paper "
                              "\n2.Scissors\n"))
        if my_choice >= 3 or my_choice < 0:
            print("Invalid choice.")
        else:
            print(f"You have chosen: {options[my_choice]}")

            comp_choice = random.randint(0, 2)
            print(f"I choose: {options[comp_choice]}")

            if my_choice == comp_choice:
                print("It's a tie!")
                user_win += 1
                comp_win += 1
            elif my_choice == 0 and comp_choice == 2:
                print("You win!")
                user_win += 1
            elif comp_choice == 0 and my_choice == 2:
                print("You lose.")
                comp_win += 1
            elif comp_choice > my_choice:
                print("You lose.")
                comp_win += 1
            elif my_choice > comp_choice:
                print("You win!")
                user_win += 1

    if user_win == 0 and comp_win == 0:
        print("You entered three invalid choices. Play again!")
    elif user_win > comp_win:
        print("Final Result: Great! you won the game.")
    elif user_win == comp_win:
        print("Final Result: It's a tie!")
    else:
        print("Final Result: Oopsiee! you lose the game.")

    x = (input("Do you want to play again? Enter yes or no.\n")).lower()
    if x == "yes" or x == "y":
        continue
    else:
        break

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

# Decide how to determine who wins or loses
# how to get the computer to choose a random shape
only_choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0, 2)
print("You chose: \n" + only_choices[user_choice])
print("Computer chose: \n" + only_choices[computer_choice])

if user_choice == computer_choice:
    print("It's a tie!")
else:
    if user_choice == 0:
        # player chooses rock
        if computer_choice == 1:
            print("Paper beats rock. Computer Wins!")
        else:
            print("Rock beats scissors. You Win!")
    elif user_choice == 1:
        # player chooses paper
        if computer_choice == 2:
            print("Scissors beats paper. Computer Wins!")
        else:
            print("Paper beats rock. You Win!")
    else:
        # player uses scissors
        if computer_choice == 0:
            print("Rock beats scissors. Computer Wins!")
        else:
            print("Scissors beats paper. You Win!")




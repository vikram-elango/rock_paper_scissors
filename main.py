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

print("WELCOME TO THE ROCK PAPER SCISSORS GAME")

choice = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

print("You chose:\n")
print(choice[choose])
comp = random.randint(0, 2)

print("Computer chose:\n")
print(choice[comp])


if choice[choose] == rock and choice[comp] == scissors:
    print("ROCK BEATS PAPER, YOU WIN!!!")
elif choice[choose] == scissors and choice[comp] == paper:
    print("SCISSORS BEATS PAPER, YOU WIN!!!")
elif choice[choose] == paper and choice[comp] == rock:
    print("PAPER BEATS ROCK, YOU WIN!!!")
elif choice[choose] == rock and choice[comp] == rock:
    print("IT'S A DRAW, TRY AGAIN!!!")
elif choice[choose] == scissors and choice[comp] == scissors:
    print("IT'S A DRAW, TRY AGAIN!!!")
elif choice[choose] == paper and choice[comp] == paper:
    print("IT'S A DRAW, TRY AGAIN!!!")
else:
    print("YOU LOSE, TRY AGAIN!!!")










"""
project_2.py: Druhý projekt do Engeto Online Python Akademie

author: Zuzana Jurtíková
email: jurtikova.z@gmail.com
discord: susique
"""
import random

line = "-" * 48

# Greetings
print(
    line,
    line,
    "Hi there!",
    "I've generated a random 4 digit number for you.", 
    "Let's play a Bulls and Cows game!",
    line,
    sep = "\n",
)

# Generating a 4 digit number
num_length = 4
secret_num = ""

while len(secret_num) < num_length:
    new_num = str(random.randint(0, 9))
    if new_num not in secret_num and not secret_num.startswith("0"):
        secret_num += new_num

# Secret number
#print(secret_num)

print(
    line,
    "Enter a number:",
    sep="\n"
)

total_attempts = 0

# Player is guessing 
while True:
    print(line)
    players_tip = input(">>> ")

    # Restrictions
    if len(players_tip) != num_length:
        print(f"The number must be {num_length} digits long!")
        continue
    elif not players_tip.isdigit():
        print("Only numbers allowed!")
        continue
    elif len(players_tip) != len(set(players_tip)):
        print("Repeated digits are not allowed!")
        continue
    elif players_tip[0] == "0":
        print("The number mustn't start with 0!")
        continue

# Game logic
    if players_tip == secret_num:
        total_attempts += 1
        if total_attempts <= 3:
            print(
                f"Well done! You've guessed the right number\nin {total_attempts} guesses!",
                line,
                "That's amazing!",
                sep = "\n",
            )
        else:
            print(
                f"Correct! You've guessed the right number\nin {total_attempts} guesses!",
                line,
                sep = "\n",
            )
            if total_attempts >= 6:
                print("That's not so good!")
            else:
                print("That's average!")
        print(
            line,
            line,
            sep="\n",
        )
        break

    else:
        total_attempts += 1
        bulls = 0
        cows = 0
        for n in range(4):
            if players_tip[n] == secret_num[n]:
                bulls += 1

            elif players_tip[n] in secret_num and players_tip[n] != secret_num[n]:
                cows += 1

        if bulls == 1:
            print(f"Bull:  {bulls}")
        else:
            print(f"Bulls: {bulls}")

        if cows == 1:
            print(f"Cow:   {cows}")
        else:
            print(f"Cows:  {cows}")





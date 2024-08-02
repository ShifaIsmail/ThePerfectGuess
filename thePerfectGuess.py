'''
Aim: generate a random number and ask user to guess it
Rules:
1. if a player's guess is more than the actual number display ="Lower number please"
2. if guess is lower than the actual number display = "higher number please"
3. if guess is correct display number of guesses player made to get correct answer
Hint: random module is used
'''

import random
randnum = random.randint(1,100)
# print(randnum)
player = None
guesses = 0

while (player != randnum):
    player = int(input(" your guess = "))
    guesses += 1

    if (player == randnum):
        print("yeeee! that's right!")
    else:
        if(player > randnum):
            print("Nah! that's not it. Guess a number smaller than that")
        else:
            print("Noo! Guess a number greater than that")
        
print(f"You got it right after {guesses} times")

with open("hiscore.txt", "r") as f:
    stri = f.read().strip()
    try:
        hiscore = int(stri)
    except ValueError:
        hiscore = float('inf')

if (guesses < hiscore):
    print("yahoo! your score is new highest")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))






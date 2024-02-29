import random

target = random.randint(1,100)
MAX_TRIES = 10
guess = 1
while  guess <= MAX_TRIES:
    userInput = input("Guess a number or Quit(q): ")
    if userInput == 'q':
        break
    if (int(userInput) == target):
        print("Success : You guessed it right")
    elif (int(userInput) > target):
        print("Wrong, guess little low") 
    else:
        print("Wrong, guess little high")
    guess +=1

if guess > MAX_TRIES:
    print("Out of tries. The target number was:", target)

print("-----GAME OVER-----")
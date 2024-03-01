import random
from random import choice 

# coin = random.choice(["heads","tails"])
# coin = choice(["heads","tails"])
# print(coin)


# number = random.randint(1, 100)
# print(number)

cards = ['Jack','King','Queen']
random.shuffle(cards)
for card in cards:
    print(card)
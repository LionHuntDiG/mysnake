# i=0
# while i < 10:
#     print("the value of i is now {0}".format(i))
#     print("-" * 25)
#     i += 1

# directions = ["north", "east", "south", "west"]
# chose = ""

# while chose not in directions:
#     chose = input("enter the direction to choose: ")
# print("Ahh your good to go in {0} ".format(chose))
import random

guessed = random.randint(1,10)
#print(guessed)  # FIXME         

guess = ""

while guess != guessed:
    guess = int(input("Guess the number: "))
    if guess == 0:
        print("exiting the game")
        break
    if guess == guessed:
        print("you got it")
        break
    if guess > guessed:
        print("please guess lower")
        continue
    else:
        if guess < guessed:
            print("please guess higher ")
            continue
print("Thanks for participating in my game")
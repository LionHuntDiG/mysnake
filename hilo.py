low = 1
high = 10000

print("Hey Py guess the number what i'm thiking in the range of {} and {}".format(low, high))
print(input("press ENTER to start the game: "))

guesses = 1
# while True:
while low != high:
    print("Guess is in the range of {} and {}".format(low,high))
    guess = low + (high - low ) //2
    i = input("My guess is {}, is it correct? or should i guess higher or lower?"
              "enter h for higher, l for lower, if it is correct enter c: ".format(guess).casefold())
    if i == "h":
        low = guess + 1
    elif i == "l":
        high = guess -1 
    elif i == "c":
        print("i got your number {} in {} guesses".format(guess,guesses))
        break
    else:        
        print("enter h or l or c")
    guesses = guesses + 1
else:
    print("Thought is correct at last: {}".format(low))
    print("i got it in {} guesses".format(guesses))
    
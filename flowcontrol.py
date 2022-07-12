# name = input("Enter the your name: ")
# age =  int(input("Enter your age: "))

# print(f"Hi {name}, we will validate your age:{age} for vote")
# if age < 18:
#     print(f"Hi {name}, your age:{age} is not valid to vote")
#     print("please come back for registering the vote ID in: {0}".format(18-age) )
# else:
#     print(f"Welcome to vote {name}, your age: {age} is valid to vote "

answer = 5
guess = int(input())

if guess == answer:
   print("you have guessed it for the 1st time")
else:
    if  guess > answer:   
     print("please guess lower")
     guess = int(input())
     if guess < answer:
         print ("guess higher, this is second chance")
         guess = int(input())
         if guess == answer:
             print ("you have made it")
         else:
          print("guess correctly in next attempt closing attempts")
     else:
         print("invalid as per suggestion: {0}is not valid".format(guess))        
    else:
     print("guess again")     
     guess = int(input())   
     if guess == answer:
      print("guessed correctly")
     else:
        print("guess again")
        guess = int(input())
        if guess != answer:
            print("please come back next time5 ")
        else:
            print("AAHH you made it")
# answer = 5
# guess = int(input())
# if guess == answer:
#     print(" guess correct")
#     if guess < answer:
#         print("guess again")
#         guess = int(input())
#     elif guess != answer:
#      print("guess correctly")
#     elif guess > answer:
#      print("guess lower")
#     elif guess < answer:
#      print("guess higher")
# else:
#     guess = int(input())
#     if guess == answer:
#      print(" guess correct")
#     elif guess != answer:
#         print("guess correctly")
#     elif guess > answer:
#         print("guess lower")
#     elif guess < answer:
#         print("guess higher")
    
    
    
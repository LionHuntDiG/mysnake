options = ["1: eat", "2: bed", "3: learn", "4: play", "0: exit"]
print("Choose any of the following options: ")
for i in options:
    print(i)
select = ""
while True:
    select = input("enter one of the options: ")
    if select == "0":
        print("exiting from the game")
        break
    if select in  "1":
        print("you have selected: {}, which is eat".format(select))
        
    elif select in  "2":
        print("you have selected: {}, which is bed".format(select))
    elif select in  "3":
        print("you have selected: {}, which is learn".format(select))
    elif select in  "4":
        print("you have selected: {}, which is exit".format(select))
        # print("selected choice is: {}".format(options.find(select))) #FIXME
    # elif select in  "5":
    #     print("you have selected: {}".format(select))
    #     print("you have selected: exit")
    else:
        print("select from the below options only: ")
        for i in options:
         print(i)
         
        
        
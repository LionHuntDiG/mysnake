day = input("enter the day: ")
temparature = int(input("enter the day's temparature in celcius: "))
raining = bool(input("enter Raining: True or False: "))

if (day == "saturday" and temparature >= 27) and not raining:
    print("Go for cricket")
else:
    print("learn coding bro") 

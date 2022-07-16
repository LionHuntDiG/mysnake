age = int(input("How old are you? : "))

if age in range(16,65):
    print("Good day at work")
else:
    print("enjoy your free time")

if age not in range(16,65):
    print("enjoy your free time")
else:
    print("good day at work")
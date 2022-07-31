computer_parts = ["computer", "mouse", "keyboard"]
my_list = []
computer_parts_index = []
for i in range(1,len(computer_parts) + 1):
    computer_parts_index.append(str(i))
print(computer_parts_index)
cart = "-"
while cart != "0":
    if cart in computer_parts_index:
        
        pindex = int(cart) - 1
        pname = computer_parts[pindex]
        if pname in my_list:
            print("removed {} to the list".format(cart))
            my_list.remove(pname)
        else:
          print("added {} to the list".format(cart))
          my_list.append(pname)
        print("your list now contains {}".format(my_list)) 
    
    else: 
        print("select the parts from the below list")
        for number, part in enumerate(computer_parts):
         print("{}: {}".format(number+1, part))
    cart = input("choose: ")
print(my_list)









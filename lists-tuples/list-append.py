available_list = ["computer", "keyboard", "mouse", "monitor", "mat", "headphones", "calci"]
computer_list = []
valid_choices = []
for i in range(1, len(available_list) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
while current_choice != "0":
    if current_choice in valid_choices:
        print("Added {} to the list".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_list[index]
        computer_list.append(chosen_part)
              
        # if current_choice == "1":
        #     computer_list.append("computer")
        # elif current_choice == "2":
        #     computer_list.append("keyboard")
        # elif current_choice == "3":
        #     computer_list.append("mouse")
        # elif current_choice == "4":
        #     computer_list.append("monitor")
        # elif current_choice == "5":
        #     computer_list.append("mat")
        # elif current_choice == "6":
        #     computer_list.append("headphones")
        # elif current_choice == "7":
        #     computer_list.append("calci")
        
    else:
        print("Select the following parts: ")
        for i, part in enumerate(available_list):
            print("{} : {}".format(i+1, part ))
            
        # print("1: computer")
        # print("2: keyboard")
        # print("3: mouse")
        # print("4: monitor")
        # print("5: mat")
        # print("6: headphones")
    current_choice =  input(" choose: ")
print("Thanks for shopping: ")    
print("your cart is: {}".format(computer_list))
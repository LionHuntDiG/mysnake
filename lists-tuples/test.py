# For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
# The user input is of the form: a,b,c, where a, b and c are numbers.
# Your program should calculate and display the result of the calculation:
# a + b - c
# Examples:
# 1. > Please enter three numbers: 10,11,10
#    11
# 2. > Please enter three numbers: 7,5,-1
#    13




# values = input("please enter three values: ")
# my_list=[]
# values_int = values.split(",")
# print(values_int)
# for i in values_int:
#     my_list.append(int(i))
# print(my_list)
# a,b,c = my_list   #TODO
# result = a+b+c   
# print(result)
    


user_list=input("Enter the three values separated by ,  : ")

list_spliting = user_list.split(",")

my_list=[]
for i in list_spliting:
    my_list.append(int(i))
print(my_list)

a,b,c = my_list
result = a+b+c
print(result)
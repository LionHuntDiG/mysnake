new_line = "*" * 181

Age = 29
print( "The age of shanmukha is {0}". format(28) ) 
print(new_line)

my_age="29"
print("The age of shanmukha is: " + my_age)

print(new_line)
print("The number of days in each month are as follows: Jan:{2},Feb:{0},Mar:{2},Apr:{1},May:{2},june:{1},July:{2},Aug:{2}".format(28,30,31))

print(new_line)
print('''The number of days are as follow: 
                                          Feb:{0}
                                          Jan:{2}
                                          Mar:{2}
                                          Apr:{1}
                                          May:{2}
                                          june:{1}
                                          July:{2}
                                          Aug:{2}".format(28,30,31''')

print("                                           /|" )
print("                                          / |" )
print("                                         /  |" )
print("                                        /   |" )
print("                                       /    |" )
print("                                      /     |" )
print("                                     /      |" )
print("                                    /_______|" )



print(new_line)
value=(input(f"Enter the value to find its square and its cube:  "))
my_int=int(value)
#for i in my_int:  # we cannot iterate on single integer value
print("The square of {0} is {1} and its cube is {2}".format(my_int, my_int**2, my_int**3))
    
print(new_line)

for i in range(1,25):
    print("The squared vaule of {0:<4} is {1:<4} and its cube is {2:<4}".format(i,i**2,i**3))
    
first_name = "John"
last_name = "Cleese"
age = 78
 
print(first_name + last_name + f"{age}")
    

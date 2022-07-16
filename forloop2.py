dummy = "a7;b8;9'/c8[l1]df[g]h]1'3,4/5/6"
number = ""
for i in dummy:
    if not i.isu():
        number = number + i 
print(number)
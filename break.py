shopping_list = ["eggs","milk","rice","bread","fish","veggies"]

need_to_found = "fish"
found_it = None

# for i in range(len(shopping_list)):
#     if shopping_list[i] == need_to_found:   #if true, it will take that i value and assign to found_it and break the loop and go to out of loop
#         found_it = i
#         break

if need_to_found in shopping_list:
    found_it = shopping_list.index(need_to_found)
if found_it != None:
    print("item found at position {0}".format(found_it))
else:    
  print("{0} item not found ".format(need_to_found))

# for i in shopping_list:
#     if i == "fish":
#      found = i
#      break
# print("item has been found: {0}".format(found))
shopping_list = ["eggs","milk","rice","bread","fish","veggies"]

need_to_found = "fish"
#found_it = None

for i in range(len(shopping_list)):
    if shopping_list[i] == need_to_found:   #if true, it will take that i value and assign to found_it and break the loop and go to out of loop
        found_it = i
        break
print("item found at {0}".format(found_it))

# for i in shopping_list:
#     if i == "fish":
#      found = i
#      break
# print("item has been found: {0}".format(found))
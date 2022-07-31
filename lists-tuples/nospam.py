from operator import index


menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         for item in meal:
#             print(item.center(23))
#     else:
#         print("the count if spam is {} in {}".format(meal, meal.count("spam")))

for meal in menu:
    # if "spam" in meal:
        # print(meal)
    # for index, value in enumerate(meal): #FIXME
        #1             [egg, beacon] ie len(meal)=2 so range(2-1, -1, -1) so first start at beacon ie is index1  and end at egg ie at index 0 bcz -1 is stop so  this will be stop at egg so at index 0
    for index in range(len(meal) - 1, -1, -1):  #TODO
            if meal[index] == "spam":
              del meal[index]
    print(meal)
            
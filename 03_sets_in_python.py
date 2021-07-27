# set is a collection of non-repeated elements
# similar as dictionay but without keys and does not allow repeated values
# can not use same values and can not access with index number
a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5}
print(a)
print(type(a))
# a.add([1,2,3]) # can not add list in a set
a.add((1, 2, 3))  # touple can be added to a set
print(a)

# ********************************************************************************************
# a.add({1, 2, 3, 4}) # is not allowed
# print(a)
# a.add({"name": "Ali"})  # is not allowed
# print(a)
# *****************************************************************************************

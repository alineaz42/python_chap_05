

# empty set
# a = set()
# print(type(a))

# adding values to set
# a.add(1)
# a.add(1)  # wont add same values
# a.add(1)  # wont add same values
# a.add(1)  # wont add same values
# a.add(1)  # wont add same values
# print(a)


# ******************************************************
# # a.add({1, 2, 3, 4}) # is not allowed
# print(a)
# a.add({"name": "Ali"})  # is not allowed
# print(a)
# *********************************************************
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(type(b))
# lenth of a set
# print(len(b))
# b.add(11)
# print(b)
# remove
# b.remove(5)
# print(b)
# b.remove(12)  # not possible cz 12 not availabe in b
# if any value not availabe in a set will throw an error
# print(b)


# pop
# b.pop()
# print(b)


# clear
# b.clear()

a = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union
print(a)
print(b)
c = a.union(b)
print(c)
# intersection
d = a.intersection(b)
print(d)

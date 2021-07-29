# _____________________________________video:4:19_____________________________________


# values inside a list touple can not be changed
# s = {1, 2, 3, 4, 5, 6, [1, 2, 3, 4, 5]}  # list is unhashable
# print(s)

s = {1, 2, 3, 4, 5, 6, (1, 2, 3, 4, 5)}  # list is unhashable
# print(s)
# print(s.add(5))
s.add(10)
print(s)

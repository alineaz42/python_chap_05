# what will be the length of following set s?
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")?????

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))  # ans will be 2 cz python evaluates 20 & 20.0 same
s2 = {20, 20.1, "20"}
print(len(s2))

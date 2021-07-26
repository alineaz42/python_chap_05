# like a JSON in jscript

myDict = {
    "Fast": "IN a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 3],
    "Age": 24,
    "Status": True
}
print(myDict["Fast"])
print(myDict["Harry"])
print(myDict["Marks"])
print(myDict["Age"])
print(type(myDict["Status"]))
print(type(myDict["Fast"]))


# mutalbe values can be changed
myDict["Marks"] = [4, 5, 8, 7]
print(myDict["Marks"])
print(type(myDict))

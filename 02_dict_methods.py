# ______________keys can also be written in lowercase ________________
myDict = {
    "fast": "IN a Quick Manner",
    "neaz": "A Coder",
    "marks": [1, 2, 3],
    "age": 24,
    "status": True,
    "address": {  # nested dictionay
        "vill": "kandail",
        "thana": "ashulia",
        "upozila": "savar",
        "district": "Dhaka"
    }
}
print(myDict["address"].values())
# _______________________________methods_______________________________
# keys
print(myDict.keys())  # prints the keys of a dictionay
print(type(myDict.keys()))
# converting to list
print(list(myDict.keys()))
# printing the values
print(myDict.values())
print(list(myDict.values()))  # listing the values


# item
print(myDict.items())  # returns a touple inside a list [keys and values]
# update  updates the dict by adding key-values from updating
# print(myDict)
upDateDict = {
    "lovis": "friendly",
    "favourite": "to every One"
}
myDict.update(upDateDict)
print(myDict["address"].values())
print(myDict["address"].keys())

# getting the values using key
# .get() method won't throw any error if the key does not exist will print "None"
print(myDict.get("address"))
print(myDict["village"])  # will throw error if the key does not exist


# ________________ search for more dictionay methods _________________

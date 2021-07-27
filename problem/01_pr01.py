''' 
write a program to crea a dictionay of english words with
values as their bangla meaning
provide user an option  to look it up
'''
myDict = {
    "pakha": "fan",
    "bakso": "box",
    "lekha": "write",
    "ekta": "a"
}
print("Options are right now ", myDict.keys())
a = input("Enter the bangla word \n")
# will through an error if key is not present in dictionay
# print("The meaning of your word is: ", myDict[a])
print("the meaning of your word is ", myDict.get(a))

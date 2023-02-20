#!/usr/bin/env python3

myFavouriteFruits = ["banana","apple","mango","avocado"]
for fruit in myFavouriteFruits: 
    print(len(myFavouriteFruits))
    friends=["phoebe","Anita","Chandler","Monica"]
    print(friends)
    friends[0] = "Mary"
    print(friends)

    new_friends = friends.copy()
    print(new_friends)

new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)

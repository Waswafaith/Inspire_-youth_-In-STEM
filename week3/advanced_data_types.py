#advanced data types
#mutable vs immutable
#mutable are data types that can change during the life cycle of the program i.e you can add or change them
#immutable are data types that cannnot be edited during the life cycle of the program

#1) lists (mutable)
#2) lists (immutable)
#3) dictionaries aka dict
#4) sets

friends=["Anita", "Mark","John","Joy"]
#or []for an empty list
#add elements to the list ------> append(), extend()

students= ["Marie","Kigen","Serphine"]

friends.extend(students)
print(friends)

friends.append("James")
print(friends)

friends.sort()
print(friends)

#Tuples------>types of lists that are not editable
stationaries= ("pens","ink","eraser","pencil")

for stationary in stationaries:
    print(stationary)

numbers= (1,2,3,4,5,6,7,8,9,76,89)

#3) Dictionaries aka dict

#uses key and value pair

student = {"name":"Faith","age":"17","gender":"female","is_tall":True}
#"name":"Faith"---> name(key) Faith(value)

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])
print(student.values())
print(student.keys())

friend = {"fav_colour":"burgundy","hobby":"dancing","course":"nursing","weight":"45","height":"6"}
print(friend["fav_colour"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])
#sets---->a collection of items used to store items in curly brackets
my_fruits={"apple","banana","mango","pinneaple"}
print(my_fruits)

for fruit in my_fruits:
    print(fruit)

print(type(my_fruits))
print(len(my_fruits))
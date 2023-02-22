#create an empty list of favourite musicians
favourite_musicians = []
#using for loop add five new musicians
#copy the list in a new list 
#sort the list
#pop out two celebs
#count the remaining celebs in the list
favourite_musicians = ("Dontoliver","SZA","Rihanna","Tems","Khalid")
for musician in favourite_musicians:
    print(len(favourite_musicians))

    musicians= ["Dontoliver","SZA","Rihanna","Tems","Khalid"]
    print(musicians)

musicians.copy()
print(musicians)
musicians.pop()
print(musicians)
musicians.pop()
print(musicians)
musicians = favourite_musicians

print(favourite_musicians.count())
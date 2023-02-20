age=24
gender="male"

if(age<18):
    print("you are still young")
    
else:
    print("you should get an ID")

#compond / multiple conditions

if((age>30) & (gender == "male")):
    print("you qualify for a loan")
else:
    print("no loan for you")

fav_colour="gray"
age=22
if(fav_colour=="gray")|(age<=20):
    print("happy birthday to you")
else:
    print("No birthday present for you")
    
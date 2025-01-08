#list --> 
fruits = ["apple" , "banana " , "cherry"]
print(fruits)

#create a list with names of 3 of your best friends 

best_friends = ["William" , "Samuel" , "Jackson"]
print(best_friends)

#dictionary --> key : value 

fruits_colors = {
    "apple" : "red" , 
    "banana" : "yellow" , 
    "cherry" : "darkred"
}

print(fruits_colors)

name_age = {
    "William" : "10",
    "Sam" : "10",
    "Jackson" : "11"
}
print(name_age)

# Accesing values
myage = name_age["Jackson"]
print(myage)

name_age["Sam"] = 11
print(name_age)

name_age["Seb"] = 10
print(name_age)

del name_age["Jackson"]
print(name_age)

if "Florence" in name_age:
    print("Florence is in the dictionary")
else:
    print("FLorence isn't in the dictionary")
# Odd or Even number
#user picks numbers and also picks a mathematical operation to be carried out, this displays the number and tells them if it odd or even.
#import tkinter as tk
#window = tk.Tk()
#window.geometry('600x600')
#num1 = int(input("Input a number: "))
#num2 = int(input("Input another number: "))





#window.mainloop()

# #list work
# list = [10,-5,125,600,-133]
# list.sort()
# print(list)

# list.sort(reverse = True)
# print(list)

# thislist = ["orange", "Banana", "plutonium", "Lettuce"]
# #order list above by case sensitive (lower to upper case)
# thislist.sort(key = str.lower)
# print(thislist)


# #list reversed after being ordered from lowercase to uppercase
# thislist.reverse()
# print(thislist)

# #copying list
# mylist = thislist.copy()
# print(mylist)







# Exceptions
# try: # generates an exception (error)
#     print(x)
# except NameError:
#     print("The X variable has not been defined")
# else:
#     print("Nothing went wrong")

# # guaranteed running even if error arises
# finally:
#     print("Regardless of an error being raised, i WILL run.")


# try:
#     o = open("demotext.txt")
#     try:
#         o.write("I love life")
#     except:
#         print("Something went wrong writing to the file")
#     finally:
#         o.close()

# except:
#     ("something went wrong opening the file")

# value error
# x = input("Enter a number greater than 0: ")

# try:
#     value = int(x)
#     print("The input is an integer number")

# except ValueError:
#     try:   
#         value = float(x)
#         print(f"{x} is a floating number")
#     except ValueError:
#         print("the input is not a number!")


# type error      0         1        "2"        3 
# geeky_list = ["sigma1", "sigma2", "sigma3", "sigma4"]
# indices = [0, 1, "2", 3]
# for i in range(len(indices)):
# 	try:
# 		print(geeky_list[indices[i]])
# 	except TypeError:
# 		print("TypeError: Check list of indices")




# # SETS
# #               they do NOT allow duplicates / and 1 and True are considered duplicates (BOTH ON) (same as False and 0)
# fruitlist = ["apple","banana","apple","strawberry","blueberry", True, 1, False, 0]
# fruitset = set((fruitlist))
# fruitset2 = {"mango", "apple", "terracotta", "idk"}
# fruitset.add("mango")
# fruitset.remove("strawberry")
# print(fruitset) # RANDOM ORDER EVERY TIME ^
# print(len(fruitset))

# #prints EVERYTHING venn diagram (obviously apart from duplicates)
# Union = fruitset | fruitset2
# print(Union)
# print("\n")

# # prints what is in FIRST set that isnt in the other!
# SetUniqueness = fruitset - fruitset2
# print(SetUniqueness)
# print("\n")

# # prints what is in BOTH venn diagrams (mango and apple in this case))
# Intersection = fruitset & fruitset2
# print(Intersection)
# print("\n")

# # prints everything OUTSIDE of the intersection (independent venn diagrams)
# Independencies = fruitset ^ fruitset2
# print(Independencies)
# print("\n")

# if "apple" in fruitset:
#     print("apple in set, but idk what index lol")

# for i in fruitset:
#     print(i)

# # adding set to another
# combination = fruitset.update(fruitset2)
# print(combination)


## DICTIONARIES / HASHMAPS
# {key:value} pairs


RLEXP = {"Octane":"Best Car",
         "Fennec":"Also Best Car",
         "Scarab":"Funny egg car",
         "Ripper":"only the wheels are cool"}

# print(dir(RLEXP)) # lists every feasible command in dictionaries

a = RLEXP.get("Octane") # * .get * used to retrieve a value of a key (that is entered inside the brackets as an arguement)
print(a)

b = RLEXP.get("Venom")
print(b)
# this prints 'None' as this is not defined as a key in the dictionary

if RLEXP.get("Fennec"):
    print("That car exists")
else:
    print("that car dont exist gng")

# adding new key/values to the dictionary
RLEXP.update({"Grog":"Ugly ahh car"})
print(RLEXP)
print("\n")

RLEXP.update({"Fennec":"stupid french car"})
print(RLEXP)
print("\n")

# removing key/values from the dictionary
RLEXP.pop("Ripper")   # no need for {} braces here
print(RLEXP)
print("\n")

# removing most recently added key/value
RLEXP.popitem()
print(RLEXP)
print("\n")

# clear/ delete everything in a dictionary
######## RLEXP.clear()

# return ALL KEYS from a dictionary (no values)
keys = RLEXP.keys()
print(keys)
print("\n")

# return ALL VALUES from a dictionary (no values)
values = RLEXP.values()
print(values)
print("\n")

# items returns the key/values, but represented in a 2D list
items = RLEXP.items()
print(items)
print("\n")

for k , v in RLEXP.items():
    print(f"{k}: {v}")
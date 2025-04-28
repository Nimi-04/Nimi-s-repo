#print("Hello, Python!")

#Python comments: Documentation, debugging, readability
# Comments
"""
"This is "
"a multiline comments in"
"python programming"
"""
# import random
# #Python Variables
# fessnum = 1
# secnum = 2
# thirdnum = 5
# print(fessnum + thirdnum)
# print(secnum * thirdnum)
# print(type(secnum))

# # Name = "Nimi"
# # print("My name is " + Name )

# check = False

# if check:
#     #print(Name)
#     pass


# #Casting
# num1 = 2
# num2 = "3"
# print(num1 + int(num2))

# num3 = 4
# print(float(num3))

# print(type(num1))
# print(type(str(num1)))

# Name1 = "Tomi"
# Name2 = 'Aisha'

# ###Case-Sensitivity of variables
# name = "John"
# name = "Akim"

# print(name)

# ###Naming Python Variables
# """Rules for descriptive variable names:
# 1. Must start with a letter or underscore
# 2. Cannot start with a number
# 3. Can only contain alpha-numeric (A-z, 0-9, and _)
# 4. Are case sensitive
# 5. Cannot be any python keywords
# """

# ##### Multi-Word Variable Names
# """
# 1. Camel-case
# 2. Snake-case
# 3. Pascal-case
# """
# #1. Camel-casing
# mySchool = "Babcock"
# myFirstName = "Aisha"

# #2. Snake-casing 
# my_school = "Babcock"
# my_first_name = "Olamide"

# #3. Pascal-casing
# MySchool = "Babcock"
# MyFirstName = "Tomi"

# """
# Assignment
# 1. Write a python statement that will output "Tomi will pay $550 at a
# discount of $50 when he buys a pack of milk at a gocery store. Use
# the following variables:
#         Nmae = "Tomi"
#         Price = "600"
#         Discount = 50
# 2. Write a simple python statement that processes the output in question 1
# only if the variable 
#             isAvailable = True
# """

# Name = "Tomi"
# Price = "600" 
# Discount = 50
# final_price = int(Price) - Discount
# print(Name + " will pay $" + str(final_price) + " at a discount of $" + str(Discount) + " when he buys a pack of milk at a grocery store.")


# isAvailable = False
# if isAvailable:
#     final_price = int(Price) - Discount
#     print(Name + " will pay $" + str(final_price) + " at a discount of $" + str(Discount) + " when he buys a pack of milk at a grocery store.")


# #Assigning many values to many variables
# fruit1, fruit2, fruit3 = "orange", "mango", "cherry"
# print(fruit1)
# print(fruit2)
# print(fruit3)

# ##Assign one value to many variables
# fruit4 = fruit5 = fruit6 = "apple"
# print(fruit4)
# print(fruit5)
# print(fruit6)

# #Unpacking a collection
# fruits = ["orange", "apple", "mango", "guava"]
# print(fruits)
# fruit1, fruit2, fruit3, fruit4 = fruits
# print(fruit2)

# #Global & Local Variables

# def myName():
#     global Name
#     Name = "Nimi"
#     print("My name is " + Name)

# myName()
# print("Her name is " + Name)

# #PYTHON NUMBERS
# """
# Three types of number:
# >> int
# >> float
# >> complex
# """

# num1 = 4
# print(type(num2))

# num2 = 2.5
# print(type(num2))

# num3 = 2j
# print(type(num3))

# num4 = 2 + 5j
# print(type(num4))

# ##Convert between numbers

# num1_compl = complex(num1)
# print(num1_compl)

# num1_float = float(num1)
# print(num1_float)

# num2_int = int(num2)
# print(num2_int)

# ###Random Numbers
# print(random.randrange(1,10))


# """
# Assignment
# 1. Create a little game where your players will guess a specific random numbers, if it matches your number, 
# output "You won!" else output "You lose!"
# Hint: Use the variables:
# randomNumber
# your Guess = input("Guess the number:)

# 2. Refine the code below to work appropriately:

# text = "We are students of python programming at Tedprime"

# hub = input("Enter a name of a hub to search from the text: )

# if hub in text:
#     print("They are the best!")
# else:
#     print("They are also good")
# """



# ##PYTHON STRINGS

# greeting = 'hello'
# print(type(greeting))

# print("It's a ball")
# bio = '''I am nimi born in ........'''

# print(bio)

# ##Strings are arrays
# name = "John"
# print(name[1])

# print(name)

# for letters in name:
#     print(letters)

# print(len("hippopotamus"))

# text = "We are students of python programming at Tedprime"

# # print("Tedprime" not in text)
# # hub = input("Enter a name of a hub to search from the text")
# # if "Tedprime" in text:
# #     print("They are the best!")
# # else:
# #     print("They are also good")



# randomNumber = random.randint(1, 10)

# yourGuess = int(input("Guess the number (between 1 and 10): "))

# if yourGuess == randomNumber:
#     print("You won!")
# else:
#     print("You lose! The correct number was", randomNumber)



# text = "We are students of python programming at Tedprime"

# hub = input("Enter a name of a hub to search from the text:")

# if hub.upper() in text.upper():
#     print("They are the best!")
# else:
#     print("They are also good")


# """
# Assignment
# 1. Use the python input statement to ask for user ages and compare with age=18. If the user is less than 18, 
# output "You are not an adult", else if the user's age is more than 18, output "You are an adult."

# 2. Use python input statement to ask for user's best fruits 
# from the collection:
# fruits = ["mango", "orange". "apple", "banana"]
# If the user's best fruit is present in the fruit collection, output 
# "We have your fruits in stock". But if the fruit is not in collection, 
# output " We don't have your fruit in stock".
# Hint: Use input statement, membership operator, string modify methods, etc
# """



# age = int(input("Please enter your age: "))

# if age < 18:
#     print("You are not an adult.")
# else:
#     print("You are an adult.")



# fruits = ["mango", "orange", "apple", "banana"]

# user_fruit = input("Please enter your favorite fruit: ").strip().lower()

# if user_fruit in (fruit.lower() for fruit in fruits):
#     print("We have your fruit in stock.")
# else:
#     print("We don't have your fruit in stock.")





# thislist = {
#     "Fan" : "OX",
#     "Class" : "Web dev",
#     "Student" : 4
# }

# print(thislist["Class"])


# """
# Assignment
# 1. create a dictionary of a car and it's specification, getting user car name input loop through your dictionary
# if user car name is found, display car specification else if car is not found output car is currently not
# available

# 2. Getting 10 user input store in a list and output the list when you get the entire input
# """


# cars = {
#     "Toyota Corolla": {"Engine": "1.8L 4-cylinder", "Transmission": "CVT", "Fuel Economy": "30/38 mpg"},
#     "Honda Civic": {"Engine": "2.0L 4-cylinder", "Transmission": "Manual", "Fuel Economy": "29/37 mpg"},
#     "Ford Mustang": {"Engine": "5.0L V8", "Transmission": "Manual", "Fuel Economy": "15/24 mpg"},
#     "Tesla Model 3": {"Engine": "Electric", "Transmission": "Single-speed", "Range": "358 miles"},
# }


# user_input = input("Enter the car name to get its specifications (or type 'exit' to quit): ")

# if user_input.lower() == "exit":
#     print("Exiting the program. Goodbye!")

# elif user_input in cars:
#     print(f"Specifications for {user_input}:")
#     for spec, value in cars[user_input].items():
#         print(f"- {spec}: {value}")
# else:
#     print(f"The car '{user_input}' is currently not available.")



# user_inputs = []


# for i in range(10):
#     user_input = input(f"Enter input {i + 1}: ")
#     user_inputs.append(user_input)

# print("Here are the inputs you provided:")
# print(user_inputs)


# #Python Lists
# ages = [11, 15, 7, 23, 53, 11, 111, 23]
# print(ages)
# ages.insert(5, 60)
# print(ages)

# ages.append(80)
# print(ages)

# #Tuple
# names = ("Aisha", "Olamide", "Praise")
# print(names[1])
# names[1] = "Chris"
# print(type(names))
# names_conv_list = list(names) #converting the tuple to a variable
# print(type(names_conv_list))
# print(names_conv_list)
# names_conv_list[1] = "Chris"  #Changing the item to a nw item
# print(names_conv_list)
# names = tuple(names_conv_list)  #Converting the list back to a tuple
# print(names)

# nums = (2,4,56,8,10,12,12)
# print(nums)

# #Set
# colors = {"blue", "black", "purple"}
# print(colors)

# #Dictionary
# person = {
#     "name" : "Tomi",
#     "age" : 20,
#     "age" : 21,
#     "fav_color" : "green" 
# }
# print(person["age"])


# ##Nested dictionary: Means a dictionary inside another dictionary

# person1 = {
#     "name": "Aisha",
#     "age": 12,
#     "fav_color": "blue"
# }
# person2 = {
#     "name": "Praise",
#     "age": 13,
#     "fav_color": "black"
# }
# person3 = {
#     "name": "Olamide",
#     "age": 14,
#     "fav_color": "purple"
# }

# Students = {
#     "person1": person1,
#     "person2": person2,
#     "person3": person3
# }

# print(f"{Students['person3']['name']}'s favorite color is {Students['person3']['fav_color']}.")
# print(Students["person1"]["name"] + ", " + Students["person2"]["name"] + ", "+ Students["person3"]["name"])

# """
# Assignment
# Using the nested dictionary given in class, use the python input() statement to search a student's name from the
# records. Ensure you handle the letter cases user types.
# """

# # Nested dictionary of students
# person1 = {
#     "name": "Aisha",
#     "age": 12,
#     "fav_color": "blue"
# }
# person2 = {
#     "name": "Praise",
#     "age": 13,
#     "fav_color": "black"
# }
# person3 = {
#     "name": "Olamide",
#     "age": 14,
#     "fav_color": "purple"
# }

# Students = {
#     "person1": person1,
#     "person2": person2,
#     "person3": person3
# }


# user_input = input("Enter the student's name: ").strip().lower()  

# found = False 
# for key, value in Students.items():
#     if value["name"].lower() == user_input:
#         print(f"Record found: {value}")
#         found = True
#         break

# if not found:
#     print(f"No record found for the name '{user_input}'.")


# #Python Conditions
# ## if...else...elif...statements
# ### Uses equals(==), not equals(!=), less than(<), less than or equal to(<=),
# ### greater than(>), greater than or equal to(>=)
# num1 = 5
# num2 = 7
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} and {num2} ae equal")

# #Shorthand if-else
# age1 = 20
# age2 = 20

# if age1 >= age2: ##Full form of the sentence
#     print('She is a teenager')

# if age1 >= age2: print('She is a teenager') #shorthand if statement

# #Another shorthand example
# Tomi_age = 15
# Aisha_age = 16

# """
# This is called conditional expressions or tenary operators
# """

# print("Tomi is younger than Aisha") if Tomi_age < Aisha_age else print("Aisha is younger than Tomi")


# # Students_ages = [11,12,13,14,15]
# # if Tomi_age < 18 and Tomi_age in Students_ages:
# #     print("Tomi is not yet an adult and could not be admitted to our school")

# # if Tomi_age < 18 or Tomi_age in Students_ages:
# #     print("Tomi is not yet an adult and could not be admitted to our school")


# # if not(Tomi_age < 18) and Tomi_age in Students_ages:
# #     print("Tomi is not yet an adult and could not be admitted to our school")


# # user_input = int(input("Enter your age: "))

# # if user_input > 18 and user_input in Students_ages:
# #     print("You are not elligible to be admitted in our school")
# # elif (user_input < 18) and (user_input not in Students_ages):
# #     print("You are not up to 18 years and your age isn't in the school's legible age")
# # else:
# #     ("You are qualfied to get an admission in our school")


# #Nested if-statements
# num = 41
# if num > 10:
#     print(f"{num} is above 10")
#     if num > 20:
#         print(" and also above 10")
#     else:
#         print("but not above 20")


# #Python Match:
# ## Used to perform different actions based on different c0nditions

# day = int(input("Enter day of the week in numbrs (1-7)"))
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Days of the week are only 7")


# ###Match with 'if statement' as a safeguard
# month = 5
# day = 4

# match day:
#     case 1 | 2 | 3 | 4 | 5 if month == 4:
#         print("A weekday in April")
#     case 1 | 2 | 3 | 4 | 5 if month == 5:
#         print("A weekday in May")


# """
# Assignment:
# Given the following variables:
# Nmaes = ("Ade", "Aisha", "Praise", "Chris", "Olamide")
# ages = [11, 12, 13, 14, 15]

# Use the python input statement to search for a name in the tuple variable "Names" and output the 
# corresponding age in the variable ages.
# Hint: Use Python 'match'
# """


# # Variables
# Names = ("Ade", "Aisha", "Praise", "Chris", "Olamide")
# ages = [11, 12, 13, 14, 15]

# name_to_search = input("Enter a name: ")

# match name_to_search:
#     case "Ade":
#         print(f"{name_to_search} is {ages[0]} years old.")
#     case "Aisha":
#         print(f"{name_to_search} is {ages[1]} years old.")
#     case "Praise":
#         print(f"{name_to_search} is {ages[2]} years old.")
#     case "Chris":
#         print(f"{name_to_search} is {ages[3]} years old.")
#     case "Olamide":
#         print(f"{name_to_search} is {ages[4]} years old.")
#     case _:
#         print("Name not found in the list.")



# #Loops
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# for x in range(6):
#   print(x)


# for x in range(1,8,2):
#   print(x)
# else:
#     print("The loop is done")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)




secret_number = 13

print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 20.")

while True: 
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Excellent Guessing! Congratulations!")
        break 
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")




number = int(input("Enter a number to generate its multiplication table: "))

print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

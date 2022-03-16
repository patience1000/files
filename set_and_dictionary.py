# Details = {}
# while True:
#     proceed = input("would you like to add a new student, enter y to add and n to not:")
#     if proceed == "y":
#         # key = input("input key:")
#         name = input("what is you name:")
#         # pad = input("input key:")
#         school = input("what is the name of your school:")
#
#         Details[name] = (school)
#         # Details[key] = name
#         print(Details)
#     else:
#         print("okay")
#         break

# A company decided to give bonus of 5% to employee if his/her year of
# service is more than 5years. Ask user for their salary and year
# of service and print the net bonus amount.
#
# print("Enter your details to know if you are a beneficiary of the bonus.")
#
# salary = (input("Enter your salary:"))
# float_salary = float(salary)
# year = input("Enter your year(s) of service:")
# year_int = int(year)
# if year_int > 5:
#     print("your net bonus is:")
#     print(float_salary * 5/100)
# else:
#     print("you are not eligible")

#THE WHILE LOOP
# With the while loop we can execute a set of statements as long as
# a condition is true
# example
# print i as long i is less than 6:
# i = 1
# while i < 6:
#     print(i)
#     i = i + 1
#     i +=1

# names = ["patience", "joy","oma","stanley"]
# i = 0
# while i < 4:
#     print(names[i])
#     i = i + 1

# Note: remember to increment i, or else the loop will continue forever
# the loop requires relevant variables to be steady
#the break statement
# with the break statement, we can go out of the loop even if the while condition is true
# example
# exit the loop when i is 3:

# i=1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
# #     i += 1
#
# i=0
# while i < 6:
#     i += 1
#     print(i)
#     if i == 4:
#         continue
#         print(i)

# FOR LOOP
# A for loop is used for iterating over a sequence(that is either a list, tupple, dictionary a set or a string e.t.c
# example
# print each name in names list:

names = ["leo","benedict","paul","kelechi"]
# for name in names:
#     print(names)

#     the for loop does not require an indexing b4 hand
# looping through a string
# even strings are iterable objects, they contain a sequence of characters
# example
# loop tru the letters in the word "stanly":

# for x in "vincent":
#     print(x)

    # the break statement
    # with the break statement we can stop the loop before it has looped all the items;

# for x in "vincent":
#     if x == "c":
#
#         continue
#     print(x)

# the range() function
# to loop through a set of code a specified number of times, we can use the range() function
# starts at zero,increments by 1 and ends at
# range(6)
# for x in range(2,30,):
#     print(x)
# for x in range(2, 31,2):
#         print(x)
#else in a loop
# the else keyword in a for loop specifies a block of code to be executed when the loop is finished
# example
# print_all_numbers from_0_to 5, and print a message when the loop has ended:
# for x in range(6):
#     if x == 4:
#         break
#     print(x)
# else:
#     print("Finally finished")
# Note: The else block will not be executed if the image loop is stopped by a break statement

# nested loop
# a nested loop is a loop inside a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# example
# print each

# first_group_of_names = ["leo","benedict","oma","stanley",'vincent']
# second_group_of_names = ["jason","david","lamido","patience","priase"]
#
# for name in first_group_of_names:
#     for nam in second_group_of_names:
#         print(name,nam)

name = input("please enter your name:")
for x in name:
    if "b" in name:
        print("you have b in your name, why?")
        break
    else:
        print("nice job")
        break









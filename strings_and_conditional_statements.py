# Strings and conditional statements in python 👇👇

# string writing types....

# a='this ia a single qoute string'
# b="this a double qoute string"
# c="""this a triple qoute string"""

# escape characters in python

# next_line="this is a string with next line escape characters.\nthis a next line string"
# print(next_line)

# tab="this is a string with tab escape characters.\tthis a tab string"
# print(tab)


# length of string in python...
# str="this is a string"
# str_len=len(str)
# print(str_len)


# indexing in python
# str = "this is a string"
# print(str[2])


# print index of any iterable with python enumerate function
# in python indexing start from 0.
# str = "this is a string"
# for index,s in enumerate(str):
#     print(index)


# Slicing in python 👇👇
# Slicing in python means is acces a part of a string
# in case of slicing the indexing start from 1.


# # slicing with negative steps 👇👇
# str = "this is a string"
# # the last step -2 is the step and it will iterate the str from negative indexing and take every second charecter from the current index
# print(str[14:5:-2])


# # shortly print the whole iterative in negative sequence 👇👇
# str = "this is a string"
# print(str[::-1])


# # mixing positive and negative indexes👇👇
# str = "this is a string"
# print(str[5:-5])


# # reverse slicing with a negative skipping index 👇👇
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[::-2])


# # partial reverse slicing 👇👇
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[6:2:-1])


# now let's see all string function 👇👇👇

# # endsWith function check weather a string ends with given substring or not and it returns True false 👇👇
# name="nasir"
# print(name.endswith("nasi"))


# # capitalize function make the first letter of the string capitalize
# name="nasir"
# print(name.capitalize())


# # replace function replace particular value with the given value
# name="nasir"
# name = name.replace("sir","hid")
# print(name)


# # find function return the first occurence index of the given value or charecter
# name="nasir"
# print(name.find("a"))


# # count function return the number of occurences of the given value. like how many times it is in the code
# name = "nasir mia is a good programmer"
# characters = []
# for char in name:
#     if char not in characters:
#         characters.append(char)
#         # count occurences
#         print(char,": occures ",name.count(char)," times")
# print(len(characters))


# conditional statements with (if , elif, else) 👇👇
# confusion is with if and elif
# elif will only run if the if statement is false and if if statement is true then elif will not run ..

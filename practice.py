# text:str = "helloWorld";
# print(text.center(30,""))

# text = "hello world";
# print(text.count('o'));

# find in python
# text = "hello world";
# position = text.find("world");
# print(text[:position-1])

# format method
# name = "Nasir";
# age = 21;
# print("hello {} , though you are {} years old , so you are eligible".format(name,age));
# print("hello {} , though you are {} years old, so you are eligible".format(age,name))



# index method

# name = "Nasir";
# print(name.index('r'));



# isAlNum = checking that is that a alphanumeric.if it contains alphabet and numeric value return true

# alphanumeric = "NasirMIa123";
# print(alphanumeric.isalnum())


# isAlpha method= checking that is it contains only alphabet characters

# alpha = "alkfaslkfasdfklj";
# print(alpha.isalpha())


# isnumeric,isdegit,isdecimal method in python
# print("123".isdigit())
# print("123".isnumeric())
# print("123".isdecimal())


# isidentifier = check is any string can be used as a variable or not. if so then true otherwise false
# identifier = "abc-4";
# print(identifier.isidentifier()) # it will return false because "-" can't use in variable 

# identifier2 = "name";
# print(identifier2.isidentifier());  #it will return false because we can use name as a  variable.


# islower checks is any string is fully lowercase or not
# name = "nasir";
# print(name.islower());



# isupper checks is any string is fully uppercase or not
# name = "NASIR";
# print(name.islower());


# isprintable checks is any string contains any escaped character like \n
# printable = "Nasir\n";
# print(printable.isprintable());


# isspace checks is any string contains only spaces or not
# space = "    ";
# print(space.isspace())


# istitle checks is any setntence contain every word with the uppercase like "My First Video Title".
# title = "My First Video Title";
# print(title.istitle());    #it will return true because it contains every word first letter with uppercase.



# join method is use to join multiple words together with given character
# name = ["my","name","is","Nasir"];
# print(" ".join(name));
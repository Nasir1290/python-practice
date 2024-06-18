# Lets practice Dictionary and Set in python 👇👇👇


# Dictionary in python 👇


# # len() function => we can check the dictionary length
# dic = {"name":"Nasir","roll":568427}
# print(len(dic))


# # dict() function => we can create a dictionary with this function
# name="Nasir"
# roll=568427
# dic=dict(name=name,roll=roll)
# print(dic)


# # clear() function => clear all item from the dictionary
# dic={"name": "Nasir", "roll":568427}
# dic.clear()
# print(dic)


# # copy() function => work like other datatype in dictionary like list
# dic={"name": "Nasir", "roll":568427}
# dic2= dic.copy()
# dic2["roll"]=568426
# print(dic,":",dic2)
# print(dic2==dic)


# # get() function => is a function which is usefull to get value from dictionary when a value don't exist in the dictionary and if i tried to get this value then with dic["name"] this will give error but if i will use it with get function and pass the value and pass a default value if the value doesn't exist then it will not crash the app . it will return default value like below
# dic = {"name": "Nasir", "roll": 568427}
# print(dic["id"])  # it will crash the code though the id is not exist on dic
# # tid is not exist still it will return default value.not error
# print(dic.get("id", "unknown"))
# hello from "Nasir"


# # dictionary comprehension
# squares = {x: x**2 for x in range(1, 8)}
# print(squares)


# removing item from dictionary

# # pop() function => remove particular given key value from dictionary.
# info = {"name": "Nasir", "age":21, "hobby":"football"}
# info.pop("hobby")
# print (info)


# # popitem() function => remove the last key-value pair from dictionary
# info = {"name": "Nasir", "age":21, "hobby":"football"}
# info.popitem()
# print (info)


# # del()function => used to delete given key like this --> del(dic[key])
# info = {"name": "Nasir", "age":21, "hobby":"football"}
# del(info["name"])
# print(info)


# # clear() function remove all element from the dictionary
# info = {"name": "Nasir", "age":21, "hobby":"football"}
# info.clear()
# print(info)


# some common uses dictionary funciton 👇👇👇

# # get() method which will return a given value if the key not in dictionary. otherwise it will return none deafultly
# info = {"name": "Nasir", "age": 21, "hobby": "football"}
# print(info.get("neme","name not Found"))



## keys() method return all keys of dictionary and we can use them like below

# info = {"name": "Nasir", "age":21, "hobby":"football"}
# keys =info.keys()
# print("name" in keys)
# # real usecases like if i need some catetory information and i have to check if there any field missing then i can use dic.keys() to find all fields and compare them with my given field

# given_field=["name","age","roll","hobby","technology"]
# missing_field=[field for field in given_field if field not in info]
# if missing_field:
#     print(f"Missing fields are {missing_field}")



# values() method return all value of the dictionary and we can use them like below 
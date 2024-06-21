# Function in python 👇👇👇


# # simple function with def definition.
# def my_func():
#     print("This is my function")
# my_func()


# # function with parameters..
# def num_sum(num1,num2):
#     sum=num1+num2
#     return sum
# get_sum=num_sum(2,3)
# print(get_sum)


# # here's in the previous example we take two parametes , but what if the input parameter are more than two?This time the code will crash.To handle this we can use *args and **kwargs
# def get_sum(num1,*args):
#     sum1=sum((num1,)+args)
#     print(sum1)
# get_sum(1,2,3,4,0,9,8)


# # in the previous example we see how we can handle more than one parameter. Now here the problem is, with this code we can't give key-value pairs as arguments.So how can we handle this?let's see

# def handle_parametes_and_dictionary(num1,*args,**kwargs):
#     print(sum((num1,)+args))
#     print(kwargs)
# handle_parametes_and_dictionary(0,2,3,4,name="nasir")


# def handle_parameter(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# handle_parameter(name="nasir",age=20)


# lambda function in python

# # it's a one line function which is work like that
# add_ten = lambda x:x+10
# print(add_ten(50))


# lambda function with higher order function like map(),filter(),sorted(),reduce()

# # lambda with map function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# squared_numbers = (map(lambda x: x**2, numbers))
# # convert it into a list because list return a reference value
# print(list(squared_numbers))


# # lambda with filter function

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# filtered_numbers = list(filter(lambda x:x%2!=0,numbers))
# #  convert it into a list because filter return a reference value
# print(filtered_numbers)


# # lambda function in sorted function

# # fruite_list=[("apple",1),("banana",2),("cucumber",3),("mango",4),("Jackfruit",5)]
# # dic=[{key:value} for key,value in fruite_list]
# # print(dic)

# fruites=[{'apple': 1}, {'banana': 2}, {'cucumber': 3}, {'mango': 4}, {'Jackfruit': 5}]
# sorted_fruites=sorted(fruites,key=lambda x:list(x.values())[0])
# print(sorted_fruites)


# # reducing boilerplate code by using lambda function

# def apply_function(x, func):
#     print(func(x))
# apply_function(5,lambda x:x+10)
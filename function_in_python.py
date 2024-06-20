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
# it's a one line function which is work like that
add_ten = lambda x:x+10
print(add_ten(50))


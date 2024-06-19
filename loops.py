# Loops in python 👇👇👇

# Loops in Python are used to execute a block of code repeatedly. Python supports two types of loops: (1)for loops and (2)while loops


# for loops👇👇

# # iterating ovet a list 
# fruits = ["apple", "orange", "blackberry","mango","banana","cupcake","cherry"]
# for fruit in fruits:
#     print(fruits.index(fruit)+1,":",fruit)


# # iterating overa  range of numbers
# for num in range(1,6):
#     print(num)



# # iterating over a dictionary
# student_score = {"Alice": 85, "Bob": 92, "Charlie": 78}
# for student,score in student_score.items():
#     print(student,"got:",score)



# # using a else after a for loop if you want to execute a block of code after your for loop completion
# for i in range (1,6):
#     print(i)
# else:
#     print("execute your own code you want to execute")





# # while loops are run depending on a condition
# count = 1
# while count <= 10:
#     print(count*"*")
#     count+=1
    
    
    
# # while loop with break statement
# count = 1
# while True:
#     print(count)
#     count+=1



# # using else with while loop
# count = 1
# while count <= 10:
#     print(count)
#     count+=1
# else:
#     print("run yoiur code after while loop")



# # nested loop
# # in nested loop the under loop will finished first by keeping the i'th loop on the hand
# for i in range (3):
#     for j in range (4,7):
#         print(f"i is :{i}, j is :{j}")


# with open("example.txt", "r") as file:
#     for line in file:
        print(line.strip())
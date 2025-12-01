# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.
list1= [1,2, 3]
#       0 1  2
list2= [4,5,6]
nested_list= [list1, list2]
# list is numered 0    1
print(nested_list)
print(nested_list[0][1]) #output is from the first list but the second number

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2])

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:
fruit=["apple", "orange", "banana", "peach"]
veggies= ["poop", "celery", "potata" ]
meats=["chicken", "fish", "turkey"]

gro= [fruit, veggies, meats] #fruit is going to be 0 and meats is 2 in order to go in brackets
print(gro[1][2])
print(gro[0][2])

# Build a matrix variable containing 3 lists of 3 numbers each.

groceri=[["chicken", "fish", "turkey"], ["apple", "orange", "banana", "peach"], ["poop", "celery", "potata" ] ]
for collection in groceri:
    for food in collection:
        print(food, end="")
        print()

# Print the first list.
num_p = ((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*", 0, "#"))

for row in num_p:
    for num in row:
        print(num, end="")
    print()
# Print the second item from the third list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2]) #3

exampl= [row[0] for row in matrix]

print(exampl)


bum= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(bum[2][0])
# Use a list comprehension to extract the last item from each sub-list.
comprehensio=[row[-1] for row in bum]
print(comprehensio)


squarednums= [x**2 for x in range(1,11)]
#for x in range (1,11):
#squared= x**2
#print(squared)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
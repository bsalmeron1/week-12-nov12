# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [1, 2, 3, 4, 5]
numbers.sort()
print(numbers)
numbers.append(6)
numbers.extend([10,11,12,13,14]) #faster method  of appending
print(numbers)

numbers.extend(list(range(15,515)))
numbers.extend(list(range(300,1900)))
print(numbers[0])         # apple
print(numbers[0:])
# Practice Problems:

# Create a list with 5 of your favorite foods.
food= ['popeyes', 'deer cartilage', 'baboon placenta', 'orangutang calf', 'tacos']
print(food)


print(food[1:2])

print(food[4:])
# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.
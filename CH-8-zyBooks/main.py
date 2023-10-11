##### 8.6 List Slicing #####

# nums = [1, 1, 2, 3, 5, 8, 13]
# print(nums[1:4])
# print(nums[3:-1])

#####8.8 List comprehension
#This eliminates the need to use for loops (see the same table in ch8)
#table 8.8.1
#1. Add 10 to every element.
#my_list = [5, 20, 50]
# my_list = [(i+10) for i in my_list]
# print(my_list)

#2.Convert every element to a string. 
# my_list = [5, 20, 50]
# my_list = [str(i) for i in my_list]
# print(my_list)

#..4. Find the sum of each row in a two-dimensional list.
# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# sum_list = [sum(row) for row in my_list]
# print(sum_list)

#5. Find the sum of the row with the smallest sum in a two-dimensional table.
# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# min_row = min([sum(row) for row in my_list])
# print(min_row)

####8.8.2 Conditional list comprehension example:
# Get a list of integers from the user
# numbers = [int(i) for i in input('Enter numbers:').split()]
# # Return a list of only even numbers
# even_numbers = [i for i in numbers if (i % 2) == 0]
# print(f'Even numbers only: {even_numbers}')

###8.9.1 list.sort() method example: Alphabetically sorting book titles
# books = []
# prompt = 'Enter new book: '
# user_input = input(prompt).strip()

# while (user_input.lower() != 'exit'):
#     books.append(user_input)
#     user_input = input(prompt).strip()

# books.sort()

# print('\nAlphabetical order:')
# for book in books:
#     print(book)

#note that sort works on alphabet
# x = ['Moon', 'Apple', 'Blue', 'Beer', 'Mountain Lion']
# x.sort()
# print(x)

###8.9.2 sorted() vs sort()###
# numbers = [int(i) for i in input('Enter numbers: ').split()]
# sorted_numbers = sorted(numbers)
# print(f'\nOriginal numbers: {numbers}')
# print(f'Sorted numbers: {sorted_numbers}')
#Note: list.sort() modifies an existing list while sorted() creates a new one.

#example (I made this):
# list = [ 1, 5, 6, 2, 10]
# print(list)
# print(sorted(list))
# print(list)
# list.sort()
# print(list) #Note the change from the original list

#Figure 8.9.4: The key argument to list.sort() or sorted() can be assigned any function.
# my_list = [[25], [15, 25, 35], [10, 15]]
# sorted_list = sorted(my_list, key=max)
# print(f'Sorted list: {sorted_list}')

# Reverse argument (prints from greatest to least)\
#This is the general format
# x.sort(reverse=True) 

#Sorting 8.9.3 participation exercise
#x.sort(key=str.upper)
# Setting key=str.upper converts each element of x to upper-case before comparing values
#
### 8.13.1 Dictionary methods
# my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
#The following replaces the value of burger with sandwich.
# my_dict['burger'] = my_dict['sandwich']
# val = my_dict.pop('sandwich')
# print(my_dict['burger'])

### Challenges###
#8.3.2 Extra credit in grades
# calculates extra credit given for grades over 100
#user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores
# sum_extra = 0 # Initialize 0 before your loop
# counter = 0
# ''' Your solution goes here '''
# for grade in test_grades:
#     if grade > 100:
#         sum_extra += grade
#         counter += 1
# sum_extra = sum_extra - (100 * counter)
# print(f'Sum extra: {sum_extra}')

# hourly_temperature = [90, 92, 94, 95]

# # Start with an empty string
# s = ""
# for t in hourly_temperature:
#     if s != "":
#         s += "-> "

#     s += str(t) + " "
# print(s)

#8.5 Print a "multiplication table"
#Note, input is: '1 2 3,2 4 6,3 6 9' and this should output a 3x3 table
# user_input= input()
# lines = user_input.split(',')
# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

# mult_table = [[int(num) for num in line.split()] for line in lines]
# ''' Your solution goes here '''
# for row in mult_table:
#     for i in range(len(row)):
#         cell = row[i]
#         print(cell, end=' | ' if i!=len(row)-1 else '')
#     print()

#8.14 Report Country Population
#input: 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800'
# user_input = input()
# entries = user_input.split(',')
# country_pop = {}

# for pair in entries:
#     split_pair = pair.split(':')
    # country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }
# print(country_pop)
# ''' Your solution goes here '''
# for country, pop in country_pop.items():
#     print(f'{country} has {pop} people.')

#Chapter 7 Labs

## Lab7.5.1 Verify input contains only integers from 0-9 ##
# user_string = input()
# ''' Type your code here. '''
# if user_string.isdigit():
#     print('Yes')
# else:
#     print('No')

### 7.6 Converts Names into Lastname, initials ###
#I don't get why it only works in the format ... = name
# name = input().split()
# if len(name) == 3:
#     first_name, middle_name, last_name = name
#     print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')
# elif len(name) == 2:
#     first_name, last_name = name
#     print(f'{last_name}, {first_name[0]}.')
# else:
#     print('not valid')

#Alternate Solution (that makes more sense to me)
# name = input().split()
# if len(name) == 3:
#     first_name = name[0]
#     middle_name = name[1]
#     last_name = name[2]
#     print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')
# elif len(name) == 2:
#     first_name = name[0]
#     last_name = name[1]
#     print(f'{last_name}, {first_name[0]}.')
# else:
#     print('not valid')

### 7.7 Lab Counting Characters in a string ###
# phrase = str(input())
# counter = phrase.count(phrase[0]) - 1
# if counter != 1:
#     print(f'{counter} {phrase[0]}\'s')
# else:
#     print(f'{counter} {phrase[0]}')

### 7.8 Mad Lib Loop ###
# while True:
#     lib = str(input())
#     if 'quit' in lib:
#         break
#     else:
#         a,b = lib.split(' ')
#         print(f'Eating {b} {a} a day keeps you happy and healthy.')

### 7.9 Palindromes ###
# words = str(input())
# removespaces = words.replace(" ", "")
# checkwords = removespaces[::-1]

# if removespaces == checkwords:
#     print(f'palindrome: {words}')
# else:
#     print(f'not a palindrome: {words}')

### 7.10 Checking for Alphabetic Characters ###
#This will remove any misc characters such as 123 or ! & $ 
# words = input()
# output = ''
# for char in words:
#     if char.isalpha():
#         output += char
# print(output)

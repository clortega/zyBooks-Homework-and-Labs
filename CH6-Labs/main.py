#Ch6 Labs

#6.18 Converts kilos to pounds
# def kilo_to_pounds(kilos):
#     # This statement intentionally has an error(FIXED). 
#     return (kilos * 2.204)


# # Main part of the program starts here. Do not remove the line below.
# if __name__ == '__main__':
#     kilos = float(input())
    
#     pounds = kilo_to_pounds(kilos)
#     print(f'{pounds:.3f} lbs')


#Driving Cost
#My Answer:
# Define your function here.
# def driving_cost(miles_per_gallon, dollars_per_gallon,miles_driven=10.0):
#     return (dollars_per_gallon * miles_driven) / miles_per_gallon 

# if __name__ == '__main__':
#     # Type your code here.
#     miles_per_gallon = float(input())
#     dollars_per_gallon = float(input())
    
# cost = driving_cost(miles_per_gallon, dollars_per_gallon)
# print(f'{cost:.2f}')
# print(f'{cost*5:.2f}')
# print(f'{cost*40:.2f}')

#Accepted Answer:
# def driving_cost(miles_per_gallon, dollars_per_gallon, 
#     miles_driven=10.0):
#     return (miles_driven / miles_per_gallon) * dollars_per_gallon
        
# if __name__ == '__main__':
#     # Type your code here.
#     miles = float(input())
#     dollars = float(input())

#     price = driving_cost(miles, dollars) 
#     print(f'{price:.2f}')
#     print(f'{price * 5:.2f}')
#     print(f'{price * 40:.2f}')

#Lab 6.20 Feet to steps walked
# def feet_to_steps(user_feet):
#     steps_walked = user_feet//2.5
#     return steps_walked

# if __name__ == '__main__':
#     # Type your code here.
#     input_feet = float(input())
#     steps_walked = feet_to_steps(input_feet)
#     print(int(steps_walked))

#6.21 Reverse Binary Converter using 2 functions
# def int_to_reverse_binary(integer_value):
#     binary = ''
#     while integer_value > 0:
#         binary = binary + str(integer_value % 2)
#         integer_value = integer_value // 2
#     return  binary
    
# def string_reverse(input_string):
#     return input_string[::-1]

# if __name__ == '__main__':
    
#     integer_value = int(input())
#     input_string = int_to_reverse_binary(integer_value)
#     print(string_reverse(input_string)

#Lab 6.22 swap values around in a list
# # Define your function here.
# def swap_values(user_val1, user_val2, user_val3, user_val4):
#     temp1 = user_val1
#     temp2 = user_val3
#     user_val1 = user_val2
#     user_val2 = temp1
#     user_val3 = user_val4
#     user_val4 = temp2
#     return user_val1, user_val2, user_val3, user_val4

# if __name__ == '__main__': 
#     # Type your code here. Your code must call the function.
    
#     user_val1 = int(input())
#     user_val2 = int(input())
#     user_val3 = int(input())
#     user_val4 = int(input())
#     listswap = swap_values(user_val1, user_val2, user_val3, user_val4)
#     print(*listswap)

#6.23 Fibonacci
# def fibonacci(n):
#     a, b = 0, 1
#     if n < 0:
#         return -1
#     for start_num in range(n):
#         a, b = b, a + b
#     return a

# if __name__ == '__main__':
#     start_num = int(input())
#     print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
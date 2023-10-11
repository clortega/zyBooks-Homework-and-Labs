### Ch 8 zyBooks Labs###

### 8.16 varied amount of input data ###
# take floating non-negative numbers and print the avg and max
# nums = []
# while not nums:
#     number = input()
#     nums = [float(x) for x in number.split() if x]

# avg = float(sum(nums) / len(nums))
# print(f'{max(nums):.2f} {avg:.2f}')

### 8.17 Filter and sort a list ###
#From the input sort and print only negatives

# user_input = input()

# integer = [int(x) for x in user_input.split()]
# neg_integer = sorted([x for x in integer if x < 0], reverse=True)

# for output in neg_integer:
#     print(output, end=' ')

### 8.18 Elements in a Range ###
# If the input is:
#25 51 0 200 33
#0 50
#The output is
# 25,0,33
#Answer:
# input_numbers = [int(x) for x in input().split(' ')]
# input_range = [int(x) for x in input().split(' ')]

# for number in input_numbers:
#     if input_range[0] <= number <= input_range[1]:
#         print(number, end=',')




# Lab 8.19 Contact List
# I spent TOOO LONG on this one. I blame the bs way zybooks gave me the input.
#This gets input for all contacts
# allContacts = input()
# #This gets a contact name from the user
# contactName = input()
# #This splits the contact by space
# splitContact = allContacts.split(" ")
# # print(splitContact)
# #This iterates through the split contacts
# for i in range(len(splitContact)):
#    #If the current element of the list is the same as the input for contactName
#    if(splitContact[i] == contactName):
#        #The loop is forcefully exited
#        break
# #This prints the phonenumber
# y = splitContact[i]
# result_string = ''.join(filter(lambda x: x.isdigit() or x == '-', y))
# print(result_string)

#tHIS might help the above...although with my previous submissions.
# xlist = [1,["a","b",["x","y"]]]
# print(xlist)
# #we want to print y:
# print(xlist[1][2][1])
# lol = [[1,2,3],[4,5,6], [7], [8,9,10,11]]


# Lab 8.20 Car Wash
# services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
# base_wash = 10
# total = 0

# service_choice1 = input()
# service_choice2 = input()

# ''' Type your code here '''
# print("ZyCar Wash")
# print("Base car wash - ${}".format(base_wash)) 
## {} is a placeholder for a value that will be inserted into the string.
## .format() is a method call that substitutes in placeholders. in this case base_carwash
# total += base_wash

# if service_choice1 != '-':
#     if service_choice1 in services:
#         total += services[service_choice1]
#     print("{} - ${}".format(service_choice1, services[service_choice1]))

# if service_choice2 != '-':
#     if service_choice2 in services:
#         total += services[service_choice2]
#     print("{} - ${}".format(service_choice2, services[service_choice2]))


# print("-----")
# print("Total price: ${}".format(total))

## Lab 8.21 Check if list is sorted
def in_order(nums):
    # Type your code here.
    return all(nums[i-1] <= nums[i] for i in range(1, len(nums)))
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
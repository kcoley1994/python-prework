# Question 1 
# write a function to print hello_username 
# USERNAME is the input of the function 
def hello_name(user_name):
    """Display username """
    print(f"Hello_username: {user_name}")

hello_name("kevon")



# Question 2
# Write a python function, first_odds that print
# odd numbers from 1-100 and return nothing 
def first_odds():
    """Display Odd Numbers"""
    odd_num =range(1,100,2)
    for num in odd_num:
        print(num)
first_odds()






# Question 3 
# Write Python function 
# max_num_in_list to return the max numer of given list
def max_num_in_list(a_list):
    """display max number"""
    print(max(a_list))

max_num_in_list([1,2,3,4,5])



# Question 4
# Write function to return given year is a leap year
# A leap year is divisible by 4, but not /100
# the return should be boolean 
def is_leap_year(a_year):
    if  a_year % 4 == 0:    
        print(True)
    else:
        print(False)


is_leap_year(2000)
is_leap_year(400)
is_leap_year(100)
is_leap_year(2001)

# Question 5 
# Wrie function to check if all num in list are consecutive
# The return should be boolean type 
def is_consecutive(a_list):
    if a_list in range(1,10):
        print(True)

is_consecutive(1,2,5)

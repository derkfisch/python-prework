#Question 1
    #Write a function to print "hello_USERNAME!" 
    #USERNAME is the input of the function.
    #The first line of code has been defined as below.

def hello_name(user_name):
    """Display a simple greeting"""
    #add the function .upper to capitalize username
    print("hello_" + user_name.upper() + "!")
#function is display a greeting that puts out a user_name which is username
hello_name('username')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Display odd numbers from 1 to 100"""
    x = 0
    #x must start at zero and loop towards 100
    while x < 100:
        #x is = x + 1
        x += 1
        #check if x divided by 2 has a remainder of 0
        #if so, continue to print x
        #the previous direction will make list odd
        if x % 2 == 0:
            continue
        print(x)
#print loop of function
print(first_odds())

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list
#The first line of the code has been defined as below

def max_num_in_list(a_list):
    """Display max number of a given list"""
    #max of a_list to 4 index spots
    max = a_list[4]
    #for every x(index position) in a_list
    for x in a_list:
        # if integer in x is great than the current max then
        if x > max:
            #the integer in position x is the new max
            x = max
    #return the max of loop
    return max
#MUST PRINT the directions to the function of the list        
print(max_num_in_list([1, 2, 3, 4, 5]))

#Question 4
#Write a function to return if the given year is a leap year
#A leap year is divisible by 4, not divisible by 100 unless it is divisible by 400
#The return should be boolean Type(true/false)

def is_leap_year(a_year):
    """Answer if a particular year is a leap year."""
    #most years or leaps in this case are not leap years or FALSE
    leap = False
    #but if the year is divisible by 4 with no remainder
    if a_year % 4 == 0:
        #must be true that is a leap year
        leap = True
        #if the year is divisible by 4 and 100 with no remainder,
        #AND has a remainder when divided by 400
        if a_year % 100 == 0 and a_year % 400 != 0:
            #it is not a leap year, false
            leap = False
        #if the year is divisible by 4 and 100 with no remainder,
        #AND DOES NOT have a remainder when divided by 400
        if a_year % 100 == 0 and a_year % 400 ==0:
            #it is a leap year, true
            leap = True
        #for any numbers not divisble by 4, 100 or 400    
        else:
            #it is not a leap year, false
            leap = False
    return leap
#enter a year as an integer in the input in the command line
a_year = int(input())
#True = leap year, False = not a leap year
print(is_leap_year(a_year))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers
#The return should be boolean Type

def is_consecutive (a_list):
    """Find if list is filled with consecutive numbers"""
    #Order items in a_list, sort(a_list)
    #set counter to match beginning of list
    #as you loop over it, check if counter is = to current number
    #if != return false (nonconsecutive)
    # ex. a_list is [2,3,4,5,6,7]
    #set counter = start of a_list which is "2"
    #then loop over list checking is counter, 2, is = number were on
    #if so add 1 to counter
    #if we get to end of list successfully, return true (consecutive)
    #if any point our counter returns false, we are kicked out of loop

    #????????????


def is_consecutive (a_list):
    """Find if list is filled with consecutive numbers"""
    a_list = [1,2,3,4,5]
    a_list.sort()
    x = a_list(1)
    for x in a_list:
        if x == a_list():
            x += 1
            return True
        else:
            return False

print(is_consecutive()) 
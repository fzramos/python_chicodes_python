#Question 1 - write a function to print "Hello_USERNAME"

def hello_name(user_name):
    print("Hello_" + user_name.upper() + "!")

hello_name('Carlos')


# Question 2 - Print the odd numbers between 1 and 100
def odd_numbers():
    for i in range(1, 101, 2):
        print(i)

odd_numbers()


# Question 3 - Write a function that returns the max number in a given list
def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list(list(range(0,40,3))))


#Question 4 - Write a function to return if the given year is a leap year
def is_leap_year(a_year):
    if a_year % 4 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False

is_leap_year(2000)

#Question 4 1.b solution
def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 ==0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap(2019)

# Question 5 - Write a function to find if all the numbers in a list are consecutive
def is_consecutive(a_list):
    i = 0 #counter
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)

is_consecutive([1, 2,3])
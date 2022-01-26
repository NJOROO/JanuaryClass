# Python Program to Check if a Number is Divisible by 5

# Take the Input From the User
number = int(input("Enter any  Number: "))

if((number % 5 == 0)):
    print("Given Number {0} is Divisible by 5".format(number))
else:
    print("Given Number {0} is Not Divisible by 5".format(number))
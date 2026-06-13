import calendar as cd

x = int(input("enter a year : "))

# Find leap year or not
# Method 1.

def find_leapYear(n):
    print("if else statment first")
    if(n % 4 ==0 or n % 400==0):
        print("leap year ",n)
    else:
        print("not leap year ")    

# using second if else statment
# Method 2.

def leap_yearSecond(n):
    print("if else statment second")
    if((n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)):
        print("leap year",n)
    else:
        print("not leap year ")        

# using calender method
# Method 3.

def leap_yearCalender(n):
    print("using calender ")
    x = cd.isleap(n)
    print(n,f"is a leap year -> {x}")


# using calender method
# Method 3.
def leap_year_lambda(n):
    print("use lambda function ")
    year = lambda n : True if((n % 4 == 0 and n %100 !=0) or (n % 400 ==0)) else False
    print(n,f"is a leap year -> {year(n)}")


# calling first if else statment
find_leapYear(x)
# calling second if else statment
leap_yearSecond(x)
# calling calender
leap_yearCalender(x)
# calling lambda function 
leap_year_lambda(x)   
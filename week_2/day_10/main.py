# Functions with Ouputs
def sum(a, b):
    return a + b

# Exercise -> Days in Month
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   

    if month == 2 and is_leap_year(year):
        return 29
    
    return month_days[month - 1]

#Returns the number of day in a specified month. 

import calendar

def days_in_month(month_name, year):
    # Get the month number from the month name
    month_number = list(calendar.month_name).index(month_name.capitalize())
    
    # Check if the month name is valid
    if month_number == 0:
        return 0  # Invalid month name
    
    # Convert year to integer
    year = int(year)
    
    # Determine the number of days in the month
    num_days = calendar.monthrange(year, month_number)[1]
    
    return num_days

# Test the function
month_name = input("What month? ")
year = input("What year? ")
print(days_in_month(month_name, year))

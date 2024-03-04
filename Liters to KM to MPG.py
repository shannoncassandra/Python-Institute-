#Converts liters to 100km to miles per gallon and visa versa. 

def liters_100km_to_miles_gallon(liters):
    # 1 mile is approximately 0.621371 kilometers
    # 1 gallon is approximately 3.78541 liters
    # mpg = 235.2146 / l/100km
    return 235.2146 / liters

def miles_gallon_to_liters_100km(miles):
    # 1 mile is approximately 0.621371 kilometers
    # 1 gallon is approximately 3.78541 liters
    # l/100km = 235.2146 / mpg
    return 235.2146 / miles

# Test the functions
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

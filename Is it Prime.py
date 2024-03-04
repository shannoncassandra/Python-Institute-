#Tells you if a value is prime, and specifies prime numbers in a range. 

def is_prime(n):
    if n <= 1:
        return False
    
    # Check divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisor found, it's prime
    return True

# Test the function
print(is_prime(5))  # Output should be True
print(is_prime(16))  # Output should be False

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


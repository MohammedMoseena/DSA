# This code calculates the LCM (Least Common Multiple) of two numbers using the relationship with GCD (Greatest Common Divisor).

def gcd(a, b):
    # This function calculates the GCD of two numbers using the Euclidean algorithm.
    if b == 0:
        return a  # Base case: when b is 0, the GCD is a.
    return gcd(b, a % b)  # Recursive case: call gcd with b and the remainder of a divided by b.

def lcm(a, b):
    # This function calculates the LCM of two numbers using the formula: lcm(a, b) = abs(a * b) // gcd(a, b).
    return (a * b) // gcd(a, b)

# Take two integer inputs from the user.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Print the LCM of the two numbers.
print("LCM:", lcm(a, b))

# Time complexity: O(log(min(a, b)))
# Space complexity: O(1)
# Auxiliary Space: O(log(min(a, b)))

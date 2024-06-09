# Iterative Power using Binary Exponentiation

'''
Approach:
1. Binary Exponentiation: Utilizes the fact that every number can be expressed as a sum of powers of 2. It iterates through each bit of the exponent n, from the least significant bit (LSB) to the most significant bit (MSB).
2. Loop Iteration: The algorithm iterates while n is greater than 0.
3. Odd Exponents: If the current bit of n is set (i.e., n is odd), it multiplies the result (res) by the base (x).
4. Square Base: In each iteration, the base x is squared to compute the next power of x.
5. Divide Exponent: n is divided by 2 in each iteration to move to the next bit.
6. Result: The final result is returned after all bits of n are processed.

'''

def power(x, n):
    res = 1  # Initialize result to 1
    while n > 0:  # Loop until n becomes 0
        if n % 2 != 0:  # If the current bit of n is set (i.e., n is odd)
            res *= x  # Multiply the result by x
        x *= x  # Square x for the next iteration
        n //= 2  # Divide n by 2 to move to the next bit
    return res  # Return the result

# Take input for base (x) and power (n) from the user
x = int(input("Enter base: "))
n = int(input("Enter power: "))

# Call the power function and print the result
print(power(x, n))

#Time complexity:O(logn)
# Auxilary Space:O(1)
# Space Complexity:O(1)
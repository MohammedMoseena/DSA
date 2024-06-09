# This code calculates the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm.

'''
Approach:
1. Input: Read two integer inputs (a and b) from the user.
2. Base Case: If b is 0, return a because the GCD of a and 0 is a.
3. Recursive Case: If b is not 0, recursively call the gcd function with b and a % b (the remainder when a is divided by b).

Explanation of gcd(b, a % b):
1. The Euclidean algorithm is based on the principle that the GCD of two numbers does not change if the larger number is replaced by its remainder when divided by the smaller number.
2. Mathematical Basis: If r is the remainder when a is divided by b (i.e., r = a % b), then gcd(a, b) = gcd(b, r).
Step-by-Step:
3.
i. Initial Call: gcd(a, b) - Start with the two numbers a and b.
ii. First Recursive Call: gcd(b, a % b) - Replace a with b and b with a % b.
iii. Subsequent Recursive Calls: Continue this process until b becomes 0.
iv. Termination: When b is 0, return a as the GCD.

Example:
To find gcd(48, 18):
gcd(48, 18) → gcd(18, 48 % 18) → gcd(18, 12)
gcd(18, 12) → gcd(12, 18 % 12) → gcd(12, 6)
gcd(12, 6) → gcd(6, 12 % 6) → gcd(6, 0)
gcd(6, 0) → 6 (since b is 0, return a)

Complexity:
Time Complexity: O(log(min(a, b))) - The number of recursive calls is proportional to the logarithm of the smaller number.
Space Complexity: O(1) - Only a constant amount of space is used for the variables.
Auxiliary Space: O(log(min(a, b))) - Due to the recursion stack. Each recursive call adds a new frame to the stack until the base case is reached.

'''


def gcd(a, b):
    # Step 1: Base case of the recursion.
    if b == 0:
        return a  # When b is 0, the GCD is a.

    # Step 2: Recursive case.
    return gcd(b, a % b)  # Recur with b and the remainder of a divided by b.

# Take two integer inputs from the user.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Print the GCD of the two numbers.
print("GCD:", gcd(a, b))

# Time complexity: O(log(min(a, b)))
# Space complexity: O(1)
# Auxiliary Space: O(log(min(a, b)))

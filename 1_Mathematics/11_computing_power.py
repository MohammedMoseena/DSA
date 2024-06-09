# Computing power of a number using divide and conquer (recursive) approach

'''
1. Base Case: If the power (n) is 0, return 1. This is the base case of the recursion.
2. Recursive Step: If the power is not 0, divide the problem into smaller subproblems by calculating temp = power(x, n // 2). This step halves the value of n in each recursive call.
3. Combine Solutions: Combine the solutions of the subproblems by squaring temp.
4. Handling Odd Powers: If n is odd, multiply the result by x before returning.
5. Recursion Unwinding: Continue this process until the base case is reached.
6. Return Result: Return the final computed result.

'''

def power(x, n):
    # Base case: If the power is 0, return 1
    if n == 0:
        return 1
    
    # Recursive step: Divide the problem into smaller subproblems
    temp = power(x, n // 2)
    
    # Combine the solutions of the subproblems
    temp = temp * temp
    
    # If n is even, return the result directly
    if n % 2 == 0:
        return temp
    
    # If n is odd, multiply the result by x before returning
    return x * temp

# Take input for base (x) and power (n) from the user
x = int(input("Enter base: "))
n = int(input("Enter power: "))

# Call the power function and print the result
print(power(x, n))


#Constraints:
# Time complexity:O(logn)
# Space Complexity:O(1)
# Auxilary Space:O(logn)
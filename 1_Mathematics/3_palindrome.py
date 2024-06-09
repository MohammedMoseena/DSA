# This code checks whether a given number is a palindrome.

'''
This approach can be used when the number of digits in the given number is less than 10^18 because if the number of digits of that number exceeds 10^18, we can’t take that number as an integer since the range of long long int doesn’t satisfy the given number.
'''

def isPalindrome(n):
    # Step 1: Store the original number in a temporary variable.
    temp = n
    
    # Step 2: Initialize a variable to store the reversed number.
    rev = 0
    
    # Step 3: Use a while loop to reverse the digits of the number.
    while temp > 0:
        x = temp % 10            # Extract the last digit of the number.
        rev = rev * 10 + x       # Add the digit to the reversed number.
        temp = temp // 10        # Remove the last digit from the original number.
    
    # Step 4: Check if the reversed number is equal to the original number.
    return n == rev

if __name__ == '__main__':
    # Step 5: Take an integer input from the user.
    n = int(input("Enter n:"))
    
    # Step 6: Print the result of the palindrome check.
    print(isPalindrome(n))

#Constraints:
# Time complexity: theta(log n)
# Space complexity: theta(1)
# Auxiliary space: theta(1)





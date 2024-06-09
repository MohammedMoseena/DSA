# This code counts the number of digits in a given number.
import math
#Best approach
x = int(input("Enter x:"))
print(math.floor(math.log10(x)+1))

# Method-2
# Step 1: Take an integer input from the user.
x = int(input("Enter x:"))

# Step 2: Initialize a counter variable to zero. This will keep track of the number of digits.
count = 0

# Step 3: Use a while loop to repeatedly divide the number by 10 until it becomes zero.
# Each iteration of the loop removes the last digit of the number.
while x > 0:
    x = x // 10
    count += 1  # Increment the counter in each iteration.

# Step 4: After the loop ends, the counter will contain the number of digits in the input number.
print(count)



#Constraints
# Time complexity: theta(log n)
# Space complexity: theta(1)
# Auxiliary space: theta(1)





'''
Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

Solve this without using any built-in list methods.

You can assume that the list is non-empty.

Complexity:
n = array length
Time = 0(n)
Space = 0(1)
'''

def max_value(nums):
  # Initialize the maximum value with the first element of the list. It guarantees the list is non-empty
  maximum = nums[0]
  # Iterate through each number in the list.
  for num in nums:
    # Check if the current number is greater than the current maximum.
    if num > maximum:
      # If it is, update maximum to the new largest number.
      maximum = num
      
  return maximum
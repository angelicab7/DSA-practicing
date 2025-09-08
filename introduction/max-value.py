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
  maximum = float('-inf')
  
  for num in nums:
    if num > maximum:
      maximum = num
      
  return maximum
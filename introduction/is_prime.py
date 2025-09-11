'''
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.

Complexity:
n = input number
Time: O(square_root(n))
Space: O(1)
'''

def is_prime(n):
  # Check if the input number `n` is less than 2, otherwise returns false
  if n < 2:
    return False
    # starting from 2 and going up to, but not including, `n`, to test every possible integer divisor of `n` between 2 and `n-1`.
  for i in range(2, n):
    # Finally check if the remainder of `n` divided by `i` is 0.If It's true, it means `i` is a divisor of `n`.
    if n % i == 0:
      return False

  return True




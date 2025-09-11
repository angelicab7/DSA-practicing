'''
Write a function, fizz_buzz, that takes in a number n as an argument. The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

if the number is divisible by 3, make the element "fizz"
if the number is divisible by 5, make the element "buzz"
if the number is divisible by 3 and 5, make the element "fizzbuzz"

Complexity:
n = input number
Time: O(n)
Space: O(n)
'''

def fizz_buzz(n):
  # Initialize an empty list to store the results.
  result = []

# Loop through the numbers from 1 up to and including n.
  for i in range(1, n + 1):
     #Check for divisibility by both 3 and 5 first. It's better to start with the case where 3 and 5 are true.
    if i % 3 == 0 and i % 5 == 0:
      result.append("fizzbuzz")
      # Check for divisibility by 3.
    elif i % 3 == 0:
      result.append("fizz")
      # Check for divisibility by 5.
    elif i % 5 == 0:
      result.append("buzz")
      # If the number was not replaced by any of the above rules, append the number itself to the list.
    else:
      result.append(i)

  return result

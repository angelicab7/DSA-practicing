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
  result = []

  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      result.append("fizzbuzz")
    elif i % 3 == 0:
      result.append("fizz")
    elif i % 5 == 0:
      result.append("buzz")
    else:
      result.append(i)

  return result

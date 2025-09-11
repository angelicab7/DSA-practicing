'''
Write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements.

Complexity:
n = length of list
Time: O(n^2)
Space: O(n^2)
'''

def pairs(elements):
  # Initialize an empty list to store the pairs.
  result = []
# Outer loop to iterate through each element in the list.
  for i in range(0, len(elements)):
    #Inner loop to pair the current element (at index i) with all subsequent elements in the list.
    #We start at i + 1 to avoid duplicate pairs and pairing an element with itself.
    for j in range(i + 1, len(elements)):
      # Create a tuple representing the unique pair and add it to the list.
      pair = [ elements[i], elements[j] ]
      result.append(pair)
    
  return result

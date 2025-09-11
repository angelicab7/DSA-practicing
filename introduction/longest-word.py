'''
Write a function, longest_word, that takes in a sentence string as an argument. The function should return the longest word in the sentence. If there is a tie, return the word that occurs later in the sentence.

You can assume that the sentence is non-empty.

Complexity:
n = length of sentence
Time = 0(n)
Space = 0(n)
'''

def longest_word(sentence):
  # Split the sentence into a list of words.
  words = sentence.split(" ")
    # Initialize a variable to hold the longest word found so far.
  longest = ""

  # Iterates through each word in the list of words.
  for word in words:
    #Compares the length of the current word with the length of the longest word found so far.
    if len(word) >= len(longest):
    # assigns the longest word found
      longest = word

  return longest

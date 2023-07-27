import math

def find_largest_palindrome(words):
  largest = 0
  palindrome = ""

  for word in words:
    if word == word[::-1]:
      if len(word) > largest:
          palindrome = word
          largest = len(word)
    
  return palindrome if palindrome else None

find_largest_palindrome(["racecar", "level", "world", "hello"])
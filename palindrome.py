from math import floor

def is_palindrome(num1, num2):
  num = str(num1 * num2)
  str_len = len(num)
  for i in range(0, floor(str_len/2)):
    if num[i] != num[str_len - 1 - i]: return False

  return True

def biggest_palindrome_product_under_factor(factor, min_factor=0):
  for i in range(factor, 0, -1):
    if i < min_factor: return None
    if is_palindrome(i, i): return [i * i, i, i]
    if is_palindrome(i, i-1): return [i * (i-1), i, i-1]


biggest = biggest_palindrome_product_under_factor(999, 100)
print(biggest)
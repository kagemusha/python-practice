import unittest

def sum_multiples(limit):
  sum = 0
  for i in range(3, limit, 3):
    sum += i
  for i in range(5, limit, 5):
    if i % 15 != 0: sum += i
  return sum

def test():
  assert sum_multiples(10) == 23
  assert sum_multiples(20) == 78

test()

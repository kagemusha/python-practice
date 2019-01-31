a = 0
b = 0
c = 0
for k in range(499, 1, -1):
  for j in range(2, k - 2):
    i = 1000 - k - j
    if i**2 + j**2 == k**2:
      a = i
      b = j
      c = k
      break

assert a ** 2 + b ** 2 == c ** 2
assert a + b + c == 1000
print((a, b, c))
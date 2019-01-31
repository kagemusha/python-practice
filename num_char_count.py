counts = {
  0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
  10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 9, 19: 8,
  20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8,
  1000000: 7, 10000000: 7
}

def num_letter_count(num):
  if num < 21:
    return counts[num]
  letter_count = 0
  num_str = str(num)
  if int(num_str[-2:]) < 20: letter_count += counts[int(num_str[-2:])]
  else:
    letter_count += counts[int(num_str[-1])]
    letter_count += counts[int(num_str[-2]) * 10]
  if num > 99:
    letter_count += counts[int(num_str[-3])]
    letter_count += counts[100]
  if num > 999:
    letter_count += counts[int(num_str[-4])]
    letter_count += counts[1000]
  return letter_count

def count_nums(num):
  sum = 0
  for i in range(1,num+1):
    sum += num_letter_count(i)
  return sum

print(num_letter_count(3519))
print(len("threethousandfivehundrednineteen"))
assert num_letter_count(15) == len("fifteen")
assert num_letter_count(30) == len("thirty")
assert num_letter_count(154) == len("onehundredfiftyfour")
assert num_letter_count(3519) == len("threethousandfivehundrednineteen")

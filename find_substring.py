# questions
def is_sub(string, sub):
  if not string:
    return False
  if len(string) < len(sub):
    return False
  sublen = len(sub)
  for i in range(len(string) + 1 - sublen):
    if match(string[i:i+sublen], sub):
      return True
  return False

def match(str_a, str_b):
  for i in range(len(str_a)):
    if str_a[i] != str_b[i]:
      return False

  return True


assert is_sub("", "bce") == False
assert is_sub("a", "ab") == False
assert is_sub("aabbce", "bbe") == False
assert is_sub("aabbce", "bce") == True

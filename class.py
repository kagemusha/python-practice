class SomeClass():
  def __init__(self):
    self.a1 = None

class CWithAttrs():
  def __init__(self, a1):
    self.a1 = a1


ca1 = CWithAttrs("a1")
c1 = SomeClass()
c1.a1 = "kuma"

print(f"ca1.a1: {ca1.a1}")
print(f"c1.a1: {c1.a1}")
# print(f"c1.a1: {c1.b1}") #errors

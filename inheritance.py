print("inheritance")

class Base:
  def __init__(self):
    print("Base init")

class Child(Base):
  def __init__(self):
    print("Child init")


class SuperChild(Base):
  def __init__(self):
    super().__init__()
    print("Child init")

print("*** Create Base")
b = Base()

print("*** Create Child")
c = Child()

print("*** Create SuperChild")
s = SuperChild()

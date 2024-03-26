class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname1(self):
      print(self.firstname,self.lastname)
obj = Student("John", "Doe")
obj1 = Person("kavya","divya")
obj1.printname()
obj.printname1()


#inheritance method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):

  def printname1(self):
      print(self.firstname,self.lastname)
obj = Student("John", "Doe")
obj.printname1()
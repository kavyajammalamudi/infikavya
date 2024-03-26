class Student():
    designation = "software Engineer"
    def __init__ (self,name,age):
      self.name = name
      self.age = age

    @classmethod
    def new_test(cls):
        cls.designation = "Tester"
        print("This is from class method" + cls.designation)
    @staticmethod
    def add(a,b):
        return a+b
    def test(self):
        print("student name is " + self.name, "age is " + self.age, "Designation is " + self.designation)
obj = Student(" kavya "," 23 ")
obj2 = Student("kav","22")
obj2.test()
print(Student.designation)
obj.new_test()
print(Student.designation)
print(Student.add(5,5))

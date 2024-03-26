class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"  # Removed the extra space before {self.x},{self.y}

    def __repr__(self):
        return f"Point({self.x},{self.y})"

ob1 = Point(1, 2)
print(ob1)


class Test:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
obj=Test([1,2,3,4,5])
print(len(obj))


class Test:
    def __init__(self,data):
        self.data = data
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index]=value

obj = Test([1,2,3])
print(obj[0])
obj[1] = 5
print(obj[1])
print(obj.data)



class Number:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self):
        print(self.a + self.b)
    def __sub__(self):
        print(self.a - self.b)

num = Number(10,5)
print(num.__add__())
print(num.__sub__())
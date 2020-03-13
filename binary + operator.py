#to overload an binary + operator

class A:
    def __init__(self,a):
        self.a = a

    #addding two object
    def __add__(self,o):
        return self.a + o.a

ob1 = A(1)
ob2 = A(2)
ob3 = A("FY")
ob4 = A("IT")

print(ob1 + ob2)
print(ob3 + ob4)

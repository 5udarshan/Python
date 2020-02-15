#Finding The area of Ellipse
class Ellipse:
    
    def CalculateArea(self):
        print("Enter major axis:")
        self.s=float(input())
        print("Enter minor axis:")
        self.c=float(input())
        area= self.s * self.c
        print("Area of ellipse is = %f"%(area))

    def CalculatePerimeter(self):
        perimeter=2*3.14**(self.s + self.c/2)
        print("Perimeter of ellipse is =%f"%(perimeter))

obj_ellipse=Ellipse()
obj_ellipse.CalculateArea()
obj_ellipse.CalculatePerimeter()

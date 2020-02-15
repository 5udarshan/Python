#Code is use to Calculate Area of Circle
class Circle:

      def Calculate_Area(self):
            print("Enter radius:")
            self.s=float(input())
            area=3.14*self.s*self.s
            print("Area of Circle is=%f"%(area))
        
      def Calculate_Perimeter(self):
            perimeter=2*3.14*self.s
            print("Perimeter of Circle is=%f"%(perimeter))
            
obj_area=Circle()
obj_area.Calculate_Area()
obj_area.Calculate_Perimeter()

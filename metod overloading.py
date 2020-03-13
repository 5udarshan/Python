class GridPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return GridPoint(self.x + other.x + self.y + other.y)

    def __str__(self,other):
        string = str(self.x)
        string = string + " " + str(self.y)
        return string 

point1 = GridPoint(10,25)
point2 = GridPoint(-7,13)

point3 = point1 + point2

print(point3)

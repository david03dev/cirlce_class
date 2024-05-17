
class circle:
    pi = 3.141

    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        result = 2 * circle.pi * self.radius
        return result
    
    def area(self):
        result = circle.pi * pow(self.radius,2)
        return result
    
#main code
r = float(input("Enter the radius of circle: "))
cir = circle(r)
print("Radius of circle is : ", r)
print("Area of cirlce is : ",cir.area())
print("Perimeter of circle is : ",cir.perimeter())
from math import pi
class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
  
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)

class Circle:
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return pi * self.r ** 2
    def getPerimeter(self):
        return 2 * pi * self.r

circy = Circle(4.44)
# print(circy.getArea())
print(circy.getPerimeter())
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetr(sels):
        pass

class Reastangle(Figura):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimetr(self):
        return 2 * (self.width + self.height)
    
class Circle(Figura):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimetr(self):
        return 2 * 3.14 * self.radius

restangle = Reastangle(5, 8)
print(restangle.area())
print(restangle.perimetr())

circle = Circle(8)
print(circle.area())
print(circle.perimetr())
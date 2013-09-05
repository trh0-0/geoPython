#Tiffany Hall, 9/5/13, OCNG 689

#class is a data container
#Point.norm makes no sense cause its vague. p1.norm works
#dont over test things
#other is what is not self. self is p1, other is p2

from math import sqrt
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __repr__(self):
        print 'Point(%f, %f)' % (self.x, self.y)
        
    def __str__(self):                       #string
        return'(%f, %f)' % (self.x, self.y)  
        
    

p1 = Point(1.0, 2.0)
p2 = Point(3.0, 4.0)
print 'p1 = ' , p1.x, p1.y
print 'p2 = ' , p2.x, p2.y

print 'p1.norm() = ' , p1.norm()
print 'p2.norm() = ' , p2.norm()

print 'p1 + p2 = ', p1 + p2  #need the add def or it doesnt know how to do it



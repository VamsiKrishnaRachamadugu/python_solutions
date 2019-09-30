"""5.Your need to define the following two methods for the Coordinate class:

a) Add an eq method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

b) Define repr, a special method that returns a string that looks like a valid Python expression that could be used to
 recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of eq from part 1.

"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, a, b):
        return a == b

    def __repr__(self):
        return "'self.getX()== self.getY() '"


a = int(input("enter x coordinate:"))
b = int(input("enter y coordinate:"))
obj = Coordinate(a, b)
print(obj.__str__())
print(a == b)
print(eval(repr(obj)))

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
class Point:
    def __init__(self, x, y, line1, line2):
        self.x = x
        self.y = y
        self.intersectionLine1 = line1
        self.intersectionLine2 = line2
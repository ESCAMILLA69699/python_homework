import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    p1 = Point(13, 27)
    p2 = Point(46, 81)
    p3 = Point(13, 27)

    print(p1)
    print(p2)
    print(p1 == p3)
    print(p1 == p2)
    print(p1.euclidean_distance(p2))

    v1 = Vector(19, 34)
    v2 = Vector(57, 12)

    print(v1)
    print(v2)
    print(v1 + v2)
    print(v1 == v2)
    print(v1.euclidean_distance(v2))

class Point2d:
    """
    Represents a point in a 2d space
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
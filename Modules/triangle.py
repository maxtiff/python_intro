def area(base, height):
        '''(number, number) -> number

        Return the area of a triangle with dimensions
        base and height.

        >>> area (10, 5)
        25.0
        >>> area (2.5, 3)
        3.75

        '''
        
        return base * height / 2

def perimeter(side1, side2, side3):
        '''(number, number, number) -> number

        Return the perimeter of a triangle with sides
        1, 2 and 3.

        >>>perimeter(3, 4, 5)
        12
        >>>perimeter(10.5, 6, 9.3)
        25.8
        '''
        
        return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
        '''(number, number, number) -> float

        Return the semiperimeter of a triangle with sides of length side1, side2, and side3.
        
        >>>semiperimeter(3, 4, 5)
        6.0
        >>>semiperimeter(10.5, 6, 9.3)
        12.9
        '''
        
        return perimeter(side1, side2, side3) / 2



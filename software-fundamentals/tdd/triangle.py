"""
We're going to build a program that takes an input 
of three sides of a shape and tells you if it would 
make a valid triangle.

In a valid triangle, the sum of any two sides must be 
larger than the remaining side. 

For example, the triangle 5 10 25 is impossible, 
because 5 + 10 is not larger than 25.

We'll also keep a track of how many valid triangles 
we've been able to make
"""

def is_valid_triangle(side_1: int, side_2: int, side_3: int) -> bool:
    sorted_sides = sorted([side_1, side_2, side_3])
    return sorted_sides[2] < sorted_sides[0] + sorted_sides[1]

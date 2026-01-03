from math import sqrt
def circle_or_square(radius: float, area: float) -> bool:
    """Return True if circumference > square_perimeter."""
    circumference = 2 * 3.14 * radius
    side = sqrt(area)
    square_perimeter = 4 * side 
    return circumference > square_perimeter
print(circle_or_square(5,100))
from math import pi

def radians_to_degrees(rad: float) -> float:
    """Convert radians to degrees, rounded to 1 decimal place."""
    result = rad * 180/pi
    return round(result, 1)
print(radians_to_degrees(20))

def triangle_area(height, base):
    if height <= 0 or base <= 0:
        raise ValueError("The height and base must be greater than 0")
    return base * height *0.5

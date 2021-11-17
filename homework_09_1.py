def get_square_data(a: int) -> tuple[int, float]:
    """Calculate area of square, perimetr and diagonal"""
    area_square = a**2
    perimetr = a*4
    diagonal = (a**2*2)**(1/2)

    return (area_square, perimetr, float(f'{diagonal:.3f}'))


c = 0
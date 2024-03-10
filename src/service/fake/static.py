"""Pre-generated fake data to save on generating time"""
from typing import List


SUPPORTED_SQUARE_MATRIX_SIZES = [5, 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]


def get_square_matrix(size: int) -> List[List[int]]:
    """Get a square matrix of the given size."""
    if size not in SUPPORTED_SQUARE_MATRIX_SIZES:
        raise ValueError(f"Unsupported matrix size: {size}. Supported sizes: {SUPPORTED_SQUARE_MATRIX_SIZES}")
        
    matrix = []
    with open(f"src/service/fake/data/matrix{size}.txt", "r") as f:
        for line in f:
            row = [int(num) for num in line.strip().strip('[]').split(', ')]
            matrix.append(row)

    return matrix

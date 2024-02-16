from typing import List

from functools import reduce

import numpy as np

from src.types.bigmath import Matrix


def matmul(matrices: List[Matrix]) -> Matrix:
    """Return product of a list of matrices.
    
    Args:
        matrices: List[Matrix]
    """
    if matrices is None:
        return None
        
    p: np.array = reduce(np.matmul, matrices)
    return p.tolist()

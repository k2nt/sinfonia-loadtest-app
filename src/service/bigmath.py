from typing import List

from functools import reduce

import numpy as np

from src.types.bigmath import Matrix


def matmul(matrices: List[Matrix]) -> Matrix:
    """Return product of a list of matrices.
    
    Args:
        matrices: List[Matrix]
    """
    if not matrices:
        raise ValueError('empty input')
    
    for m in matrices:
        if not m:
            raise ValueError('empty matrix')
        
    p: np.array = reduce(np.matmul, matrices)
    return p.tolist()

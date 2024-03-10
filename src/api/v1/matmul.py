from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.lib.http import HTTPStatus

from src.types.maths import Matrix

from src.schema.base import (
    ResponseBase,
    ok_response,
)

import src.service as svc

from src.service import fake


router = APIRouter()


# class MatmulRequest(BaseModel):
#     """Contains two matrices."""
#     matrix_size: int


@router.get('/matmul', response_model=ResponseBase)
async def matmul(gen: bool = Query(..., title="Whether to generate the matrix"), sz: int = Query(..., title="Matrix size")):
    """Matrix multiplication."""        
    try:
        mtx = fake.static.get_square_matrix(sz) if gen else fake.maths.square_matrix(sz)
        p = svc.maths.matmul([mtx, mtx])
    except ValueError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=str(e),
            ) from e
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(e),
            ) from e
        
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=ok_response(data=p),
        )

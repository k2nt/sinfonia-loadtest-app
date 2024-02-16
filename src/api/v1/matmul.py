from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.lib.http import HTTPStatus

from src.types.bigmath import Matrix

from src.schema.base import (
    ResponseBase,
    ok_response,
)

import src.service as svc


router = APIRouter()


class MatricesRequest(BaseModel):
    """Contains two matrices."""
    matrix1: Matrix
    matrix2: Matrix


@router.post('/matmul', response_model=ResponseBase)
async def matmul(matrices: MatricesRequest):
    """Matrix multiplication."""
    try:
        p = svc.bigmath.matmul([matrices.matrix1, matrices.matrix2])
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

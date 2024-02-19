from fastapi import APIRouter

from .matmul import router as matmul_router


router = APIRouter(prefix='/api/v1')

router.include_router(matmul_router)

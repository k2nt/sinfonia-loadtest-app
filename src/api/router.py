from fastapi import APIRouter

from src.api.core.health import router as health_router
from src.api.v1.router import router as v1_router


router = APIRouter()

router.include_router(health_router, tags=['core'])
router.include_router(v1_router, tags=['v1'])

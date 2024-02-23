"""The so-called 'z-pages' for system heath checks."""
from fastapi import APIRouter

from src.schema.base import ok_response


router = APIRouter()


@router.get('/livez')
async def livez():
    """Liveness probe."""
    return ok_response('ok')


@router.get('/readyz')
async def readyz():
    """Readiness probe."""
    return ok_response('ok')

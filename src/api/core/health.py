"""The so-called 'z-pages' for system heath checks."""
from fastapi import APIRouter

from src.schema.base import ok_response


router = APIRouter()


@router.get('/livez')
async def get_livez():
    """Check system component health status."""
    return ok_response('ok')

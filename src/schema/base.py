from typing import Any, Dict, Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Base response schema."""
    message: Optional[str] = None
    data: Optional[Any] = None


def ok_response(
        message: Optional[str] = 'success',
        data: Optional[Any] = None,
) -> Dict:
    """Response builder.
    
    Args:
        message -- str: Response message [default: ' success']
        data -- Any: Data [default: None]
    
    Returns:
        Dict -- str: Response object
    """
    resp = ResponseBase(message=message, data=data)
    return resp.model_dump(exclude_defaults=True)

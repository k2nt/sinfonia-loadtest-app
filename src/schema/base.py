from typing import Dict, Optional

from http import HTTPStatus

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Base response schema."""
    status_code: int = ''
    message: Optional[str] = None
    data: Optional[Dict] = None
    error_message: Optional[str] = None
    error_trace: Optional[str] = None


def custom_response(
        status_code: int,
        message: Optional[str] = None,
        data: Optional[Dict] = None,
        error_message: Optional[str] = None,
        error_trace: Optional[str] = None,
) -> Dict:
    """Response builder.
    
    Args:
        status_code -- int: HTTP status code
        message -- str: Response message [default: None]
        error_message -- str: Error message [default: None]
        error_trace -- str: Error trace [default: None]
    
    Returns:
        Dict -- str: Response object
    """
    resp = ResponseBase(
        status_code=status_code,
        message=message,
        data=data,
        error_message=error_message,
        error_trace=error_trace,
        )

    return resp.model_dump(exclude_defaults=True)


def ok_response(
        message: Optional[str] = HTTPStatus.OK.phrase, 
        data: Optional[Dict] = None
) -> Dict:
    """Returns response with status code 200.
    
    Args:
        message -- str: Response message
        data -- str: Response data [default: None]
        
    Returns:
        Dict: Response object
    """
    return custom_response(HTTPStatus.OK.value, message, data)


def bad_request_response(
        message: Optional[str] = HTTPStatus.BAD_REQUEST.phrase,
        data: Optional[Dict] = None,
        error_message: Optional[str] = None,
        error_trace: Optional[str] = None,
) -> Dict:
    """Returns response with status code 400.
    
    Args:
        message -- str: Response message
        data -- str: Response data [default: None]
        
    Returns:
        Dict: Response object
    """
    return custom_response(
        HTTPStatus.BAD_REQUEST.value,
        message=message,
        data=data,
        error_message=error_message,
        error_trace=error_trace,
        )
    
    
def internal_server_error_response(
        message: Optional[str] = HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        data: Optional[Dict] = None,
        error_message: Optional[str] = None,
        error_trace: Optional[str] = None,
) -> Dict:
    """Returns response with status code 500.
    
    Args:
        message -- str: Response message
        data -- str: Response data [default: None]
        
    Returns:
        Dict: Response object
    """
    return custom_response(
        HTTPStatus.INTERNAL_SERVER_ERROR.value,
        message=message,
        data=data,
        error_message=error_message,
        error_trace=error_trace,
        )
    
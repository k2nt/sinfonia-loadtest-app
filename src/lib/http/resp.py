import requests
from src.lib.http import HTTPStatus  # Repurpose HTTPStatus from stanard library


def is_success_status_code(status_code: int) -> bool:
    return status_code >= 200 and status_code <= 299


def status_code_repr(code: int) -> str:
    """Return HTTP status code along with its descriptive phrase.
    
    Example:
        200 -> 200 OK
    
    Args:
        code -- int: HTTP status code
        
    Return:
        str -- Status code representation
    """
    return f"{str(code)} {HTTPStatus(code).phrase}"
    
    
def is_json_response(resp: requests.Response) -> bool:
    """Check if response is of JSON type. 
    
    Args:
        resp -- requests.Response: Response object
        
    Return:
        bool
    """
    try:
        _ = resp.json()
        return True
    except Exception:
        return False

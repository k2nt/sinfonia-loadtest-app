from pprint import PrettyPrinter


def json_repr(
        j: str,
        indent: int = 2,
        width: int = 90,
) -> str:
    """Prettify JSON string.
    
    Args:
        j -- str: JSON string
        indent -- int: Indent level (spaces) [default = 2]
        width -- int: Maximum line width (spaces) [default = 90]
        
    Return:
        str -- Prettified JSON string
    """    
    pp = PrettyPrinter(indent=indent, width=width)
    return pp.pformat(j)

"""
safe_division module - 防呆裝置 (Fool-proof device)

This module provides a safe division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divide two numbers with protection against division by zero.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a / b as a float
    
    Raises:
        ValueError: If b is zero (with a descriptive error message)
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(7, 3)
        2.3333333333333335
        >>> safe_division(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

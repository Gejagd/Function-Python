"""
Lesson 7 : Function
Computer Science class, Programing in Python
Program : simple division operation
"""

"""Library"""
import logging
import math
from enum import Enum
from typing import Tuple, Optional

"""Configure Logging"""
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

"""Error Code for Division Operations"""
class DivisionError(Enum):
    SUCCESS = 0
    DIVIDE_BY_ZERO = 1


def validate_input(a: int, b: int) -> Optional[DivisionError]:
    """
    Validate Value Before Division
    
    Pre-Condition:
    - Variable validated through condition
    
    Post-Condition:
    - Return Denominator must not be zero logs
    
    Args:
        a: Numerator
        b: Denominator

    Returns:
        DivisionError if invalid, None if valid
    """
    
    '''Pre-Condition'''
    if b == 0:
        '''Post-Condition'''
        logger.error("Division By Zero Attempted")
        return DivisionError.DIVIDE_BY_ZERO
    
    return None

def safe_divide(a: int, b: int) -> Tuple[Optional[int], DivisionError]:
    """
    Perform safe division with comprehensive error handling
    
    Pre-Conditions:
    - Input validation
    
    Post-Conditions:
    - Return of successful division result
    
    Args:
        a: Numerator (dividend)
        b: Denominator (divisor)
        
    Return:
        Tuple of (result, error_code)
        - If successful (float_value, DivisionError.SUCCESS)
        - IF error (None, DivisionError.xxx)
    """
    
    '''Pre-Condition: Validate Input'''
    logger.info(f'Dividing {a} by {b}')
    
    validation_error = validate_input(a, b)
    if validation_error is not None:
        return (None, validation_error)
    
    '''Perform Division'''
    try:
        result = a / b
    except ZeroDivisionError:
        logger.error(f'Unexpected ZeroDivisionError')
        return (None, DivisionError.DIVIDE_BY_ZERO)
    
    '''Post-Condition'''
    logger.info(f'Division Successful: {result}')
    return (result, DivisionError.SUCCESS)
    
if __name__ == '__main__':
    print("\nPlease Input A and B value")
    x_input = input("Value A: ")
    y_input = input("Value B: ")
    
    x = int(x_input)
    y = int(y_input)
    
    safe_divide(x, y)
    
"""
itentionally complex 😊
"""
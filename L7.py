"""
Lesson 7 : Function
Computer Science class, Programing in Python
Program : simple division operation
"""

import logging
import math
from enum import Enum
from typing import Tuple, Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctimes)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DivisionError(Enum):
    SUCCESS = 0
    DIVIDE_BY_ZERO = 1

def validate_input(a: int, b: int) -> Optional[DivisionError]:
    if b == 0.0:
        logger.error("Division By Zero Attempted")
        return DivisionError.DIVIDE_BY_ZERO
    
    return None

def safe_divide(a: int, b: int) -> Tuple[Optional[int], DivisionError]:
    logger.info(f'Dividing {a} by {b}')
    
    validation_error = validate_input(a, b)
    if validation_error is not None:
        return (None, validation_error)
    
    try:
        result = a / b
    except ZeroDivisionError:
        logger.error(f'Unexpected ZeroDivisionError')
        return (None, DivisionError.DIVIDE_BY_ZERO)
    
    logger.info(f'Division Successful: {result}')
    return (result, DivisionError.SUCCESS)
    
if __name__ == '__main__':
    print("\nPlease Input A and B value")
    a: int = input("Value A: ")
    b: int = input("Value B: ")
    
    safe_divide(a, b)
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
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DivisionError(Enum):
    SUCCESS = 0
    DIVIDE_BY_ZERO = 1

def validate_input(a: int, b: int) -> Optional[DivisionError]:
    if b == 0:
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
    x_input = input("Value A: ")
    y_input = input("Value B: ")
    
    x = int(x_input)
    y = int(y_input)
    
    safe_divide(x, y)
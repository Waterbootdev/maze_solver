from enum import Enum

class WALLINDEX(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

def opposite(wallindex:WALLINDEX)-> WALLINDEX:
    match wallindex:
        case WALLINDEX.TOP:
            return WALLINDEX.BOTTOM
        case WALLINDEX.BOTTOM:
            return WALLINDEX.TOP
        case WALLINDEX.LEFT:
            return WALLINDEX.RIGHT
        case WALLINDEX.RIGHT:
            return WALLINDEX.LEFT 

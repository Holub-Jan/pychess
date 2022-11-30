from enum import Enum


class PieceColor(Enum):
    WHITE = 'white'
    BLACK = 'black'


class PieceType(Enum):
    BISHOP = 'bishop'
    KING = 'king'
    KNIGHT = 'knight'
    PAWN = 'pawn'
    QUEEN = 'queen'
    ROOK = 'rook'

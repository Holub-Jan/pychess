import abc
from abc import abstractmethod

from gui.gui_widgets import GuiPiece
from model.enums import PieceColor, PieceType


class APiece(abc.ABC):
    def __init__(self, color: PieceColor, piece_type: PieceType):
        self.color = color
        self.piece_type = piece_type
        self._gui_element = GuiPiece(f"{self.color.value}_{self.piece_type.value}")

    def gui(self):
        return self._gui_element


# TODO - Rook, Knight, Bishop, Queen, King
class Pawn(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.PAWN)


class Rook(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.ROOK)


class Knight(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KNIGHT)


class Bishop(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.BISHOP)


class Queen(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.QUEEN)


class King(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KING)

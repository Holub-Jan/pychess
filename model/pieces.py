import abc
from abc import abstractmethod

from gui.gui_widgets import GuiPiece
from model.enums import PieceColor, PieceType


class APiece(abc.ABC):
    def __init__(self, color: PieceColor, piece_type: PieceType):
        self._color = color
        self._piece_type = piece_type
        self._gui_element = GuiPiece(f"{self._color.value}_{self._piece_type.value}")

    def gui(self):
        return self._gui_element

    @abstractmethod
    def moves(self):
        pass


# TODO - Rook, Knight, Bishop, Queen, King
class Pawn(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.PAWN)

    def moves(self):
        return ["A3", "A4"]


class Rook(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.ROOK)

    def moves(self):
        return ["A3", "A4"]


class Knight(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KNIGHT)

    def moves(self):
        return ["A3", "A4"]


class Bishop(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.BISHOP)

    def moves(self):
        return ["A3", "A4"]


class Queen(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.QUEEN)

    def moves(self):
        return ["A3", "A4"]


class King(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KING)

    def moves(self):
        return ["A3", "A4"]


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


class Pawn(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.PAWN)

    def moves(self):
        return ["A3", "A4"]

# TODO - Rook, Knight, Bishop, Queen, King

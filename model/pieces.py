import abc

from gui.gui_widgets import GuiPiece
from model.enums import PieceColor, PieceType


class APiece(abc.ABC):
    def __init__(self, color: PieceColor, piece_type: PieceType):
        self._color = color
        self._piece_type = piece_type
        self._gui_element = GuiPiece(f"{self._color.value}_{self._piece_type.value}")

    def gui(self):
        return self._gui_element


class Pawn(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.PAWN)


# TODO - Rook, Knight, Bishop, Queen, King

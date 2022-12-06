import abc
from abc import abstractmethod

from gui.gui_widgets import GuiPiece
from model.enums import PieceColor, PieceType
from game.rule_manager import RuleManager


class APiece(abc.ABC):
    def __init__(self, color: PieceColor, piece_type: PieceType):
        self._color = color
        self._piece_type = piece_type
        self._gui_element = GuiPiece(f"{self._color.value}_{self._piece_type.value}")

    def gui(self):
        return self._gui_element

    @abstractmethod
    def moves(self, x, y):
        pass


# TODO - Rook, Knight, Bishop, Queen, King
class Pawn(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.PAWN)

    def moves(self, x, y):
        print(self._color)
        if self._color == PieceColor.WHITE:
            return self._white_moves(x, y)
        return self._black_moves(x, y)

    def _white_moves(self, x, y):
        move_list = list()

        if x > 0:
            move_list.append((x - 1, y))

        return move_list

    def _black_moves(self, x, y):
        move_list = list()

        if x < 8:
            move_list.append((x + 1, y))

        return move_list


class Rook(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.ROOK)

    def moves(self, x, y):
        moves_list = list()

        for space in range(8):
            if space != x:
                moves_list.append((space, y))
            if space != y:
                moves_list.append((x, space))

        return moves_list


class Knight(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KNIGHT)

    def moves(self, x, y):
        return ["A3", "A4"]


class Bishop(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.BISHOP)

    def moves(self, x, y):
        return ["A3", "A4"]


class Queen(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.QUEEN)

    def moves(self, x, y):
        return ["A3", "A4"]


class King(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KING)

    def moves(self, x, y):
        return ["A3", "A4"]


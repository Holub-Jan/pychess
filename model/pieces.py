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

    @staticmethod
    def _white_moves(x, y):
        move_list = list()

        if x > 0:
            move_list.append((x - 1, y))

        return move_list

    @staticmethod
    def _black_moves(x, y):
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
        left = self._get_left(x, y)
        right = self._get_right(x, y)
        top = self._get_top(x, y)
        bottom = self._get_bottom(x, y)

        return top + bottom + left + right

    @staticmethod
    def _get_top(x, y):
        lst = list()
        if x > 0:
            if y < 6:
                lst.append((x - 1, y + 2))
            if y > 1:
                lst.append((x - 1, y - 2))

        return lst

    @staticmethod
    def _get_bottom(x, y):
        lst = list()
        if x < 7:
            if y < 6:
                lst.append((x + 1, y + 2))
            if y > 1:
                lst.append((x + 1, y - 2))

        return lst

    @staticmethod
    def _get_right(x, y):
        lst = list()
        if x < 7:
            if x < 6:
                lst.append((x + 2, y + 1))
            if x > 1:
                lst.append((x - 2, y + 1))

        return lst

    @staticmethod
    def _get_left(x, y):
        lst = list()
        if y > 0:
            if x > 1:
                lst.append((x - 2, y - 1))
            if x < 6:
                lst.append((x + 2, y - 1))

        return lst


class Bishop(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.BISHOP)

    def moves(self, x, y):
        top_left = self._get_top_left(x, y)
        top_right = self._get_top_right(x, y)
        bot_left = self._get_bottom_left(x, y)
        bot_right = self._get_bottom_right(x, y)

        return top_left + top_right + bot_right + bot_left

    @staticmethod
    def _get_top_left(x, y):
        lst = list()

        while x != 0 or y != 0:
            lst.append((x - 1, y - 1))
            x -= 1
            y -= 1

        return lst

    @staticmethod
    def _get_top_right(x, y):
        lst = list()

        while x != 0 or y != 7:
            lst.append((x - 1, y + 1))
            x -= 1
            y += 1

        return lst

    @staticmethod
    def _get_bottom_right(x, y):
        lst = list()

        while x != 7 or y != 7:
            lst.append((x + 1, y + 1))
            x += 1
            y += 1

        return lst

    @staticmethod
    def _get_bottom_left(x, y):
        lst = list()

        while x != 7 or y != 0:
            lst.append((x + 1, y - 1))
            x += 1
            y -= 1

        return lst


class Queen(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.QUEEN)

    def moves(self, x, y):
        horizontal = list()

        for space in range(8):
            if space != x:
                horizontal.append((space, y))
            if space != y:
                horizontal.append((x, space))

        top_left = self._get_top_left(x, y)
        top_right = self._get_top_right(x, y)
        bot_left = self._get_bottom_left(x, y)
        bot_right = self._get_bottom_right(x, y)

        return horizontal + top_left + top_right + bot_right + bot_left

    @staticmethod
    def _get_top_left(x, y):
        lst = list()

        while x != 0 or y != 0:
            lst.append((x - 1, y - 1))
            x -= 1
            y -= 1

        return lst

    @staticmethod
    def _get_top_right(x, y):
        lst = list()

        while x != 0 or y != 7:
            lst.append((x - 1, y + 1))
            x -= 1
            y += 1

        return lst

    @staticmethod
    def _get_bottom_right(x, y):
        lst = list()

        while x != 7 or y != 7:
            lst.append((x + 1, y + 1))
            x += 1
            y += 1

        return lst

    @staticmethod
    def _get_bottom_left(x, y):
        lst = list()

        while x != 7 or y != 0:
            lst.append((x + 1, y - 1))
            x += 1
            y -= 1

        return lst


class King(APiece):
    def __init__(self, color: PieceColor):
        super().__init__(color, PieceType.KING)

    def moves(self, x, y):
        move_list = list()

        if x > 0:
            if y > 0:
                # Top left
                move_list.append((x - 1, y - 1))

            # Left
            move_list.append((x - 1, y))

            if y < 7:
                # Top right
                move_list.append((x - 1, y + 1))

        if y < 7:
            # Right
            move_list.append((x, y + 1))

        if y > 0:
            # Left
            move_list.append((x, y - 1))

        if x < 7:
            if y > 0:
                # Bottom left
                move_list.append((x + 1, y - 1))

            # Bottom
            move_list.append((x + 1, y))

            if y < 7:
                # Bottom right
                move_list.append((x + 1, y + 1))

        return move_list


from model.enums import PieceType, PieceColor


class RuleManager:
    def __init__(self, board):
        self.board = board
        self.color = ''

    def legal_moves(self, piece, x, y):
        self.color = piece.color
        if piece.piece_type == PieceType.PAWN:
            moves = self._pawn_moves(x, y)
        elif piece.piece_type == PieceType.ROOK:
            moves = self._rook_moves(x, y)
        elif piece.piece_type == PieceType.KNIGHT:
            moves = self._knight_moves(x, y)
        elif piece.piece_type == PieceType.BISHOP:
            moves = self._bishop_moves(x, y)
        elif piece.piece_type == PieceType.QUEEN:
            moves = self._queen_moves(x, y)
        else:
            moves = self._king_moves(x, y)

        return moves

    def _pawn_moves(self, x, y):
        if self.color == PieceColor.WHITE:
            return self._white_pawn_moves(x, y)
        return self._black_pawn_moves(x, y)

    def _white_pawn_moves(self, x, y):
        move_list = list()

        if x > 0:
            if y > 0 and self.board[x - 1][y - 1] and self.board[x - 1][y - 1] != self.color:
                move_list.append((x - 1, y - 1))

            move_list.append((x - 1, y))

            if y < 7 and self.board[x - 1][y + 1] and self.board[x - 1][y - 1] != self.color:
                move_list.append((x - 1, y + 1))

        return move_list

    def _black_pawn_moves(self, x, y):
        move_list = list()

        if x < 8:
            if y > 0 and self.board[x + 1][y - 1] and self.board[x - 1][y - 1] != self.color:
                move_list.append((x + 1, y - 1))

            move_list.append((x + 1, y))

            if y < 7 and self.board[x + 1][y + 1] and self.board[x - 1][y - 1] != self.color:
                move_list.append((x + 1, y + 1))

        return move_list

    def _rook_moves(self, x, y):
        left = self._get_left(x, y)
        right = self._get_right(x, y)
        top = self._get_top(x, y)
        bot = self._get_bot(x, y)

        return left + right + top + bot

    def _get_left(self, x, y):
        lst = list()

        x -= 1
        while x >= 0 and not self.board[x][y]:
            lst.append((x, y))
            x -= 1

        if x > -1:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _get_right(self, x, y):
        lst = list()

        x += 1
        while x <= 7 and not self.board[x][y]:
            lst.append((x, y))
            x += 1

        if x < 8:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _get_bot(self, x, y):
        lst = list()

        y += 1
        while y <= 7 and not self.board[x][y]:
            lst.append((x, y))
            y += 1

        if y < 8:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _get_top(self, x, y):
        lst = list()

        y -= 1
        while y >= 0 and not self.board[x][y]:
            lst.append((x, y))
            y -= 1

        if y > - 1:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _knight_moves(self, x, y):
        left = self._get_knight_left(x, y)
        right = self._get_knight_right(x, y)
        top = self._get_knight_top(x, y)
        bottom = self._get_knight_bottom(x, y)

        return top + bottom + left + right

    def _get_knight_top(self, x, y):
        lst = list()
        if x > 0:
            if y < 6 and (not self.board[x - 1][y + 2] or self.board[x - 1][y + 2].color != self.color):
                lst.append((x - 1, y + 2))
            if y > 1 and (not self.board[x - 1][y - 2] or self.board[x - 1][y - 2].color != self.color):
                lst.append((x - 1, y - 2))
        return lst

    def _get_knight_bottom(self, x, y):
        lst = list()
        if x < 7:
            if y < 6 and (not self.board[x + 1][y + 2] or self.board[x + 1][y + 2].color != self.color):
                lst.append((x + 1, y + 2))
            if y > 1 and (not self.board[x - 1][y - 2] or self.board[x - 1][y - 2].color != self.color):
                lst.append((x + 1, y - 2))
        return lst

    def _get_knight_right(self, x, y):
        lst = list()
        if y < 7:
            if x < 6 and (not self.board[x + 2][y + 1] or self.board[x + 2][y + 1].color != self.color):
                lst.append((x + 2, y + 1))
            if x > 1 and (not self.board[x - 2][y + 1] or self.board[x - 2][y + 1].color != self.color):
                lst.append((x - 2, y + 1))
        return lst

    def _get_knight_left(self, x, y):
        lst = list()
        if y > 0:
            if x > 1 and (not self.board[x - 2][y - 1] or self.board[x - 2][y - 1].color != self.color):
                lst.append((x - 2, y - 1))
            if x < 6 and (not self.board[x + 2][y - 1] or self.board[x + 2][y - 1].color != self.color):
                lst.append((x + 2, y - 1))
        return lst

    def _bishop_moves(self, x, y):
        top_left = self._get_top_left(x, y)
        top_right = self._get_top_right(x, y)
        bot_left = self._get_bottom_left(x, y)
        bot_right = self._get_bottom_right(x, y)

        return top_left + top_right + bot_right + bot_left

    def _get_top_left(self, x, y):
        lst = list()

        x -= 1
        y -= 1
        while x >= 0 and y >= 0 and not self.board[x][y]:
            lst.append((x, y))
            x -= 1
            y -= 1

        if y >= 0 and x >= 0:
            if not self.board[x][y] and self.board[x][y].color == self.color:
                lst.append((x, y))

        return lst

    def _get_top_right(self, x, y):
        lst = list()

        x -= 1
        y += 1
        while x >= 0 and y <= 7 and not self.board[x][y]:
            lst.append((x, y))
            x -= 1
            y += 1

        if x >= 0 and y <= 7:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _get_bottom_right(self, x, y):
        lst = list()

        x += 1
        y += 1
        while x <= 7 and y <= 7 and not self.board[x][y]:
            lst.append((x, y))
            x += 1
            y += 1

        if x <= 7 and y <= 7:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _get_bottom_left(self, x, y):
        lst = list()

        x += 1
        y -= 1
        while x <= 7 and y >= 0 and not self.board[x][y]:
            lst.append((x, y))
            x += 1
            y -= 1

        if x <= 7 and y >= 0:
            if not self.board[x][y] and self.board[x][y].color != self.color:
                lst.append((x, y))

        return lst

    def _queen_moves(self, x, y):
        top_left = self._get_top_left(x, y)
        top_right = self._get_top_right(x, y)
        bot_left = self._get_bottom_left(x, y)
        bot_right = self._get_bottom_right(x, y)

        left = self._get_left(x, y)
        right = self._get_right(x, y)
        top = self._get_top(x, y)
        bot = self._get_bot(x, y)

        return left + right + top + bot + top_left + top_right + bot_right + bot_left

    # TODO : cognitive complexity high
    def _king_moves(self, x, y):
        move_list = list()

        if x > 0:
            if y > 0 and self.board[x - 1][y - 1].color != self.color:
                # Top left
                move_list.append((x - 1, y - 1))

            if self.board[x - 1][y].color != self.color:
                # Left
                move_list.append((x - 1, y))

            if y < 7 and self.board[x - 1][y + 1].color != self.color:
                # Top right
                move_list.append((x - 1, y + 1))

        if y < 7 and self.board[x][y + 1].color != self.color:
            # Right
            move_list.append((x, y + 1))

        if y > 0 and self.board[x][y - 1].color != self.color:
            # Left
            move_list.append((x, y - 1))

        if x < 7:
            if y > 0 and self.board[x + 1][y - 1].color != self.color:
                # Bottom left
                move_list.append((x + 1, y - 1))

            if self.board[x + 1][y].color != self.color:
                # Bottom
                move_list.append((x + 1, y))

            if y < 7 and self.board[x + 1][y + 1].color != self.color:
                # Bottom right
                move_list.append((x + 1, y + 1))

        return move_list


class RuleManager:
    def __init__(self, piece_type):
        self._piece_type = piece_type

    def get_moves(self, x, y):
        if self._piece_type == 'pawn':
            moves = self._pawn_moves(x, y)
        elif self._piece_type == 'rook':
            moves = self._rook_moves(x, y)
        elif self._piece_type == 'knight':
            moves = self._knight_moves(x, y)
        elif self._piece_type == 'bishop':
            moves = self._bishop_moves(x, y)
        elif self._piece_type == 'queen':
            moves = self._queen_moves(x, y)
        else:
            moves = self._king_moves(x, y)

        return moves

    def _pawn_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

    def _rook_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

    def _knight_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

    def _bishop_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

    def _queen_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

    def _king_moves(self, x, y):
        # From current position where can pawn go if the board is empty
        return []

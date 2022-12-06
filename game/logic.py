from model.enums import PieceColor
from model.pieces import Rook, Knight, Bishop, Queen, King, Pawn
from game.rule_manager import RuleManager


class Logic:
    def __init__(self):
        self.len_x = 8
        self.len_y = 8

        self.piece_list = list()
        self.taken_pieces = list()

        self._init_field_gen()
        self._selected_pos = tuple()
        self._legal_moves = list()

        self.rule_manager = RuleManager(self.piece_list)

    def _init_field_gen(self):

        for row in range(self.len_x):
            self.piece_list.append([])
            for col in range(self.len_y):
                if row == 0:
                    self._init_gen_royals_black(row, col)
                elif row == 1:
                    self.piece_list[row].append(Pawn(PieceColor.BLACK))
                elif row == 6:
                    self.piece_list[row].append(Pawn(PieceColor.WHITE))
                elif row == 7:
                    self._init_gen_royals_white(row, col)
                else:
                    self.piece_list[row].append(False)

    def _init_gen_royals_black(self, row, col):
        piece = False

        if col in [0, 7]:
            piece = Rook(PieceColor.BLACK)
        elif col in [1, 6]:
            piece = Knight(PieceColor.BLACK)
        elif col in [2, 5]:
            piece = Bishop(PieceColor.BLACK)
        elif col == 3:
            piece = Queen(PieceColor.BLACK)
        elif col == 4:
            piece = King(PieceColor.BLACK)

        self.piece_list[row].append(piece)

    def _init_gen_royals_white(self, row, col):
        piece = False

        if col in [0, 7]:
            piece = Rook(PieceColor.WHITE)
        elif col in [1, 6]:
            piece = Knight(PieceColor.WHITE)
        elif col in [2, 5]:
            piece = Bishop(PieceColor.WHITE)
        elif col == 3:
            piece = Queen(PieceColor.WHITE)
        elif col == 4:
            piece = King(PieceColor.WHITE)

        self.piece_list[row].append(piece)

    def get_piece_list(self):
        return self.piece_list

    # TODO : flipped by 90 clockwise,idk
    def move_piece(self, y, x):
        if self._selected_pos == ():
            if not self._tile_empty(x, y):
                self._selected_pos = (x, y)
                self._legal_moves = self.rule_manager.legal_moves(self.piece_list[x][y], x, y)

                if not self._legal_moves:
                    self._selected_pos = tuple()
                print(self._legal_moves)

        elif (x, y) in self._legal_moves:
            select_x = self._selected_pos[0]
            select_y = self._selected_pos[1]

            self.piece_list[x][y] = self.piece_list[select_x][select_y]
            self.piece_list[select_x][select_y] = False
            self._selected_pos = tuple()
            self._legal_moves = list()

    def _tile_empty(self, x, y):
        if not self.piece_list[x][y]:
            return True
        return False

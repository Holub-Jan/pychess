from model.enums import PieceColor
from model.pieces import Rook, Knight, Bishop, Queen, King, Pawn


class Logic:
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y

        self.piece_list = list()

        self._init_field_gen()

    def _init_field_gen(self):
        for row in range(self.len_x):
            self.piece_list.append([])
            if row in [0, 7]:
                if row == 0:
                    self.piece_list[row].append(Rook(PieceColor.BLACK))
                    self.piece_list[row].append(Knight(PieceColor.BLACK))
                    self.piece_list[row].append(Bishop(PieceColor.BLACK))
                    self.piece_list[row].append(Queen(PieceColor.BLACK))
                    self.piece_list[row].append(King(PieceColor.BLACK))
                    self.piece_list[row].append(Bishop(PieceColor.BLACK))
                    self.piece_list[row].append(Knight(PieceColor.BLACK))
                    self.piece_list[row].append(Rook(PieceColor.BLACK))
                else:
                    self.piece_list[row].append(Rook(PieceColor.WHITE))
                    self.piece_list[row].append(Knight(PieceColor.WHITE))
                    self.piece_list[row].append(Bishop(PieceColor.WHITE))
                    self.piece_list[row].append(Queen(PieceColor.WHITE))
                    self.piece_list[row].append(King(PieceColor.WHITE))
                    self.piece_list[row].append(Bishop(PieceColor.WHITE))
                    self.piece_list[row].append(Knight(PieceColor.WHITE))
                    self.piece_list[row].append(Rook(PieceColor.WHITE))
            else:
                for _ in range(self.len_y):
                    if row == 1:
                        self.piece_list[row].append(Pawn(PieceColor.BLACK))
                    elif row == 6:
                        self.piece_list[row].append(Pawn(PieceColor.WHITE))
                    else:
                        self.piece_list[row].append(False)

    def get_piece_list(self):
        return self.piece_list

    def move_piece(self, from_pos, to_pos):
        piece = self.piece_list[from_pos]
        self.piece_list.pop(from_pos)
        print(piece)
        self.piece_list[to_pos] = piece


class Logic:
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y

        self.piece_list = dict()

        self._init_field_gen()

    def _init_field_gen(self):
        for col in range(self.len_y):
            if col in [0, 7]:
                self.piece_list[0, col] = {'color': 'black', 'type': 'rook'}
                self.piece_list[7, col] = {'color': 'white', 'type': 'rook'}

            elif col in [1, 6]:
                self.piece_list[0, col] = {'color': 'black', 'type': 'knight'}
                self.piece_list[7, col] = {'color': 'white', 'type': 'knight'}

            elif col in [2, 5]:
                self.piece_list[0, col] = {'color': 'black', 'type': 'bishop'}
                self.piece_list[7, col] = {'color': 'white', 'type': 'bishop'}

            elif col == 3:
                self.piece_list[0, 3] = {'color': 'black', 'type': 'queen'}
                self.piece_list[7, 3] = {'color': 'white', 'type': 'queen'}
            elif col == 4:
                self.piece_list[0, 4] = {'color': 'black', 'type': 'king'}
                self.piece_list[7, 4] = {'color': 'white', 'type': 'king'}

            self.piece_list[1, col] = {'color': 'black', 'type': 'pawn'}
            self.piece_list[6, col] = {'color': 'white', 'type': 'pawn'}

    def get_piece_list(self):
        return self.piece_list


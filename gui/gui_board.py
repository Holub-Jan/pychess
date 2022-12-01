from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QMainWindow

from gui.gui_widgets import GuiTile, GuiLabel
from game.logic import Logic
from model.enums import PieceColor
from model.pieces import Pawn, Rook, Knight, Bishop, Queen, King


class GuiChessBoard(QWidget):
    axis_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    axis_y = range(8, 0, -1)

    # TODO
    def __init__(self):
        super().__init__()
        # init chess tiles
        self.logic = Logic(len(self.axis_y), len(self.axis_y))
        self._chess_tiles = [
            [GuiTile(x, y, self.tile_clicked) for x in range(len(self.axis_x))]
            for y in range(len(self.axis_y))]
        self._layout = QGridLayout()
        # render content
        self._render()

    def _render(self):
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        for i in range(len(self.axis_x)):
            self._layout.addWidget(GuiLabel(self.axis_y[i]), i, 0)
            for j in range(len(self.axis_y)):
                self._layout.addWidget(self._chess_tiles[i][j], i, j + 1)

        label_x_row = len(self.axis_x) + 1
        self._layout.addWidget(GuiLabel(""), label_x_row, 0)
        for i in range(len(self.axis_x)):
            self._layout.addWidget(GuiLabel(self.axis_x[i]), label_x_row, i + 1)
        self.setLayout(self._layout)

    # Example of game init
    def init_game(self):
        self._load_board()

    def _load_board(self):
        piece_list = self.logic.get_piece_list()

        for x in range(len(self.axis_x)):
            for y in range(len(self.axis_y)):
                tile = self._chess_tiles[x][y]

                if (x, y) not in piece_list:
                    tile.clear()
                else:
                    piece_type = piece_list[x, y]['type']
                    piece_color = piece_list[x, y]['color']

                    self._load_by_type(x, y, piece_type, piece_color)

    def _load_by_type(self, x, y, piece_type, piece_color):
        if piece_type == 'pawn':
            self._set_pawn(x, y, piece_color)

        elif piece_type == 'rook':
            self._set_rook(x, y, piece_color)

        elif piece_type == 'knight':
            self._set_knight(x, y, piece_color)

        elif piece_type == 'bishop':
            self._set_bishop(x, y, piece_color)

        elif piece_type == 'queen':
            self._set_queen(x, y, piece_color)

        elif piece_type == 'king':
            self._set_king(x, y, piece_color)

    def _set_pawn(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            pawn = Pawn(PieceColor.WHITE)
        else:
            pawn = Pawn(PieceColor.BLACK)

        tile.set_piece(pawn.gui())

    def _set_rook(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            rook = Rook(PieceColor.WHITE)
        else:
            rook = Rook(PieceColor.BLACK)

        tile.set_piece(rook.gui())

    def _set_knight(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            knight = Knight(PieceColor.WHITE)
        else:
            knight = Knight(PieceColor.BLACK)

        tile.set_piece(knight.gui())

    def _set_bishop(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            bishop = Bishop(PieceColor.WHITE)
        else:
            bishop = Bishop(PieceColor.BLACK)

        tile.set_piece(bishop.gui())

    def _set_queen(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            queen = Queen(PieceColor.WHITE)
        else:
            queen = Queen(PieceColor.BLACK)

        tile.set_piece(queen.gui())

    def _set_king(self, x, y, color):
        tile = self._chess_tiles[x][y]
        tile.clear()

        if color == 'white':
            king = King(PieceColor.WHITE)
        else:
            king = King(PieceColor.BLACK)

        tile.set_piece(king.gui())

    def tile_clicked(self, x, y):
        print(f"You clicked on tile {self.axis_x[x]}{self.axis_y[y]}")


class ChessGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.chess_board = GuiChessBoard()
        self.setWindowTitle("PyChess")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.chess_board)
        win = QWidget()
        win.setLayout(layout)
        self.setCentralWidget(win)

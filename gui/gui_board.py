from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QMainWindow

from gui.gui_widgets import GuiTile, GuiLabel
from model.enums import PieceColor
from model.pieces import Pawn, Rook, Knight, Bishop, Queen, King


class GuiChessBoard(QWidget):
    axis_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    axis_y = range(8, 0, -1)

    # TODO
    def __init__(self):
        super().__init__()
        # init chess tiles
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

    def tile_clicked(self, x, y):
        print(f"You clicked on tile {self.axis_x[x]}{self.axis_y[y]}")

    # Example of game init
    def init_game(self):
        self.init_pieces_set()

    def init_pieces_set(self):
        self.init_piece_set_pawns()
        self.init_piece_set_rooks()
        self.init_piece_set_knights()
        self.init_piece_set_bishops()
        self.init_piece_set_royal()

    def init_piece_set_pawns(self):
        # White
        for i in range(len(self.axis_x)):
            tile = self._chess_tiles[6][i]
            tile.clear()
            w_pawn = Pawn(PieceColor.WHITE)
            tile.set_piece(w_pawn.gui())
        # Black
        for i in range(len(self.axis_x)):
            tile = self._chess_tiles[1][i]
            tile.clear()
            b_pawn = Pawn(PieceColor.BLACK)
            tile.set_piece(b_pawn.gui())

    def init_piece_set_rooks(self):
        # White
        for i in [0, 7]:
            tile = self._chess_tiles[7][i]
            tile.clear()
            w_rook = Rook(PieceColor.WHITE)
            tile.set_piece(w_rook.gui())

        # Black
        for i in [0, 7]:
            tile = self._chess_tiles[0][i]
            tile.clear()
            b_rook = Rook(PieceColor.BLACK)
            tile.set_piece(b_rook.gui())

    def init_piece_set_knights(self):
        # White
        for i in [1, 6]:
            tile = self._chess_tiles[7][i]
            tile.clear()
            w_knight = Knight(PieceColor.WHITE)
            tile.set_piece(w_knight.gui())

        # Black
        for i in [1, 6]:
            tile = self._chess_tiles[0][i]
            tile.clear()
            b_knight = Knight(PieceColor.BLACK)
            tile.set_piece(b_knight.gui())

    def init_piece_set_bishops(self):
        # White
        for i in [2, 5]:
            tile = self._chess_tiles[7][i]
            tile.clear()
            w_bishop = Bishop(PieceColor.WHITE)
            tile.set_piece(w_bishop.gui())

        # Black
        for i in [2, 5]:
            tile = self._chess_tiles[0][i]
            tile.clear()
            b_bishop = Bishop(PieceColor.BLACK)
            tile.set_piece(b_bishop.gui())

    def init_piece_set_royal(self):
        # White
        tile = self._chess_tiles[7][3]
        tile.clear()
        w_queen = Queen(PieceColor.WHITE)
        tile.set_piece(w_queen.gui())

        tile = self._chess_tiles[7][4]
        tile.clear()
        w_king = King(PieceColor.WHITE)
        tile.set_piece(w_king.gui())

        # Black
        tile = self._chess_tiles[0][3]
        tile.clear()
        b_queen = Queen(PieceColor.BLACK)
        tile.set_piece(b_queen.gui())

        tile = self._chess_tiles[0][4]
        tile.clear()
        b_king = King(PieceColor.BLACK)
        tile.set_piece(b_king.gui())


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

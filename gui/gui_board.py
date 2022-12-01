from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QMainWindow

from gui.gui_widgets import GuiTile, GuiLabel, GuiWidget
from model.enums import PieceColor
from model.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from game.logic import Logic



class GuiChessBoard(GuiWidget):
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
        
        self.from_pos = tuple()

    def _get_stylesheet(self) -> str:
        return ''

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
                tile.clear()
                if piece_list[x][y]:
                    piece = piece_list[x][y]
                    tile.clear()
                    tile.set_piece(piece.gui())

    def tile_clicked(self, x, y):
        print(x, y)
        if self.from_pos == ():
            self.from_pos = (x, y)
        elif self.from_pos != (x, y):
            self.logic.move_piece(self.from_pos, (x, y))
            self.from_pos = tuple()
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

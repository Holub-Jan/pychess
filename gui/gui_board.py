from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QMainWindow

from gui.gui_widgets import GuiTile, GuiLabel, GuiWidget
from model.enums import PieceColor
from model.pieces import Pawn


class GuiChessBoard(GuiWidget):
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

    def tile_clicked(self, x, y):
        print(f"You clicked on tile {self.axis_x[x]}{self.axis_y[y]}")

    # Example of game init
    def init_game(self):
        for i in range(len(self.axis_x)):
            tile = self._chess_tiles[1][i]
            tile.clear()
            if i % 4 == 0:
                tile.set_selected(True)
            w_pawn = Pawn(PieceColor.WHITE)
            tile.set_piece(w_pawn.gui())
        for i in range(len(self.axis_x)):
            tile = self._chess_tiles[6][i]
            tile.clear()
            b_pawn = Pawn(PieceColor.BLACK)
            tile.set_piece(b_pawn.gui())


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

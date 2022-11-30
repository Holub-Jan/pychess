from typing import Callable

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class GuiLabel(QWidget):
    def __init__(self, text):
        super().__init__()
        self._text = text
        # create layout and widgets
        self._layout = QVBoxLayout()
        self._label = QLabel(f" {self._text} ")
        # render content
        self._render()

    def _render(self):
        self._label.setAlignment(Qt.AlignCenter)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.addWidget(self._label)
        self.setStyleSheet('background-color: rgba(0,0,0); color: white;')
        self.setLayout(self._layout)


class GuiPiece(QWidget):
    def __init__(self, img_name):
        super().__init__()
        self._img_name = img_name
        # create layout and widgets
        self._layout = QVBoxLayout()
        self._label = QLabel()
        self._pic = QPixmap(f"assets/images/{self._img_name}.png")
        # render content
        self._render()

    def _render(self):
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._label.setPixmap(self._pic)
        self._label.setFixedSize(64, 64)
        self._layout.addWidget(self._label)
        self.setLayout(self._layout)


class GuiTile(QWidget):

    __index = 0

    def __init__(self, x: int, y: int, on_click: Callable):
        super().__init__()
        self.x = x
        self.y = y
        # create layout and widgets
        self._layout = QVBoxLayout()
        self._piece_widget = QWidget()
        # render content
        self._render()
        # update counter of instances
        GuiTile.__index += 1
        # register event
        self.mouseReleaseEvent = lambda event: on_click(self.x, self.y)

    def _render(self):
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.addWidget(self._piece_widget)
        self.setStyleSheet(f"background-color: {self._get_background()}; "
                           f"border: 1px solid #000;")
        self.setFixedSize(64, 64)
        self.setLayout(self._layout)

    def set_piece(self, piece: GuiPiece):
        self._layout.removeWidget(self._piece_widget)
        self._piece_widget = piece
        self._layout.addWidget(self._piece_widget)

    def clear(self):
        self._layout.removeWidget(self._piece_widget)
        self._piece_widget = QWidget()
        self._layout.addWidget(self._piece_widget)

    @staticmethod
    def _get_background():
        i = 0 if int(GuiTile.__index / 8) % 2 == 0 else 1
        return 'white' if GuiTile.__index % 2 == i else 'grey'

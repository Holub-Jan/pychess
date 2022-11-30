import sys
from PyQt5.QtWidgets import QApplication

from gui.gui_board import ChessGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ChessGUI()
    # example of interaction with GUI
    win.chess_board.init_game()
    
    win.show()
    sys.exit(app.exec_())

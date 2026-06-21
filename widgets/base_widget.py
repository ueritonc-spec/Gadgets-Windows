from PySide6.QtWidgets import QWidget

from PySide6.QtCore import (
    Qt,
    QPoint
)

from core.settings import (
    set_widget_position
)


class BaseWidget(QWidget):

    def __init__(self):
        super().__init__()

        # =====================================
        # WINDOW FLAGS
        # =====================================

        self.setWindowFlags(

            Qt.FramelessWindowHint
            |
            Qt.WindowStaysOnTopHint
            |
            Qt.Tool
        )

        # =====================================
        # TRANSPARENT
        # =====================================

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        # =====================================
        # DRAG
        # =====================================

        self.drag_position = QPoint()

        self.widget_name = ""

    # =====================================
    # MOUSE PRESS
    # =====================================

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.drag_position = (

                event.globalPosition().toPoint()

                -

                self.frameGeometry().topLeft()
            )

            event.accept()

    # =====================================
    # MOUSE MOVE
    # =====================================

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:

            self.move(

                event.globalPosition().toPoint()

                -

                self.drag_position
            )

            event.accept()

    # =====================================
    # MOUSE RELEASE
    # =====================================

    def mouseReleaseEvent(self, event):

        try:

            set_widget_position(

                self.widget_name,

                self.x(),

                self.y()
            )

        except:

            pass
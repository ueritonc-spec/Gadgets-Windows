from PySide6.QtWidgets import QWidget

from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont,
    QConicalGradient
)

from PySide6.QtCore import (
    Qt,
    QRectF
)

from themes.config import ThemeConfig


class CircularProgress(QWidget):

    def __init__(self, color=QColor(0,170,255)):
        super().__init__()

        self.value = 0
        self.color = color

        size = int(160 * ThemeConfig.UI_SCALE)

        self.setFixedSize(size, size)

    def set_value(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):

        width = self.width()
        height = self.height()

        margin = int(14 * ThemeConfig.UI_SCALE)

        rect = QRectF(
            margin,
            margin,
            width - margin * 2,
            height - margin * 2
        )

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        # FUNDO

        bg_pen = QPen(
            QColor(35,35,35)
        )

        bg_pen.setWidth(
            int(12 * ThemeConfig.UI_SCALE)
        )

        painter.setPen(bg_pen)

        painter.drawArc(
            rect,
            0,
            360 * 16
        )

        # GRADIENTE

        gradient = QConicalGradient()

        gradient.setCenter(
            rect.center()
        )

        gradient.setAngle(-90)

        gradient.setColorAt(
            0.0,
            QColor(0,220,255)
        )

        gradient.setColorAt(
            1.0,
            QColor(0,120,255)
        )

        progress_pen = QPen()

        progress_pen.setBrush(gradient)

        progress_pen.setWidth(
            int(12 * ThemeConfig.UI_SCALE)
        )

        progress_pen.setCapStyle(
            Qt.RoundCap
        )

        painter.setPen(progress_pen)

        span = int(
            -360 * 16 * (
                self.value / 100
            )
        )

        painter.drawArc(
            rect,
            90 * 16,
            span
        )

        # TEXTO

        painter.setPen(Qt.white)

        font = QFont()

        font.setPointSize(
            int(28 * ThemeConfig.UI_SCALE)
        )

        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            f"{int(self.value)}%"
        )
from themes.config import ThemeConfig
from PySide6.QtWidgets import QWidget

from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QPainterPath,
    QLinearGradient,
    QBrush
)

from PySide6.QtCore import Qt

from themes.config import ThemeConfig


class HistoryGraph(QWidget):

    def __init__(self, color=QColor(0,170,255)):
        super().__init__()

        self.values = []

        self.color = color

        self.setMinimumHeight(
            int(90 * ThemeConfig.UI_SCALE)
        )

    def add_value(self, value):

        self.values.append(value)

        if len(self.values) > 60:
            self.values.pop(0)

        self.update()

    def paintEvent(self, event):

        if len(self.values) < 2:
            return

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        width = self.width()
        height = self.height()

        bottom_padding = int(
            10 * ThemeConfig.UI_SCALE
        )

        # GRID

        grid_pen = QPen(
            QColor(255,255,255,20)
        )

        painter.setPen(grid_pen)

        for i in range(5):

            y = int(height / 4 * i)

            painter.drawLine(
                0,
                y,
                width,
                y
            )

        # PATH

        path = QPainterPath()

        step_x = width / (
            len(self.values) - 1
        )

        points = []

        for i, value in enumerate(self.values):

            x = i * step_x

            visual_value = max(
                value * 3,
                8
            )

            if visual_value > 100:
                visual_value = 100

            y = (
                height - bottom_padding
            ) - (
                (visual_value / 100)
                * height
            )

            points.append((x, y))

        first_x, first_y = points[0]

        path.moveTo(first_x, first_y)

        for i in range(1, len(points)):

            prev_x, prev_y = points[i - 1]

            x, y = points[i]

            mid_x = (prev_x + x) / 2

            path.cubicTo(
                mid_x,
                prev_y,
                mid_x,
                y,
                x,
                y
            )

        # AREA

        fill_path = QPainterPath(path)

        fill_path.lineTo(
            width,
            height
        )

        fill_path.lineTo(
            0,
            height
        )

        fill_path.closeSubpath()

        gradient = QLinearGradient(
            0,
            0,
            0,
            height
        )

        gradient.setColorAt(
            0.0,
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                120
            )
        )

        gradient.setColorAt(
            1.0,
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                0
            )
        )

        painter.fillPath(
            fill_path,
            QBrush(gradient)
        )

        # GLOW

        glow_pen = QPen(
            QColor(
                self.color.red(),
                self.color.green(),
                self.color.blue(),
                80
            )
        )

        glow_pen.setWidth(
            int(8 * ThemeConfig.UI_SCALE)
        )

        painter.setPen(glow_pen)

        painter.drawPath(path)

        # LINHA

        line_gradient = QLinearGradient(
            0,
            0,
            width,
            0
        )

        line_gradient.setColorAt(
            0,
            QColor(0,220,255)
        )

        line_gradient.setColorAt(
            1,
            QColor(0,120,255)
        )

        line_pen = QPen(
            QBrush(line_gradient),
            int(3 * ThemeConfig.UI_SCALE)
        )

        line_pen.setCapStyle(
            Qt.RoundCap
        )

        painter.setPen(line_pen)

        painter.drawPath(path)
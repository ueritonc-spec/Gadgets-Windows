from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)

from PySide6.QtGui import QColor

from widgets.base_widget import BaseWidget
from widgets.circular_progress import CircularProgress
from widgets.history_graph import HistoryGraph

from themes.config import ThemeConfig


class BaseMonitorWidget(BaseWidget):

    def __init__(
        self,
        title,
        color
    ):
        super().__init__()

        self.color = color

        self.resize(
            self.s(420),
            self.s(390)
        )

        self.container = QFrame()

        self.container.setObjectName(
            "container"
        )

        self.title = QLabel(title)

        self.title.setStyleSheet(f"""
            font-size: {self.s(28)}px;
            font-weight: bold;
            color: white;
        """)

        self.subtitle = QLabel(
            "Loading..."
        )

        self.subtitle.setWordWrap(True)

        self.subtitle.setStyleSheet(f"""
            font-size:{self.s(14)}px;
            color: rgba(255,255,255,180);
        """)

        self.circle = CircularProgress(
            QColor(*color)
        )

        self.graph = HistoryGraph(
            QColor(*color)
        )

        self.info_layout = QVBoxLayout()

        self.info_layout.setSpacing(
            self.s(10)
        )

        center_layout = QHBoxLayout()

        center_layout.setSpacing(
            self.s(20)
        )

        center_layout.addWidget(
            self.circle
        )

        center_layout.addLayout(
            self.info_layout
        )

        layout = QVBoxLayout()

        layout.setContentsMargins(
            self.s(20),
            self.s(15),
            self.s(20),
            self.s(20)
        )

        layout.setSpacing(
            self.s(10)
        )

        layout.addWidget(self.title)

        layout.addWidget(
            self.subtitle
        )

        layout.addSpacing(
            self.s(5)
        )

        layout.addLayout(center_layout)

        layout.addSpacing(
            self.s(5)
        )

        layout.addWidget(self.graph)

        self.container.setLayout(layout)

        root = QVBoxLayout()

        root.setContentsMargins(
            self.s(10),
            self.s(10),
            self.s(10),
            self.s(10)
        )

        root.addWidget(self.container)

        self.setLayout(root)

        r, g, b = color

        self.setStyleSheet(f"""

            #container{{
                background:qlineargradient(
                    x1:0,
                    y1:0,
                    x2:1,
                    y2:1,
                    stop:0 rgba(8,15,30,240),
                    stop:1 rgba(3,8,18,240)
                );

                border-radius:{self.s(25)}px;

                border: 1px solid rgba({r},{g},{b},150);
            }}

            QLabel{{
                background: transparent;
                color:white;
            }}

        """)

    def s(self, value):
        return int(
            value * ThemeConfig.UI_SCALE
        )

    def create_info_card(
        self,
        title,
        value
    ):

        r, g, b = self.color

        frame = QFrame()

        frame.setObjectName("infoCard")

        frame.setFixedSize(
            self.s(170),
            self.s(65)
        )

        frame.setStyleSheet(f"""

            #infoCard{{
                background-color:
                    rgba(20,25,45,200);

                border-radius:{self.s(18)}px;

                border: 1px solid
                    rgba({r},{g},{b},100);
            }}

        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(
            self.s(15),
            self.s(8),
            self.s(15),
            self.s(8)
        )

        layout.setSpacing(2)

        label_title = QLabel(title)

        label_title.setStyleSheet(f"""
            font-size:{self.s(14)}px;
            color: rgba(255,255,255,180);
        """)

        label_value = QLabel(value)

        label_value.setStyleSheet(f"""
            font-size:{self.s(16)}px;
            font-weight:bold;
            color: rgb({r},{g},{b});
        """)

        frame.value_label = label_value

        layout.addWidget(label_title)

        layout.addWidget(label_value)

        frame.setLayout(layout)

        self.info_layout.addWidget(frame)

        return frame
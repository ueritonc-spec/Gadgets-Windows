from PySide6.QtCore import QTimer

from widgets.base_monitor_widget import (
    BaseMonitorWidget
)

from core.ram import (
    get_ram_usage,
    get_ram_total
)


class RAMWidget(BaseMonitorWidget):

    def __init__(self):

        super().__init__(
            "Memoria Ram",
            (0,255,170)
        )

        self.subtitle.setText(
            "Memória do Sistema"
        )

        self.total = self.create_info_card(
            "Total",
            "-- GB"
        )

        self.used = self.create_info_card(
            "Uso",
            "-- %"
        )

        self.available = self.create_info_card(
            "Disponível",
            "-- GB"
        )

        # TIMER
        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_info
        )

        self.timer.start(500)

        self.update_info()

    # =========================
    # UPDATE
    # =========================

    def update_info(self):

        ram = get_ram_usage()

        total = get_ram_total()

        available = round(
            total * (1 - ram / 100),
            1
        )

        # círculo
        self.circle.set_value(ram)

        # gráfico
        self.graph.add_value(ram)

        # cards
        self.total.value_label.setText(
            f"{total} GB"
        )

        self.used.value_label.setText(
            f"{ram}%"
        )

        self.available.value_label.setText(
            f"{available} GB"
        )
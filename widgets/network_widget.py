from PySide6.QtCore import QTimer

from widgets.base_monitor_widget import (
    BaseMonitorWidget
)

from core.network import (
    get_network_usage
)


class NetworkWidget(
    BaseMonitorWidget
):

    def __init__(self):

        super().__init__(
            "Rede",
            (180,0,255)
        )

        self.subtitle.setText(
            "Tráfego de rede"
        )

        self.download = self.create_info_card(
            "Download",
            "-- MB/s"
        )

        self.upload = self.create_info_card(
            "Upload",
            "-- MB/s"
        )

        self.status = self.create_info_card(
            "Status",
            "Online"
        )

        # =====================
        # TIMER MAIS RÁPIDO
        # =====================

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_info
        )

        # 250ms
        self.timer.start(250)

        self.update_info()

    # =========================
    # UPDATE
    # =========================

    def update_info(self):

        data = get_network_usage()

        usage = data["usage"]

        # círculo
        self.circle.set_value(usage)

        # gráfico
        self.graph.add_value(usage)

        # cards
        self.download.value_label.setText(
            f"{data['download']:.2f} MB/s"
        )

        self.upload.value_label.setText(
            f"{data['upload']:.2f} MB/s"
        )

        self.status.value_label.setText(
            "Online"
        )
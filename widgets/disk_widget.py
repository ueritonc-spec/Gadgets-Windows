from PySide6.QtCore import QTimer

from widgets.base_monitor_widget import (
    BaseMonitorWidget
)

from core.disk import (
    get_disk_usage,
    get_disk_total,
    get_disk_free
)


class DiskWidget(
    BaseMonitorWidget
):

    def __init__(self):

        super().__init__(
            "Disco",
            (255,60,60)
        )

        self.subtitle.setText(
            "Uso do armazenamento"
        )

        self.total = self.create_info_card(
            "Total",
            "-- GB"
        )

        self.used = self.create_info_card(
            "Uso",
            "-- %"
        )

        self.free = self.create_info_card(
            "Livre",
            "-- GB"
        )

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_info
        )

        self.timer.start(1000)

        self.update_info()

    def update_info(self):

        try:

            usage = get_disk_usage()

            total = get_disk_total()

            free = get_disk_free()

            self.circle.set_value(usage)

            self.graph.add_value(usage)

            self.total.value_label.setText(
                f"{total} GB"
            )

            self.used.value_label.setText(
                f"{usage}%"
            )

            self.free.value_label.setText(
                f"{free} GB"
            )

        except Exception as e:

            print("Erro Widget DISK:", e)
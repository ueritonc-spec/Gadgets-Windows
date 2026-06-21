from PySide6.QtCore import QTimer

from widgets.base_monitor_widget import (
    BaseMonitorWidget
)

from core.cpu import (
    get_cpu_usage,
    get_cpu_name,
    get_cpu_frequency,
    get_cpu_cores,
    get_cpu_threads
)


class CPUWidget(BaseMonitorWidget):

    def __init__(self):

        super().__init__(
            "Processador",
            (0,170,255)
        )

        # subtitulo
        self.subtitle.setText(
            get_cpu_name()
        )

        # cards
        self.freq = self.create_info_card(
            "Frequência",
            "-- GHz"
        )

        self.cores = self.create_info_card(
            "Núcleos",
            "--"
        )

        self.threads = self.create_info_card(
            "Threads",
            "--"
        )

        # timer
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

        cpu = get_cpu_usage()

        freq = get_cpu_frequency()

        cores = get_cpu_cores()

        threads = get_cpu_threads()

        # círculo
        self.circle.set_value(cpu)

        # gráfico
        self.graph.add_value(cpu)

        # cards
        self.freq.value_label.setText(
            f"{freq} GHz"
        )

        self.cores.value_label.setText(
            str(cores)
        )

        self.threads.value_label.setText(
            str(threads)
        )
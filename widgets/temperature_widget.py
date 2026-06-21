from PySide6.QtCore import QTimer, QThread, Signal

from widgets.base_monitor_widget import (
    BaseMonitorWidget
)

from core.temperature import (
    get_cpu_temperature
)


# =========================================
# WORKER THREAD (faz o pedido HTTP)
# =========================================

class TemperatureWorker(QThread):

    result = Signal(float)

    def run(self):

        temp = get_cpu_temperature()

        self.result.emit(temp)


# =========================================
# WIDGET
# =========================================

class TemperatureWidget(BaseMonitorWidget):

    def __init__(self):

        super().__init__(
            "Temperatura CPU",
            (255, 120, 0)
        )

        self.subtitle.setText(
            "CPU Temperature"
        )

        # =====================
        # CARDS
        # =====================

        self.current = self.create_info_card(
            "Atual",
            "-- °C"
        )

        self.status = self.create_info_card(
            "Status",
            "--"
        )

        self.max_temp = self.create_info_card(
            "Limite",
            "95 °C"
        )

        # =====================
        # WORKER
        # =====================

        self._worker = None

        # =====================
        # TIMER
        # =====================

        self.timer = QTimer()

        self.timer.timeout.connect(
            self._start_update
        )

        self.timer.start(1000)

        self._start_update()

    # =========================
    # INICIA WORKER
    # =========================

    def _start_update(self):

        # Evita lançar nova thread se a anterior ainda está a correr
        if self._worker and self._worker.isRunning():
            return

        self._worker = TemperatureWorker()

        self._worker.result.connect(
            self._apply_update
        )

        self._worker.start()

    # =========================
    # APLICA RESULTADO (UI)
    # =========================

    def _apply_update(self, temp):

        self.circle.set_value(temp)

        self.graph.add_value(temp)

        self.current.value_label.setText(
            f"{temp} °C"
        )

        self.status.value_label.setText(
            self.get_status(temp)
        )

    # =========================
    # STATUS
    # =========================

    def get_status(self, temp):

        if temp < 60:
            return "Normal"

        elif temp < 80:
            return "Quente"

        return "Crítico"

    # =========================
    # CLEANUP AO FECHAR
    # =========================

    def closeEvent(self, event):

        self.timer.stop()

        if self._worker and self._worker.isRunning():
            self._worker.quit()
            self._worker.wait()

        super().closeEvent(event)
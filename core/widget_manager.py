from widgets.cpu_widget import CPUWidget
from widgets.ram_widget import RAMWidget
from widgets.temperature_widget import (
    TemperatureWidget
)
from widgets.network_widget import (
    NetworkWidget
)
from widgets.disk_widget import (
    DiskWidget
)

from core.settings import (
    get_widget_position
)


class WidgetManager:

    def __init__(self):

        self.widgets = {}

    # =====================================
    # TOGGLE WIDGET
    # =====================================

    def toggle_widget(
        self,
        widget_name,
        enabled
    ):

        if enabled:

            self.open_widget(
                widget_name
            )

        else:

            self.close_widget(
                widget_name
            )

    # =====================================
    # OPEN WIDGET
    # =====================================

    def open_widget(
        self,
        widget_name
    ):

        # evita duplicar

        if widget_name in self.widgets:

            self.widgets[
                widget_name
            ].show()

            return

        widget = None

        # =====================================
        # CPU
        # =====================================

        if widget_name == "cpu":

            widget = CPUWidget()

            widget.widget_name = "cpu"

            x, y = get_widget_position(
                "cpu"
            )

            widget.move(x, y)

        # =====================================
        # RAM
        # =====================================

        elif widget_name == "ram":

            widget = RAMWidget()

            widget.widget_name = "ram"

            x, y = get_widget_position(
                "ram"
            )

            widget.move(x, y)

        # =====================================
        # TEMP
        # =====================================

        elif widget_name == "temp":

            widget = TemperatureWidget()

            widget.widget_name = "temp"

            x, y = get_widget_position(
                "temp"
            )

            widget.move(x, y)

        # =====================================
        # NET
        # =====================================

        elif widget_name == "net":

            widget = NetworkWidget()

            widget.widget_name = "net"

            x, y = get_widget_position(
                "net"
            )

            widget.move(x, y)

        # =====================================
        # DISK
        # =====================================

        elif widget_name == "disk":

            widget = DiskWidget()

            widget.widget_name = "disk"

            x, y = get_widget_position(
                "disk"
            )

            widget.move(x, y)

        # =====================================
        # SHOW
        # =====================================

        if widget:

            widget.show()

            self.widgets[
                widget_name
            ] = widget

    # =====================================
    # CLOSE WIDGET
    # =====================================

    def close_widget(
        self,
        widget_name
    ):

        if widget_name in self.widgets:

            self.widgets[
                widget_name
            ].close()

            del self.widgets[
                widget_name
            ]

    # =====================================
    # RELOAD WIDGETS
    # =====================================

    def reload_widgets(self):

        active = list(
            self.widgets.keys()
        )

        self.close_all()

        for widget in active:

            self.open_widget(widget)

    # =====================================
    # CLOSE ALL
    # =====================================

    def close_all(self):

        for widget in self.widgets.values():

            try:

                widget.close()

            except:

                pass

        self.widgets.clear()
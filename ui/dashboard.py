from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QSlider,
    QFrame,
    QPushButton,
    QSystemTrayIcon,
    QMenu,
    QStyle,
    QApplication
)

from PySide6.QtCore import Qt

from PySide6.QtGui import QAction

from core.widget_manager import (
    WidgetManager
)

from themes.config import ThemeConfig

from core.settings import (
    set_scale,
    set_widget_enabled,
    is_widget_enabled,
    get_scale
)

from core.startup import (
    enable_startup,
    disable_startup,
    is_startup_enabled
)


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.manager = WidgetManager()

        # =====================================
        # APLICAR ESCALA SALVA
        # (antes de criar qualquer widget)
        # =====================================

        ThemeConfig.UI_SCALE = get_scale()

        # =====================================
        # FRAMELESS
        # =====================================

        self.setWindowFlags(

            Qt.FramelessWindowHint
            |
            Qt.WindowStaysOnTopHint
        )

        # =====================================
        # TRANSPARENT
        # =====================================

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        self.resize(980, 120)

        # =====================================
        # POSITION
        # =====================================

        screen = self.screen().geometry()

        x = (
            screen.width() // 2
        ) - 490

        y = screen.height() - 180

        self.move(x, y)

        # =====================================
        # STYLE
        # =====================================

        self.setStyleSheet("""

            QWidget{
                background:transparent;
                color:white;
                font-size:14px;
            }

            #container{

                background:qlineargradient(
                    x1:0,
                    y1:0,
                    x2:1,
                    y2:1,
                    stop:0 rgba(8,15,30,240),
                    stop:1 rgba(3,8,18,240)
                );

                border-radius:30px;

                border:1px solid
                    rgba(0,170,255,120);
            }

            QLabel{
                font-size:18px;
                font-weight:bold;
            }

            QCheckBox{
                spacing:8px;
                padding:5px;
            }

            QCheckBox::indicator{
                width:18px;
                height:18px;
            }

            QCheckBox::indicator:unchecked{

                border-radius:6px;

                border:1px solid
                    rgba(255,255,255,80);

                background:
                    rgba(255,255,255,20);
            }

            QCheckBox::indicator:checked{

                border-radius:6px;

                background:
                    rgb(0,170,255);

                border:1px solid
                    rgb(0,220,255);
            }

            QSlider::groove:horizontal{

                height:6px;

                background:#222;

                border-radius:3px;
            }

            QSlider::handle:horizontal{

                background:#00aaff;

                width:16px;

                border-radius:8px;
            }

            QPushButton{

                background:
                    rgba(255,255,255,20);

                border:none;

                border-radius:12px;

                color:white;

                font-size:16px;
            }

            QPushButton:hover{

                background:
                    rgba(0,170,255,120);
            }

        """)

        # =====================================
        # CONTAINER
        # =====================================

        container = QFrame()

        container.setObjectName(
            "container"
        )

        # =====================================
        # TITLE
        # =====================================

        title = QLabel(
            "Desktop Gadgets"
        )

        # =====================================
        # CHECKBOXES
        # =====================================

        self.cpu = QCheckBox("CPU")
        self.ram = QCheckBox("RAM")
        self.temp = QCheckBox("TEMP")
        self.net = QCheckBox("REDE")
        self.disk = QCheckBox("DISCO")

        self.startup = QCheckBox(
            "Iniciar com Windows"
        )

        # =====================================
        # SIGNALS
        # =====================================

        def on_cpu(v):
            set_widget_enabled("cpu", v)
            self.manager.toggle_widget("cpu", v)

        def on_ram(v):
            set_widget_enabled("ram", v)
            self.manager.toggle_widget("ram", v)

        def on_temp(v):
            set_widget_enabled("temp", v)
            self.manager.toggle_widget("temp", v)

        def on_net(v):
            set_widget_enabled("net", v)
            self.manager.toggle_widget("net", v)

        def on_disk(v):
            set_widget_enabled("disk", v)
            self.manager.toggle_widget("disk", v)

        self.cpu.toggled.connect(on_cpu)

        self.ram.toggled.connect(on_ram)

        self.temp.toggled.connect(on_temp)

        self.net.toggled.connect(on_net)

        self.disk.toggled.connect(on_disk)

        self.startup.toggled.connect(
            self.toggle_startup
        )

        # =====================================
        # TOP BAR
        # =====================================

        top = QHBoxLayout()

        top.setSpacing(20)

        top.addWidget(title)

        top.addSpacing(10)

        top.addWidget(self.cpu)
        top.addWidget(self.ram)
        top.addWidget(self.temp)
        top.addWidget(self.net)
        top.addWidget(self.disk)

        top.addSpacing(15)

        top.addWidget(self.startup)

        top.addStretch()

        # =====================================
        # SCALE
        # =====================================

        scale_label = QLabel(
            "Escala"
        )

        self.scale = QSlider(
            Qt.Horizontal
        )

        self.scale.setMinimum(50)

        self.scale.setMaximum(120)

        self.scale.setValue(
            int(get_scale() * 100)
        )

        self.scale.setFixedWidth(180)

        self.scale.valueChanged.connect(
            self.change_scale
        )

        top.addWidget(scale_label)

        top.addWidget(self.scale)

        # =====================================
        # BUTTONS
        # =====================================

        self.min_btn = QPushButton("—")

        self.close_btn = QPushButton("✕")

        self.min_btn.setFixedSize(32, 32)

        self.close_btn.setFixedSize(32, 32)

        self.min_btn.clicked.connect(
            self.hide_to_tray
        )

        self.close_btn.clicked.connect(
            self.close_application
        )

        top.addSpacing(10)

        top.addWidget(self.min_btn)

        top.addWidget(self.close_btn)

        # =====================================
        # LAYOUT
        # =====================================

        layout = QVBoxLayout()

        layout.setContentsMargins(
            25,
            20,
            25,
            20
        )

        layout.addLayout(top)

        container.setLayout(layout)

        root = QVBoxLayout()

        root.setContentsMargins(
            10,
            10,
            10,
            10
        )

        root.addWidget(container)

        # =====================================
        # TRAY
        # =====================================

        self.tray = QSystemTrayIcon(self)

        self.tray.setIcon(

            self.style().standardIcon(
                QStyle.SP_ComputerIcon
            )
        )

        tray_menu = QMenu()

        show_action = QAction(
            "Abrir Painel",
            self
        )

        quit_action = QAction(
            "Fechar",
            self
        )

        show_action.triggered.connect(
            self.showNormal
        )

        quit_action.triggered.connect(
            self.close_application
        )

        tray_menu.addAction(show_action)

        tray_menu.addSeparator()

        tray_menu.addAction(quit_action)

        self.tray.setContextMenu(
            tray_menu
        )

        self.tray.show()

        self.tray.activated.connect(
            self.restore_window
        )

        # =====================================
        # RESTORE STATE
        # =====================================

        self.cpu.setChecked(
            is_widget_enabled("cpu")
        )

        self.ram.setChecked(
            is_widget_enabled("ram")
        )

        self.temp.setChecked(
            is_widget_enabled("temp")
        )

        self.net.setChecked(
            is_widget_enabled("net")
        )

        self.disk.setChecked(
            is_widget_enabled("disk")
        )

        self.startup.setChecked(
            is_startup_enabled()
        )

        self.setLayout(root)

        # =====================================
        # START MINIMIZED
        # =====================================

        self.hide()

    # =====================================
    # SCALE
    # =====================================

    def change_scale(self, value):

        scale = value / 100

        ThemeConfig.UI_SCALE = scale

        set_scale(scale)

        self.manager.reload_widgets()

    # =====================================
    # STARTUP
    # =====================================

    def toggle_startup(self, enabled):

        if enabled:

            enable_startup()

        else:

            disable_startup()

    # =====================================
    # HIDE TO TRAY
    # =====================================

    def hide_to_tray(self):

        self.hide()

    # =====================================
    # RESTORE
    # =====================================

    def restore_window(self, reason):

        if reason == QSystemTrayIcon.Trigger:

            self.showNormal()

            self.activateWindow()

    # =====================================
    # CLOSE APP
    # =====================================

    def close_application(self):

        self.manager.close_all()

        self.tray.hide()

        QApplication.quit()
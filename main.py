import sys
import os
import subprocess
import psutil
import time

from PySide6.QtWidgets import QApplication

from ui.dashboard import Dashboard


# =========================================
# BASE DIR
# =========================================

if getattr(sys, 'frozen', False):

    BASE_DIR = sys._MEIPASS

else:

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )


# =========================================
# CHECK LIBRE HARDWARE
# =========================================

def monitor_running():

    for process in psutil.process_iter(['name']):

        try:

            if process.info['name'] == (
                "LibreHardwareMonitor.exe"
            ):

                return True

        except:

            pass

    return False


# =========================================
# LIBRE PATH
# =========================================

monitor_path = os.path.join(
    BASE_DIR,
    "LibreHardwareMonitor",
    "LibreHardwareMonitor.exe"
)

# =========================================
# START LIBRE FIRST
# =========================================

if (
    os.path.exists(monitor_path)
    and
    not monitor_running()
):

    try:

        subprocess.Popen(
            monitor_path,
            shell=True
        )

        # =====================================
        # WAIT LIBRE START
        # =====================================

        started = False

        for _ in range(20):

            if monitor_running():

                started = True
                break

            time.sleep(1)

        # usuário clicou NÃO
        if not started:

            sys.exit()

    except:

        sys.exit()


# =========================================
# QT APP
# =========================================

app = QApplication(sys.argv)

app.setQuitOnLastWindowClosed(False)

# =========================================
# DASHBOARD
# =========================================

window = Dashboard()

window.show()

# =========================================
# EXEC
# =========================================

sys.exit(app.exec())
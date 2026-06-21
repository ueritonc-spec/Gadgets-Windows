import os
import sys


# =====================================
# BASE DIR (recursos do app)
# =====================================

if getattr(sys, 'frozen', False):

    BASE_DIR = sys._MEIPASS

else:

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

# =====================================
# DEFAULT SETTINGS (junto ao app)
# =====================================

DEFAULT_SETTINGS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "default_settings.json"
)

# =====================================
# USER DATA DIR (%APPDATA%)
# Sempre gravável, persiste reinstalações
# =====================================

USER_DATA_DIR = os.path.join(
    os.environ.get(
        "APPDATA",
        os.path.expanduser("~")
    ),
    "DesktopGadgets"
)

os.makedirs(USER_DATA_DIR, exist_ok=True)

# =====================================
# SETTINGS FILE (em %APPDATA%)
# =====================================

SETTINGS_FILE = os.path.join(
    USER_DATA_DIR,
    "settings.json"
)
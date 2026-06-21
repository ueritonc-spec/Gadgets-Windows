import os
import sys
import winreg

from core.constants import (
    APP_NAME
)


# =====================================
# EXECUTABLE PATH
# =====================================

def get_executable_path():

    if getattr(sys, "frozen", False):

        return sys.executable

    return os.path.abspath(
        sys.argv[0]
    )


# =====================================
# ENABLE STARTUP
# =====================================

def enable_startup():

    exe_path = get_executable_path()

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(
        key,
        APP_NAME,
        0,
        winreg.REG_SZ,
        exe_path
    )

    winreg.CloseKey(key)


# =====================================
# DISABLE STARTUP
# =====================================

def disable_startup():

    try:

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )

        winreg.DeleteValue(
            key,
            APP_NAME
        )

        winreg.CloseKey(key)

    except:

        pass


# =====================================
# CHECK STARTUP
# =====================================

def is_startup_enabled():

    try:

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run"
        )

        winreg.QueryValueEx(
            key,
            APP_NAME
        )

        winreg.CloseKey(key)

        return True

    except:

        return False
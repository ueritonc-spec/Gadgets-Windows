import json
import os

from core.config_manager import (
    SETTINGS_FILE,
    DEFAULT_SETTINGS_FILE
)


# =====================================
# LOAD JSON
# =====================================

def load_json(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# =====================================
# SAVE JSON
# =====================================

def save_json(path, data):

    try:

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    except Exception:

        pass


# =====================================
# CREATE SETTINGS
# =====================================

def ensure_settings_file():

    if not os.path.exists(
        SETTINGS_FILE
    ):

        default = load_json(
            DEFAULT_SETTINGS_FILE
        )

        save_json(
            SETTINGS_FILE,
            default
        )


# =====================================
# LOAD SETTINGS
# =====================================

def load_settings():

    ensure_settings_file()

    return load_json(
        SETTINGS_FILE
    )


# =====================================
# SAVE SETTINGS
# =====================================

def save_settings(settings):

    save_json(
        SETTINGS_FILE,
        settings
    )


# =====================================
# SCALE
# =====================================

def get_scale():

    settings = load_settings()

    return settings.get(
        "scale",
        0.65
    )


def set_scale(value):

    settings = load_settings()

    settings["scale"] = value

    save_settings(settings)


# =====================================
# STARTUP
# =====================================

def get_startup_enabled():

    settings = load_settings()

    return settings.get(
        "startup",
        False
    )


def set_startup_enabled(enabled):

    settings = load_settings()

    settings["startup"] = enabled

    save_settings(settings)


# =====================================
# WIDGET ENABLED
# =====================================

def is_widget_enabled(widget_name):

    settings = load_settings()

    widgets = settings.get(
        "widgets",
        {}
    )

    widget = widgets.get(
        widget_name,
        {}
    )

    return widget.get(
        "enabled",
        False
    )


def set_widget_enabled(
    widget_name,
    enabled
):

    settings = load_settings()

    if "widgets" not in settings:

        settings["widgets"] = {}

    if widget_name not in settings[
        "widgets"
    ]:

        settings["widgets"][
            widget_name
        ] = {}

    settings["widgets"][
        widget_name
    ]["enabled"] = enabled

    save_settings(settings)


# =====================================
# WIDGET POSITION
# =====================================

def get_widget_position(
    widget_name
):

    settings = load_settings()

    widgets = settings.get(
        "widgets",
        {}
    )

    widget = widgets.get(
        widget_name,
        {}
    )

    return (
        widget.get("x", 20),
        widget.get("y", 20)
    )


def set_widget_position(
    widget_name,
    x,
    y
):

    settings = load_settings()

    if "widgets" not in settings:

        settings["widgets"] = {}

    if widget_name not in settings[
        "widgets"
    ]:

        settings["widgets"][
            widget_name
        ] = {}

    settings["widgets"][
        widget_name
    ]["x"] = x

    settings["widgets"][
        widget_name
    ]["y"] = y

    save_settings(settings)
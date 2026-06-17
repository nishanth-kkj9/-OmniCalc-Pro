# Theme management functions
from PySide6.QtWidgets import QApplication
from utils.constants import THEMES_DIR
import os


def apply_theme(app: QApplication, theme_name: str = "dark"):
    qss_path = os.path.join(THEMES_DIR, f"{theme_name}.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())
    else:
        app.setStyleSheet("")
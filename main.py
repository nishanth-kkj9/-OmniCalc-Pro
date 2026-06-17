# CRITICAL: matplotlib backend MUST be set before any Qt imports
import matplotlib
matplotlib.use("QtAgg")

import sys
import os
import traceback

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.helpers import ensure_dirs, load_config
from utils.themes import apply_theme
from utils.logger import setup_logger, get_logger
from core.error_handler import install_global_handler
from core.services import register_service, get_service
from core.history_manager import get_history_manager
from ui.main_window import MainWindow

logger = get_logger()


def register_services():
    register_service("history_manager", get_history_manager, singleton=True)
    register_service("config", load_config, singleton=True)


def main():
    setup_logger()
    logger.info("=== OmniCalc Pro Application Starting ===")

    try:
        ensure_dirs()
        logger.debug("Project directories verified/created.")

        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        logger.info("QApplication initialized with Fusion style.")

        install_global_handler(app)
        logger.debug("Global error handler installed.")

        register_services()

        config = load_config()
        logger.debug(f"Configuration loaded: {config}")

        apply_theme(app, config.get("theme", "dark"))
        logger.info(f"Applied theme: {config.get('theme', 'dark')}")

        font = QFont("Segoe UI", config.get("font_size", 14))
        app.setFont(font)

        pal = app.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor("#1e1e24"))
        app.setPalette(pal)

        window = MainWindow()
        logger.info("Main window instantiated.")

        window.show()
        logger.info("Application window displayed. Entering event loop.")

        sys.exit(app.exec())
    except Exception as e:
        logger.critical(f"Fatal startup error: {e}\n{traceback.format_exc()}")
        raise


if __name__ == "__main__":
    main()
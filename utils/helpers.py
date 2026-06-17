import os
import sys
import json
import pyperclip
from PySide6.QtCore import Qt
from utils.constants import BASE_DIR, CONFIG_PATH
from utils.logger import get_logger
from core.safe_evaluator import safe_eval as _safe_eval

logger = get_logger()


def ensure_dirs():
    dirs = [
        os.path.join(BASE_DIR, 'assets', 'icons'),
        os.path.join(BASE_DIR, 'assets', 'images'),
        os.path.join(BASE_DIR, 'assets', 'themes'),
        os.path.join(BASE_DIR, 'database')
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    logger.debug("Project directories ensured.")


def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            logger.debug("Config file loaded.")
            return json.load(f)
    logger.warning("Config file not found. Using defaults.")
    return {"theme": "dark", "font_size": 14, "angle_mode": "degrees"}


def save_config(cfg):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(cfg, f, indent=2)
    logger.debug("Configuration saved.")


def safe_eval(expression: str, mode: str = "degrees"):
    """Backward compatible wrapper using new SafeEvaluator."""
    return _safe_eval(expression, mode)


def copy_to_clipboard(text):
    try:
        pyperclip.copy(str(text))
        logger.debug(f"Copied to clipboard: {text}")
    except Exception as e:
        logger.warning(f"Clipboard copy failed: {e}")


def paste_from_clipboard():
    try:
        return pyperclip.paste()
    except Exception:
        return ""
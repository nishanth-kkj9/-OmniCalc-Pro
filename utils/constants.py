import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR: str = os.path.dirname(sys.executable)
else:
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_DIR: str = os.path.join(BASE_DIR, 'assets')
THEMES_DIR: str = os.path.join(ASSETS_DIR, 'themes')
ICONS_DIR: str = os.path.join(ASSETS_DIR, 'icons')
DB_DIR: str = os.path.join(BASE_DIR, 'database')
DB_PATH: str = os.path.join(DB_DIR, 'history.db')
CONFIG_PATH: str = os.path.join(BASE_DIR, 'config.json')

APP_NAME: str = "OmniCalc Pro"
VERSION: str = "2.1.0"

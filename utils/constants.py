# Constants for OmniCalc Pro
import os
import sys

# Base directory setup
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
THEMES_DIR = os.path.join(ASSETS_DIR, 'themes')
ICONS_DIR = os.path.join(ASSETS_DIR, 'icons')
DB_DIR = os.path.join(BASE_DIR, 'database')
DB_PATH = os.path.join(DB_DIR, 'history.db')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

APP_NAME = "OmniCalc Pro"
VERSION = "2.1.0"
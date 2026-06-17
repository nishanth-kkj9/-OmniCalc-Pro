from PySide6.QtWidgets import QPushButton, QLineEdit, QMenu
from PySide6.QtCore import Qt
from utils.helpers import copy_to_clipboard, paste_from_clipboard

class CalcButton(QPushButton):
    def __init__(self, text, style_class=""):
        super().__init__(text)
        self.setProperty("class", style_class)
        self.setMinimumSize(65, 55)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.setStyleSheet("""
            QPushButton { border-radius: 12px; padding: 8px; font-weight: 600; }
            QPushButton:hover { background-color: #333345; }
            QPushButton:pressed { background-color: #1a1a28; }
        """)

class DisplayPanel(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.setStyleSheet("""
            background-color: #1a1a24; color: #00ffaa; font-family: "Consolas", "Courier New", monospace;
            font-size: 32px; border: 2px solid #2a2a35; padding: 16px; border-radius: 14px;
        """)
        self.setMinimumHeight(80)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
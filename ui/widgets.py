from PySide6.QtWidgets import QPushButton, QLineEdit, QMenu, QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QFont
from utils.helpers import copy_to_clipboard, paste_from_clipboard

BUTTON_STYLES = {
    "": """
        QPushButton {
            border-radius: 10px;
            padding: 8px;
            font-weight: 600;
            background-color: #252535;
            color: #fff;
            border: none;
        }
        QPushButton:hover { background-color: #2f2f45; }
        QPushButton:pressed { background-color: #1a1a28; }
    """,
    "Op": """
        QPushButton {
            border-radius: 10px;
            padding: 8px;
            font-weight: 700;
            background-color: #2b5797;
            color: white;
            border: none;
        }
        QPushButton:hover { background-color: #3668b0; }
        QPushButton:pressed { background-color: #1e3d6b; }
    """,
    "Func": """
        QPushButton {
            border-radius: 10px;
            padding: 8px;
            font-weight: 600;
            background-color: #2d3a2d;
            color: #aaffaa;
            border: none;
        }
        QPushButton:hover { background-color: #3a4a3a; }
        QPushButton:pressed { background-color: #1d2a1d; }
    """,
    "DangerBtn": """
        QPushButton {
            border-radius: 10px;
            padding: 8px;
            font-weight: 600;
            background-color: #8b2222;
            color: #fff;
            border: none;
        }
        QPushButton:hover { background-color: #a33333; }
        QPushButton:pressed { background-color: #6b1a1a; }
    """,
}


class CalcButton(QPushButton):
    def __init__(self, text, style_class=""):
        super().__init__(text)
        self.setProperty("class", style_class)
        self.setMinimumSize(52, 44)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(BUTTON_STYLES.get(style_class, BUTTON_STYLES[""]))


class DisplayPanel(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a24;
                color: #00ffaa;
                font-family: "Consolas", "Courier New", monospace;
                font-size: 34px;
                border: 2px solid #2a2a35;
                padding: 16px 20px;
                border-radius: 14px;
                selection-background-color: #3a3a55;
                selection-color: #ffffff;
            }
        """)
        self.setMinimumHeight(80)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)


class AnimatedButton(QPushButton):
    def __init__(self, text, style_class=""):
        super().__init__(text)
        self.setProperty("class", style_class)
        self.setMinimumSize(52, 44)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(BUTTON_STYLES.get(style_class, BUTTON_STYLES[""]))
        self._anim_value = 0.0
        self._animation = QPropertyAnimation(self, b"opacity")
        self._animation.setDuration(100)
        self._animation.setStartValue(1.0)
        self._animation.setEndValue(0.7)
        self._animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.clicked.connect(self._animate_press)

    def _animate_press(self):
        self._animation.stop()
        self._animation.setDirection(QPropertyAnimation.Direction.Forward)
        self._animation.finished.connect(lambda: self._animation.setDirection(QPropertyAnimation.Direction.Backward) or self._animation.start())
        self._animation.start()
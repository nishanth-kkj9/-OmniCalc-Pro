from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolButton, QLabel
from PySide6.QtCore import Qt, Signal

PAGE_NAMES = ["Dashboard", "Basic", "Scientific", "Graph", "Converter", "Programmer", "Matrix", "Statistics", "Finance", "History", "Settings"]
ICONS = ["\U0001f3e0", "\U0001f522", "\U0001f52c", "\U0001f4c8", "\U0001f504", "\U0001f4bb", "\U0001f532", "\U0001f4ca", "\U0001f4b0", "\U0001f552", "\U00002699"]

class Sidebar(QWidget):
    page_changed = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.btn_list = []
        self.setup_ui()

    def setup_ui(self):
        self.setFixedWidth(90)
        self.setStyleSheet("background-color: #15151e; border-right: 1px solid #252535;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 15)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        for i, name in enumerate(PAGE_NAMES):
            btn = QToolButton()
            btn.setToolTip(name)
            btn.setText(ICONS[i])
            
            f = btn.font()
            f.setPointSize(22)
            btn.setFont(f)
            
            btn.setFixedSize(60, 60)
            btn.setStyleSheet("""
                QToolButton { border-radius: 14px; background: transparent; color: #888; }
                QToolButton:hover { background: #1e1e2e; color: #fff; }
            """)
            btn.clicked.connect(lambda _, idx=i: self.page_changed.emit(idx))
            self.btn_list.append(btn)
            layout.addWidget(btn)
        layout.addStretch()
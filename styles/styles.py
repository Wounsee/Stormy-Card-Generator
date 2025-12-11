style = """
QMainWindow { background: transparent; }
QWidget { font-family: 'Segoe UI', sans-serif; color: #ECEFF4; outline: none; }

QFrame#MnFr {
    background-color: #121215; 
    border-radius: 16px; 
    border: 1px solid #23232A;
}

QFrame#TiBar { background: transparent; }
QLabel#TiLbl { color: #7C4DFF; font-weight: 900; letter-spacing: 2px; font-size: 12px; }

QPushButton#TiBtn, QPushButton#TiBtnCls {
    border-radius: 6px; background: transparent; color: #555; font-weight: bold;
}
QPushButton#TiBtn:hover { background-color: #2A2A35; color: white; }
QPushButton#TiBtnCls:hover { background-color: #FF453A; color: white; }

/* Control Panel fixed at top */
QFrame#Ctrl {
    background-color: #1A1A20; border-radius: 12px; border: 1px solid #2A2A32;
}

QComboBox, QSpinBox {
    background-color: #121215; border: 1px solid #2A2A32; border-radius: 6px;
    padding: 8px 12px; color: #ddd; font-weight: 600; font-size: 13px;
}
QComboBox:focus, QSpinBox:focus { border-color: #7C4DFF; }
QComboBox::drop-down { border: none; width: 20px; }
QComboBox QAbstractItemView {
    background-color: #1A1A20; border: 1px solid #333; selection-background-color: #7C4DFF; color: white;
}

QPushButton#GenBtn {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6C3CFF, stop:1 #5522E0);
    color: white; border-radius: 8px; font-weight: 700; font-size: 13px; padding: 10px;
}
QPushButton#GenBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7F55FF, stop:1 #6C3CFF);
}
QPushButton#GenBtn:pressed { background: #451AB0; }

QScrollArea { background: transparent; border: none; }
QWidget#ResW { background: transparent; }

/* Card Styling */
QFrame#Row {
    background-color: #1A1A20; border-radius: 8px; border: 1px solid #25252D;
}
QFrame#Row:hover { border-color: #444; background-color: #202028; }

QLabel#Mono {
    font-family: 'Consolas', monospace; font-size: 14px; color: #ddd; font-weight: bold;
}
QLabel#Mono:hover { color: #7C4DFF; }

QLabel#Tp { font-size: 10px; font-weight: 800; color: #666; }

QPushButton#Exp {
    background: transparent; border: 1px solid #333; color: #777; border-radius: 6px; font-size: 11px; padding: 5px 10px;
}
QPushButton#Exp:hover { border-color: #7C4DFF; color: #7C4DFF; }

QLabel#Tst {
    background-color: #252525; border-left: 3px solid #7C4DFF; color: white; 
    border-radius: 4px; padding: 8px 16px; font-weight: 600; font-size: 12px;
}

QScrollBar:vertical { background: transparent; width: 6px; }
QScrollBar::handle:vertical { background: #333; border-radius: 3px; }
QScrollBar::handle:vertical:hover { background: #555; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
"""
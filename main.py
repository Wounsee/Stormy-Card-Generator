from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from styles.styles import style
from util.generUtil import genOne, BINS
from PyQt6.QtGui import *
from util.savaUtil import expData

class Clk(QLabel):
    clk = pyqtSignal(str)
    def __init__(self, t, r):
        super().__init__(t)
        self.raw = r
        self.setObjectName("Mono")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            QApplication.clipboard().setText(self.raw)
            self.clk.emit(self.raw)

class Tst(QLabel):
    def __init__(self, p, t):
        super().__init__(t, p)
        self.setObjectName("Tst")
        self.adjustSize()
        self.move((p.width()-self.width())//2, p.height()-60)
        self.show()
        self.eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.eff)
        self.a = QPropertyAnimation(self.eff, b"opacity")
        self.a.setDuration(300); self.a.setStartValue(0); self.a.setEndValue(1)
        self.a.start()
        QTimer.singleShot(2000, self.out)
        
    def out(self):
        self.a.setDirection(QPropertyAnimation.Direction.Backward)
        self.a.start()
        self.a.finished.connect(self.close)

class TiBar(QFrame):
    def __init__(self, p):
        super().__init__()
        self.p = p
        self.setObjectName("TiBar")
        self.setFixedHeight(40)
        l = QHBoxLayout(self)
        l.setContentsMargins(15,0,15,0)
        l.addWidget(QLabel("@StormDev -> Stormy Card Generation", objectName="TiLbl"))
        l.addStretch()
        b1 = QPushButton("-", objectName="TiBtn"); b1.setFixedSize(30,30)
        b1.clicked.connect(p.showMinimized)
        b2 = QPushButton("x", objectName="TiBtnCls"); b2.setFixedSize(30,30)
        b2.clicked.connect(p.close)
        l.addWidget(b1); l.addWidget(b2)
        self.old = None
        
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton: self.old = e.globalPosition().toPoint()
        
    def mouseMoveEvent(self, e):
        if self.old:
            self.p.move(self.p.pos() + e.globalPosition().toPoint() - self.old)
            self.old = e.globalPosition().toPoint()
            
    def mouseReleaseEvent(self, e): self.old = None

class Row(QFrame):
    
    def __init__(self, d, cb):
        super().__init__()
        self.setObjectName("Row")
        self.setFixedHeight(55)
        l = QHBoxLayout(self); l.setContentsMargins(15,0,15,0); l.setSpacing(15)
        
        c = {"VISA":"#4d6eff","MASTERCARD":"#FF453A","AMEX":"#00E5FF"}.get(d['t'],"#FFA500")
        ind = QLabel(); ind.setFixedSize(3,20); ind.setStyleSheet(f"background:{c};border-radius:1px")
        l.addWidget(ind)
        l.addWidget(QLabel(d['t'], objectName="Tp"))
        l.addStretch()
        
        l1 = Clk(d['f'], d['n']); l1.clk.connect(cb); l.addWidget(l1)
        l.addSpacing(10)
        l2 = Clk(d['e'], d['e']); l2.clk.connect(cb); l.addWidget(l2)
        l.addSpacing(10)
        l3 = Clk(d['c'], d['c']); l3.clk.connect(cb); l.addWidget(l3)
        
        self.eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.eff)
        self.eff.setOpacity(0)
        
    def show_anim(self, del_ms):
        QTimer.singleShot(del_ms, self._fade)
        
    def _fade(self):
        self.a = QPropertyAnimation(self.eff, b"opacity")
        self.a.setDuration(400); self.a.setStartValue(0); self.a.setEndValue(1)
        self.a.finished.connect(self._clean) 
        self.a.start()
        
    def _clean(self):
        self.setGraphicsEffect(None)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(520, 720)
        self.fr = QFrame(objectName="MnFr")
        self.setCentralWidget(self.fr)
        sh = QGraphicsDropShadowEffect(self); sh.setBlurRadius(20); sh.setColor(QColor(0,0,0,150)); sh.setOffset(0,5)
        self.fr.setGraphicsEffect(sh)
        ml = QVBoxLayout(self.fr); ml.setContentsMargins(0,0,0,0); ml.setSpacing(0)
        ml.addWidget(TiBar(self))
        cnt = QVBoxLayout(); cnt.setContentsMargins(25,20,25,25); cnt.setSpacing(15)
        self.ctrl = QFrame(objectName="Ctrl")
        cl = QVBoxLayout(self.ctrl); cl.setContentsMargins(15,15,15,15); cl.setSpacing(12)
        r1 = QHBoxLayout()
        self.cb = QComboBox(); self.cb.addItems(BINS.keys())
        self.sb = QSpinBox(); self.sb.setRange(1,1000); self.sb.setValue(10); self.sb.setFixedWidth(70); self.sb.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.sb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        r1.addWidget(self.cb, 1); r1.addWidget(self.sb)
        cl.addLayout(r1)
        b = QPushButton("Сгенерировать", objectName="GenBtn")
        b.setCursor(Qt.CursorShape.PointingHandCursor)
        b.clicked.connect(self.go)
        cl.addWidget(b)
        cnt.addWidget(self.ctrl)
        self.sa = QScrollArea()
        self.sa.setWidgetResizable(True); self.sa.horizontalScrollBar().setDisabled(True)
        self.w_res = QWidget(objectName="ResW")
        self.l_res = QVBoxLayout(self.w_res); self.l_res.setAlignment(Qt.AlignmentFlag.AlignTop); self.l_res.setSpacing(8)
        self.sa.setWidget(self.w_res)
        cnt.addWidget(self.sa)
        self.ft = QHBoxLayout()
        bj = QPushButton("JSON", objectName="Exp"); bj.clicked.connect(lambda: self.sv("json"))
        bt = QPushButton("TXT", objectName="Exp"); bt.clicked.connect(lambda: self.sv("txt"))
        self.ft.addStretch(); self.ft.addWidget(bj); self.ft.addWidget(bt)
        cnt.addLayout(self.ft)
        ml.addLayout(cnt)
        self.dt = []

    def ntf(self, t): Tst(self.fr, t)
    def go(self):
        while self.l_res.count():
            w = self.l_res.takeAt(0).widget()
            if w: w.deleteLater()
        self.dt = []
        n = self.sb.value()
        bn = self.cb.currentText()
        for i in range(n):
            d = genOne(bn); self.dt.append(d)
            r = Row(d, lambda x: self.ntf(f"Скопировано: {x}"))
            self.l_res.addWidget(r)
            r.show_anim(i * 40) 

    def sv(self, f):
        if not self.dt: return self.ntf("Сначало сгенерируйте карты!")
        p, _ = QFileDialog.getSaveFileName(self, "Сохранить", "", f"*.{f}")
        if p: expData(p, self.dt, f); self.ntf("Сохранено")

app = QApplication(sys.argv)
app.setStyleSheet(style)
w = App()
w.show()
sys.exit(app.exec())

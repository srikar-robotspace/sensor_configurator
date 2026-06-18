from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from ui.styles import STYLESHEET
from ui.widgets import PulseButton, StatusLED

from backend.scan_worker import ScanWorker
from backend.modbus_manager import ModbusManager


class SensorConfigurator(QWidget):

    PORT = "/dev/ttyUSB0"

    def __init__(self):

        super().__init__()

        self.current_addr = None

        self._scan_worker = None

        self.backend = ModbusManager(self.PORT)

        self.setWindowTitle(
            "Scoot · Sensor Configurator"
        )

        self.setMinimumSize(720, 680)

        self.setStyleSheet(STYLESHEET)

        self._build_ui()

    def _build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(
            32, 28, 32, 24
        )

        root.setSpacing(20)

        root.addWidget(self._header())

        row = QHBoxLayout()

        row.setSpacing(16)

        row.addWidget(self._port_card(), 1)

        row.addWidget(self._status_card(), 1)

        root.addLayout(row)

        root.addWidget(self._scan_card())

        root.addWidget(self._assign_card())

        root.addWidget(self._log_card(), 1)

    def _header(self):

        w = QWidget()

        h = QHBoxLayout(w)

        badge = QLabel("MODBUS RTU")

        badge.setObjectName("badge")

        h.addWidget(badge)

        h.addStretch()

        title = QLabel("Sensor Configurator")

        title.setObjectName("title")

        h.addWidget(title)

        return w

    def _port_card(self):

        card = self._make_card()

        l = card.layout()

        lbl = QLabel("SERIAL PORT")

        lbl.setObjectName("card_eyebrow")

        l.addWidget(lbl)

        self.port_display = QLabel(self.PORT)

        self.port_display.setObjectName(
            "mono_large"
        )

        l.addWidget(self.port_display)

        sub = QLabel("9600 8N1  ·  Modbus RTU")

        sub.setObjectName("sub")

        l.addWidget(sub)

        return card

    def _status_card(self):

        card = self._make_card()

        l = card.layout()

        top = QHBoxLayout()

        lbl = QLabel("DEVICE STATUS")

        lbl.setObjectName("card_eyebrow")

        top.addWidget(lbl)

        top.addStretch()

        self.led = StatusLED()

        top.addWidget(self.led)

        l.addLayout(top)

        self.status_label = QLabel("No device")

        self.status_label.setObjectName(
            "mono_large"
        )

        l.addWidget(self.status_label)

        self.addr_sub = QLabel(
            "Run a scan to detect"
        )

        self.addr_sub.setObjectName("sub")

        l.addWidget(self.addr_sub)

        return card

    def _scan_card(self):

        card = self._make_card()

        l = card.layout()

        lbl = QLabel("DISCOVER")

        lbl.setObjectName("card_eyebrow")

        l.addWidget(lbl)

        self.scan_btn = PulseButton(
            "  Scan for Sensor"
        )

        self.scan_btn.setObjectName(
            "primary_btn"
        )

        self.scan_btn.setFixedHeight(48)

        self.scan_btn.clicked.connect(
            self.scan_sensor
        )

        l.addWidget(self.scan_btn)

        return card

    def _assign_card(self):

        card = self._make_card()

        l = card.layout()

        lbl = QLabel("ASSIGN ADDRESS")

        lbl.setObjectName("card_eyebrow")

        l.addWidget(lbl)

        row = QHBoxLayout()

        row.setSpacing(12)

        self.addr_input = QLineEdit()

        self.addr_input.setObjectName(
            "addr_input"
        )

        self.addr_input.setPlaceholderText(
            "Enter new address  (1 – 247)"
        )

        self.addr_input.setFixedHeight(44)

        row.addWidget(self.addr_input, 1)

        self.assign_btn = QPushButton("Assign")

        self.assign_btn.setObjectName(
            "assign_btn"
        )

        self.assign_btn.setFixedHeight(44)

        self.assign_btn.setFixedWidth(110)

        self.assign_btn.clicked.connect(
            self.assign_address
        )

        row.addWidget(self.assign_btn)

        l.addLayout(row)

        hint = QLabel(
            "Write to register 100."
        )

        hint.setObjectName("hint")

        l.addWidget(hint)

        return card

    def _log_card(self):

        card = self._make_card()

        l = card.layout()

        top = QHBoxLayout()

        lbl = QLabel("ACTIVITY LOG")

        lbl.setObjectName("card_eyebrow")

        top.addWidget(lbl)

        top.addStretch()

        clr = QPushButton("Clear")

        clr.setObjectName("ghost_btn")

        clr.clicked.connect(
            lambda: self.log.clear()
        )

        top.addWidget(clr)

        l.addLayout(top)

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.setObjectName("log")

        l.addWidget(self.log)

        return card

    def _make_card(self):

        card = QFrame()

        card.setObjectName("card")

        vl = QVBoxLayout(card)

        vl.setContentsMargins(
            20, 16, 20, 16
        )

        return card

    def log_message(self, msg):

        self.log.append(msg)

    def scan_sensor(self):

        if (
            self._scan_worker
            and self._scan_worker.isRunning()
        ):
            return

        self.scan_btn.setEnabled(False)

        self.scan_btn.start_pulse()

        self.status_label.setText("Scanning...")

        self.log_message(
            "Initiating scan..."
        )

        self._scan_worker = ScanWorker(
            self.PORT
        )

        self._scan_worker.log.connect(
            self.log_message
        )

        self._scan_worker.found.connect(
            self._on_found
        )

        self._scan_worker.not_found.connect(
            self._on_not_found
        )

        self._scan_worker.start()

    def _on_found(self, addr):

        self.current_addr = addr

        self.scan_btn.stop_pulse()

        self.scan_btn.setEnabled(True)

        self.led.set_color("#22c55e")

        self.status_label.setText(
            f"Address {addr}"
        )

        self.addr_sub.setText(
            "Sensor online"
        )

    def _on_not_found(self):

        self.current_addr = None

        self.scan_btn.stop_pulse()

        self.scan_btn.setEnabled(True)

        self.led.set_color("#ef4444")

        self.status_label.setText(
            "Not found"
        )

    def assign_address(self):

        QMessageBox.information(
            self,
            "Info",
            "Assign Logic Here"
        )
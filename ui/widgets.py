from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush


class PulseButton(QPushButton):

    def __init__(self, text, parent=None):

        super().__init__(text, parent)

        self._pulse_radius = 0.0

        self._pulsing = False

        self._timer = QTimer(self)

        self._timer.timeout.connect(self._tick)

    def start_pulse(self):

        self._pulse_radius = 0.0

        self._pulsing = True

        self._timer.start(16)

    def stop_pulse(self):

        self._pulsing = False

        self._timer.stop()

        self._pulse_radius = 0.0

        self.update()

    def _tick(self):

        self._pulse_radius = (
            self._pulse_radius + 1.5
        ) % 60

        self.update()

    def paintEvent(self, event):

        super().paintEvent(event)

        if self._pulsing and self._pulse_radius > 0:

            painter = QPainter(self)

            painter.setRenderHint(
                QPainter.RenderHint.Antialiasing
            )

            cx = self.width() // 2
            cy = self.height() // 2

            r = int(self._pulse_radius)

            alpha = max(
                0,
                255 - int(self._pulse_radius * 4.2)
            )

            pen = QPen(
                QColor(0, 212, 255, alpha)
            )

            pen.setWidth(2)

            painter.setPen(pen)

            painter.setBrush(
                Qt.BrushStyle.NoBrush
            )

            painter.drawEllipse(
                cx - r,
                cy - r,
                r * 2,
                r * 2
            )

            painter.end()


class StatusLED(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setFixedSize(14, 14)

        self._color = QColor("#444")

    def set_color(self, color: str):

        self._color = QColor(color)

        self.update()

    def paintEvent(self, event):

        p = QPainter(self)

        p.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        p.setBrush(
            QBrush(self._color)
        )

        p.setPen(Qt.PenStyle.NoPen)

        p.drawEllipse(1, 1, 12, 12)
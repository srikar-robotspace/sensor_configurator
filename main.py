import sys
from PyQt6.QtWidgets import QApplication

from ui.main_window import SensorConfigurator


app = QApplication(sys.argv)

app.setStyle("Fusion")

window = SensorConfigurator()

window.show()

sys.exit(app.exec())
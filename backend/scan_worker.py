from PyQt6.QtCore import QThread, pyqtSignal
from pymodbus.client import ModbusSerialClient


class ScanWorker(QThread):

    found = pyqtSignal(int)
    not_found = pyqtSignal()
    log = pyqtSignal(str)

    def __init__(self, port):
        super().__init__()
        self.port = port

    def run(self):

        client = ModbusSerialClient(
            port=self.port,
            baudrate=9600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=0.5
        )

        if not client.connect():

            self.log.emit(
                f"✗  Cannot open {self.port}"
            )

            self.not_found.emit()

            return

        self.log.emit(
            f"Scanning {self.port}  ·  addresses 1 – 247 …"
        )

        for addr in range(1, 248):

            try:

                result = client.read_holding_registers(
                    address=2,
                    count=2,
                    device_id=addr
                )

                if not result.isError():

                    client.close()

                    self.log.emit(
                        f"✓  Sensor detected at address {addr}"
                    )

                    self.found.emit(addr)

                    return

            except Exception:
                pass

        client.close()

        self.log.emit(
            "✗  No sensor found on this port"
        )

        self.not_found.emit()
from pymodbus.client import ModbusSerialClient


class ModbusManager:

    def __init__(self, port):
        self.port = port

    def make_client(self):

        return ModbusSerialClient(
            port=self.port,
            baudrate=9600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=1
        )
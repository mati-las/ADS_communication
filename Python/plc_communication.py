import ctypes
import pyads
from structs import Struct_IN, Struct_OUT

class PLC_communication():
    def __init__(self, PLC_IP:str, PLC_AMS_IP:str, PLC_port = pyads.PORT_TC3PLC1):
        self.PLC_IP = PLC_IP
        self.PLC_AMS_IP = PLC_AMS_IP
        self.PLC_port = PLC_port
        self.plc = pyads.Connection(self.PLC_AMS_IP, self.PLC_port, self.PLC_IP)

    def connect(self):
        self.plc.open()

    def disconnect(self):
        if self.plc.is_open:
            self.plc.close()

    def write(self, plc_write:str, signal:bool, bOK:bool):
        data_out = Struct_OUT()
        data_out.bHeat1 = signal
        data_out.bOK = bOK
        self.plc.write_by_name(plc_write, bytes(data_out), pyads.PLCTYPE_BYTE * ctypes.sizeof(Struct_OUT))

    def read(self, plc_read:str):
        data_in = self.plc.read_by_name(plc_read, pyads.PLCTYPE_BYTE * ctypes.sizeof(Struct_IN))
        return Struct_IN.from_buffer_copy(bytes(data_in))
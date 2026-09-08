import pyads
import ctypes
from structs import Struct_IN, Struct_OUT


PLC_IP = '127.0.0.1'
PLC_AMS_IP = '192.168.1.8.1.1'
plc_read = 'MAIN.data_out'


with pyads.Connection(PLC_AMS_IP, pyads.PORT_TC3PLC1, PLC_IP) as plc:
    try:
        data_in = plc.read_by_name(plc_read, pyads.PLCTYPE_BYTE * ctypes.sizeof(Struct_IN))
        print(Struct_IN.from_buffer_copy(bytes(data_in)))
    except pyads.ADSError as err:
        print(f"Error {err}")


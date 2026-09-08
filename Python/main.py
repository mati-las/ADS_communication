import pyads
import ctypes
import time
from structs import Struct_IN, Struct_OUT
from plc_communication import PLC_communication


'''
NOTE: Update the IP addresses and AMS Net IDs to match your hardware setup.
Depending on the target PLC and the host device (e.g., local PC vs. Raspberry Pi) 
used for reading/writing data structures, you must also add or modify 
the ADS routing configuration in TwinCAT 3
'''
PLC_IP = '127.0.0.1'
PLC_AMS_IP = '192.168.1.8.1.1'     
data_read = 'MAIN.data_out'
data_write = 'MAIN.data_in'

plc = PLC_communication(PLC_IP, PLC_AMS_IP, pyads.PORT_TC3PLC1)

data_in = Struct_IN()
data_out = Struct_OUT()
data_out.bHeat1 = True
data_out.bOK = False

plc.connect()

try:
    data_in = plc.read(data_read)
    print("Data read from PLC:")
    print(data_in)
    plc.write(data_write, data_out.bHeat1, data_out.bOK)
except Exception as e:
    print(f"Communication error: {e}")
finally:
    plc.disconnect()



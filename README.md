# ADS_communication

> Project Status: Work in Progress
> Core communication and signal generation are already working. File logging functionality is currently missing and will be implemented soon.

## About the Project
This project provides a communication interface between a PC / Raspberry Pi and a Beckhoff PLC. 

Both devices generate a bit signal, send it to each other, and verify the received data. Based on this verification, they send back connection status information to confirm that the received signal is correct and the connection is stable.

**Technologies used:**
* Python (`pyads`)
* TwinCAT 3
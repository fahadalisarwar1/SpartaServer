import socket

local_ip = socket.gethostname()
local_port = 8080
address = (local_ip, local_port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(address)

s.listen(5)


HEADER_SIZE=10
msg = "HELLO WORLD my name is fahad"
print(msg)
msg = f"{len(msg):<{HEADER_SIZE}}" + msg
print(msg)
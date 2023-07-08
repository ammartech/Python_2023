import socket

def ip_local_gather():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM)as s:
        s.connect(("8.8.8.8", 80))
        final = s.getsockname()[0]
        return final  

local_ip= ip_local_gather()

print(f"عنوان المحلي هو : {local_ip}")

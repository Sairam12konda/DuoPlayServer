import socket
from _thread import *
import time
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('ssl.pem')
server = '10.20.202.223'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]
start_time=time.time()
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = pos[nid][:]
                a=pos[0].split(":")[1]
                b=pos[1].split(":")[1]
                if(a==b):
                    conn.sendall(str.encode("Game Over"))
                print("Sending: " + reply)
            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
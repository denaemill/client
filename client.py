import socket
import sys

BUFFER_SIZE = 10000

#Getting all of the inputs from the command line
host = sys.argv[1]
port = sys.argv[2]
file = sys.argv[3]


#Establishing the connection from the client
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("ERROR: Socket not created")
    sys.exit(1)

try:
    sock.settimeout(10)  # Setting timeouts for the code
    port = int(port)
    sock.connect((host, port))

except socket.gaierror:
    print("ERROR: Address-related error connecting to server")
    sys.exit(1)

except socket.error:
    print("ERROR: No connection established")
    sys.exit(1)


#Getting two commands from the connection??
i = 0
msg = b""
while i < 2:

    #Recieves commands from the server bit by bit
    while True:

        try:
            m = sock.recv(1)

        except socket.error:
            print("ERROR: could not receive data")
            sys.exit(1)

        # Connection is closed by server
        if len(m) <= 0:
            break

        msg += m

    #Checks if there was a command recorded
    if len(msg) > 0:

        if msg.find(b"accio\r\n") >= 0 and msg.find(b"accio\r\n") < len(msg):

            if i == 0:
                i += 1
                msg = b""
                sock.send("confirm-accio\r\n".encode())

            elif i == 1:
                i += 1
                msg = b""
                sock.send("confirm-accio\r\n".encode())

        # Continues to append to the mg string until
        # ... it matches the specified command
        elif len(msg) < len("accio\r\n"):
            continue



#Transfer the specified file
if i == 2:

    #Opens file in binary
    with open(file, "rb") as f:

        while True:
            fileIn = f.read(BUFFER_SIZE)

            if not fileIn:
                break

            byteSize = sock.send(fileIn)




#Ending the program
sock.close()

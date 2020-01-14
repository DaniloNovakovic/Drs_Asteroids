import select
import socket


class Server:
    def __init__(self):
        self.HOST = ''  # Symbolic name meaning all available interfaces
        self.PORT = 50005  # Arbitrary non-privileged port
        self.conn1 = None
        self.conn2 = None
        self.start_server()

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.setblocking(0)
            s.listen(2)
            print('Server opened at ' + socket.gethostbyname())
            print("waiting for clients to connect...")
            self.conn1, addr1 = s.accept()
            print(addr1 + ' connected.')
            self.conn2, addr2 = s.accept()
            print(addr2 + ' connected')

            potential_read = [self.conn1, self.conn2]
            potential_write = [self.conn1, self.conn2]
            potential_err = []
            while True:
                ready_to_read, ready_to_write, in_error = select.select(potential_read, potential_write, potential_err)

    def get_sockets_to_write_to(self, ready_to_read):
        if ready_to_read.count() == 2:
            return ready_to_read
        if ready_to_read == self.conn1:
            return self.conn2
        return self.conn1

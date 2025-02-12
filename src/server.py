from socketserver import TCPServer, BaseRequestHandler, ThreadingMixIn
import threading



# TODO: Logging

# Use a threaded tcp server, may need pool for db operation
class ThreadedTCPRequestHandler(BaseRequestHandler):

    def handle(self):
        # look up client id by API key
        # if client id is not found, return 401

        # look up how much storage is used by client id

        # calculate storage estimate of request

        # if storage + request storage is full, return 429

        # look up how much compute was used by client id in past hour

        # calculate compute estimate of request

        # if compute + request compute is full, return 429

        # perform operation

        # if compute, make entry in compute table (client id, compute used, timestamp)

        # if storage, make/moidfy intry in storage table (client id, +-storage used)



        print("Request received")
        print("request data: {}".format(self.request))
        current_thread = threading.current_thread()
        print("current thread: {}".format(current_thread.name))

        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)

        print(f"Received from {self.client_address[0]}:")
        print(self.data.decode("utf-8"))
        self.request.sendall(self.data.upper())


# TODO implement pool of connections to db
# TODO implement startup/shutdown of server
class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 1300

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    # TODO: Make class for server
    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)

        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread: ", server_thread.name)

        server.serve_forever()
    server.shutdown()


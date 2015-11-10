import socket
import struct
from HomeStation.message import DataMessage_pb2
from HomeStation.tools.tokenizer import Tokenizer


class Collector:
    def __init__(self):
        address = ('localhost', 6005)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(address)

        while 1:
            print "Listening"

            total_len = server_socket.recv(4)
            print "total_len: ", total_len
            totallen_recv = struct.unpack('>I', total_len)
            print "totallen_recv: ", totallen_recv
            totallen_recv = totallen_recv[0]
            print "totallen_recv[0]: ", str(int(totallen_recv))
            messagelen = totallen_recv - 4
            print "messagelen: ", messagelen
            message = server_socket.recv(messagelen)

            data_message = DataMessage_pb2.DataMessage()
            data_message.ParseFromString(message)

            print "[server] param1:", data_message.stationId, "param2:", data_message.timestamp

            print data_message

            tok = Tokenizer()
            token = tok.prepare_token(data_message.stationId, data_message.apiKey, data_message.timestamp)

            if tok.validate_token(data_message, token):
                print "token OK :-)"
            else:
                print "token WRONG !!!"

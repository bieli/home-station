import socket
import struct

import time

from HomeStation.message import DataMessage_pb2
from HomeStation.tools.tokenizer import Tokenizer


class Collector:
    def __init__(self, host='localhost', port=6005):
        self.host = host
        self.port = port
        address = (self.host, self.port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(address)

        m = 0
        t0 = int(time.time())
        while 1:
            print("[HOME-STATION] Collectorr listening for measurement data...")

            total_len = server_socket.recv(4)
            print("total_len: ", total_len)
            totallen_recv = struct.unpack('>I', total_len)[0]
            print("totallen_recv[0]: ", totallen_recv)
            messagelen = totallen_recv - 4
            print("messagelen: ", messagelen)
            message = server_socket.recv(messagelen * 2)

            # DEBUG
            # with open('coll.test.packet.1', 'wb') as pack:
            #     pack.write(message)

            recv_data_message = DataMessage_pb2.DataMessage()
            recv_data_message.ParseFromString(message)

            #print("[server] param1:", recv_data_message.stationId, "param2:", recv_data_message.timestamp)

            print(str(recv_data_message))

            tok = Tokenizer()
            recv_token = tok.prepare_token(recv_data_message.stationId, recv_data_message.apiKey, recv_data_message.timestamp)

            if tok.validate_token(recv_data_message, recv_token):
                print("token OK :-)")
            else:
                print("token WRONG !!!")

            m += 1
            t = int(time.time()) - t0
            print("[INFO] #### t [s]: ", t, "m [get data msg count]: ", str(int(m)))
            # if t >= t0 + 1:
            #     break


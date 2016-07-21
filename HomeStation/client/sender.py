import hashlib

import time

from HomeStation.message import DataMessage_pb2
from HomeStation.tools.tokenizer import Tokenizer


class Sender:
    def __init__(self, host='localhost', port=6005):
        self.host = host
        self.port = port

    def send_data(self, station_id, api_key, timestamp, data, alerts=None):
        data_message = DataMessage_pb2.DataMessage()
        data_message.stationId = str(station_id)
        data_message.apiKey = str(api_key)
        data_message.timestamp = int(timestamp)

        # data_items = []
        # for data_item in data:
        #     dataItem = data_message.dataItems.add()
        #     dataItem.parameterId = int(data_item['parameterId'])
        #     dataItem.value = float(data_item['value'])
        #     data_items.append(dataItem)
        #
        # data_message.dataItems.extend(data_items)

        for data_item in data:
            data_message.dataItems.add(parameterId=data_item['parameterId'], value=data_item['value'])

        # data_message.dataItemsCount = len(data)

        tok = Tokenizer()
        token = tok.prepare_token(data_message.stationId, data_message.apiKey, data_message.timestamp)

        print("token: ", token)

        data_message.token = str(token)

        # Write the new address book back to disk.
        #f = open("/tmp/test.pb2.bin", "wb")
        #f.write(data_message.SerializeToString())
        #f.close()

        # from test_msg_pb2 import test_msg
        import socket
        import struct

        address = (self.host, self.port)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.connect(address)
        data = data_message

        num_retransmits = 0
        while (num_retransmits < 5):  # send the same message 5 times
            num_retransmits = num_retransmits + 1

            serialized_message = data.SerializeToString()
            # DEBUG
            #if tok.validate_token(data_message, token):
            #    print("token OK :-)")
            #else:
            #    print("token WRONG !!!")

            print("serialized_message: ", len(serialized_message))
            totallen = 4 + len(serialized_message)
            print("totallen: ", totallen)
            pack1 = struct.pack('>I', totallen)  # the first part of the message is length
            client_socket.sendall(pack1 + serialized_message)

            # DEBUG
            # with open('send.test.packet.1', 'wb') as pack:
            #     pack.write(pack1 + serialized_message)

            print("[client] stationId: ", data.stationId, " timestamp: ", data.timestamp)
            # time.sleep(2)


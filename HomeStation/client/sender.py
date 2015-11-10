import hashlib

import time

from HomeStation.message import DataMessage_pb2
from HomeStation.tools.tokenizer import Tokenizer


class Sender:
    def __init__(self):
        pass

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

        if len(data):
            for data_item in data:
                data_message.dataItems.add(parameterId=data_item['parameterId'], value=data_item['value'])
        else:
            data_message.dataItems.add()

        # required uint64 dataItemsCount = 6;
        # data_message.dataItemsCount = len(data)

        tok = Tokenizer()

        data_message.token = str(tok.prepare_token(station_id, api_key, timestamp))

        # Write the new address book back to disk.
        f = open("/tmp/test.pb2.bin", "wb")
        f.write(data_message.SerializeToString())
        f.close()

        print data_message

        # from test_msg_pb2 import test_msg
        import socket
        import struct

        address = ('localhost', 6005)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.connect(address)
        data = data_message

        num_retransmits = 0
        while num_retransmits < 5:  # send the same message 5 times
            num_retransmits += 1

            s = data.SerializeToString()

            data_len = len(s)
            print "data_len: ", data_len
            total_len = 4 + data_len
            print "total_len: ", total_len
            pack1 = struct.pack('>I', total_len)  # the first part of the message is length
            client_socket.sendall(pack1 + s)

            print "[client] stationId: ", data.stationId, " timestamp: ", data.timestamp
            time.sleep(1)

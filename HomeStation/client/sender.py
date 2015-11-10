import hashlib

import time

from HomeStation.message import DataMessage_pb2


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

        for data_item in data:
            data_message.dataItems.add(parameterId=data_item['parameterId'], value=data_item['value'])

        # data_message.dataItemsCount = len(data)

        token = hashlib.sha256()
        token.update(str(data_message.stationId) + str(data_message.apiKey) + str(data_message.timestamp))
        token = token.hexdigest()
        print "token: ", token

        data_message.token = str(token)

        # Write the new address book back to disk.
        f = open("/tmp/test.pb2.bin", "wb")
        f.write(data_message.SerializeToString())
        f.close()

        # from test_msg_pb2 import test_msg
        import socket
        import struct

        address = ('localhost', 6005)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.connect(address)
        data = data_message

        num_retransmits = 0
        while (num_retransmits < 5):  # send the same message 5 times
            num_retransmits = num_retransmits + 1

            s = data.SerializeToString()

            totallen = 4 + len(s)
            print "totallen: ", totallen
            pack1 = struct.pack('>I', totallen)  # the first part of the message is length
            client_socket.sendall(pack1 + s)

            print "[client] stationId: ", data.stationId, " timestamp: ", data.timestamp
            # time.sleep(2)

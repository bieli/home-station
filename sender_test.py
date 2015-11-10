import time

from HomeStation.client.sender import Sender


s = Sender()
#TODO: change data na key:value list

while 1:
    s.send_data("0283429873498724283", "apiKey",
                int(time.time()), [])
    # [{'parameterId': 111, 'value': 11.0}, {'parameterId': 22, 'value': 22.0}])

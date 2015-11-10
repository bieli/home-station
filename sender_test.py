import random
import time

from HomeStation.client.sender import Sender


s = Sender()
#TODO: change data na key:value list

while 1:
    s.send_data("0283429873498724283", "apiKey",
                int(time.time()), [{'parameterId': random.randint(1, 1000000), 'value': 11.1}, {'parameterId': random.randint(1, 1000000), 'value': 22.02}])

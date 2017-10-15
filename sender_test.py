import random
import time
import requests

from HomeStation.client.sender import Sender


def test_socket_protobuf_custom(benchmark):
    s = Sender()
    benchmark.pedantic(s.send_data, args=("0283429873498724283", "apiKey", int(time.time()), [{'parameterId': random.randint(1, 1000000), 'value': 22.02}]), iterations=1000, rounds=100)
    assert 1 == 1

def test_http_json_basehttpserver(benchmark):
    url = 'http://localhost:8888/api/v1/addrecord/1'
    payload = {"parameterId": 1, "value": 1.0, "stationId":"0283429873498724283", "apiKey":"", "ts": int(time.time())}

    #r = requests.post(url, json=payload)
    benchmark.pedantic(requests.post, args=(url, payload, {'Content-Type': 'application/json'}), iterations=1000, rounds=100)
    assert 1 == 1


def test_http_json_flask(benchmark):
    url = 'http://localhost:8887/api/v1/addrecord/1'
    payload = {"parameterId": 1, "value": 1.0, "stationId":"0283429873498724283", "apiKey":"", "ts": int(time.time())}

    #r = requests.post(url, json=payload)
    benchmark.pedantic(requests.post, args=(url, payload, {'Content-Type': 'application/json'}), iterations=1000, rounds=100)
    assert 1 == 1


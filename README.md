# HOME STATION [![Build Status](https://travis-ci.org/bieli/home-station.png)](https://travis-ci.org/bieli/home-station) #
===================

HOME STATION - client and server data measurement with PROTOBUF protocol


What is this ?
--------------
Prototype code for internal web services data messages in home automation, SCADA and things like that solutions.


Implementation TODO list
-------------
 - [x] git ignore
 - [x] travis CI
 - [x] protocol definition and generation script in standard PROTOBUF way
 - [ ] unit tests
 - [x] runnable code prototype PoC
 - [x] simple socket test client/server example based on PROTO
 - [ ] socket client/server with exceptions and all error handling
 - [ ] functional test automation
 - [ ] *temperature and humidity measurement in home with zones* (practical implementation in home automation)


Basic PROTOCOL definition for preparing all types of typical values in measurement
-------------

```
$ protoc --version
libprotoc 2.6.1

$ python
>>> import google.protobuf
>>> google.protobuf.__version__
'3.0.0a3'
```

DataMessage.proto
```
option py_generic_services = true;
option optimize_for = SPEED;
option java_package = "net.bieli.HomeStation.protocol.protobuf.DataMessage";

package ProtobufDataMessage;

message DataMessage {
  required string stationId = 1;
  required string apiKey = 2;
  required string token = 3;
  required uint32 timestamp = 4;
  repeated DataItem dataItems = 5;

  enum Alert {
    CRITICAL_HIGH = 3;
    TOO_HIGH = 2;
    HIGH = 1;
    NO_ALERT = 0;
    LOW = -1;
    TOO_LOW = -2;
    CRITICAL_LOW = -3;
  }

  message DataItem {
    required uint32 parameterId = 1;
    required float value = 2;
    optional Alert alert = 3 [default = NO_ALERT];
  }
}
```


Example first PRE-ALPHA test runs:
-------------------

Run on first console client sender test proccess:

```
$ python sender_test.py

token:  222637d764dc605239118043203d6a5a50990354823dee19f4336650df7ff796
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1447198307
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1447198307
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1447198307
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1447198307
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1447198307
```

and try run on another console run server collector consumer proccess:

```
$ python collector_test.py


Listening
total_len: 
totallen_recv[0]:  127
messagelen:  123
[server] param1: 0283429873498724283 param2: 1447198307
stationId: "0283429873498724283"
apiKey: "apiKey"
token: "222637d764dc605239118043203d6a5a50990354823dee19f4336650df7ff796"
timestamp: 1447198307
dataItems {
  parameterId: 563130
  value: 11.1000003815
}
dataItems {
  parameterId: 938785
  value: 22.0200004578
}

token OK :-)
[INFO] #### t [s]:  29 m [get data msg count]:  45374
```

Wow, on local machine with simple sockets server solution performance: *~1.5 k recv messages per second* (45374 [ recv messages] / 29 [s])

Good enough for home automation solution.
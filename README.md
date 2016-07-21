# HOME STATION [![Build Status](https://travis-ci.org/bieli/home-station.png)](https://travis-ci.org/bieli/home-station) [![Coverage](https://coveralls.io/repos/bieli/home-station/badge.png?branch=master)](https://coveralls.io/r/bieli/home-station?branch=master) #
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
 - [x] migrationg codebase to Python 3.4 from Python 2.7
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


How to install
--------------

```
$ sudo pip3.4 install -r requirements.txt 
```


Example first PRE-ALPHA test runs:
-------------------

Run on first console client sender test proccess:

```
$ python sender_test.py

[client] stationId:  0283429873498724283  timestamp:  1469138864
token:  4dda93cd0cd983157eb733fc6b366d0403b8b8fea67cd3cbba578a0b26113326
serialized_message:  123
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1469138864
serialized_message:  123
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1469138864
serialized_message:  123
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1469138864
serialized_message:  123
totallen:  127
[client] stationId:  0283429873498724283  timestamp:  1469138864
serialized_message:  123
totallen:  127
```

and try run on another console run server collector consumer proccess:

```
$ python collector_test.py


[HOME-STATION] Collectorr listening for measurement data...
total_len:  b'\x00\x00\x00\x7f'
totallen_recv[0]:  127
messagelen:  123
stationId: "0283429873498724283"
apiKey: "apiKey"
token: "4dda93cd0cd983157eb733fc6b366d0403b8b8fea67cd3cbba578a0b26113326"
timestamp: 1469138864
dataItems {
  parameterId: 590653
  value: 11.100000381469727
}
dataItems {
  parameterId: 822252
  value: 22.020000457763672
}

token OK :-)
[INFO] #### t [s]:  92 m [get data msg count]:  181802
```


Quasi-performance speed tests info
----------------------------------

Wow, on local machine with simple sockets server solution performance: *1976 recv messages per second* (181802 [ recv messages] / 92 [s])

Good enough for home automation solution :-)


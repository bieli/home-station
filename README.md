# HOME STATION [![Build Status](https://travis-ci.org/bieli/home-station.png)](https://travis-ci.org/bieli/home-station) [![Coverage Status](https://coveralls.io/repos/github/bieli/home-station/badge.svg?branch=master)](https://coveralls.io/github/bieli/home-station?branch=master) #
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


Performance servers comparisions
----------------------------------

On local machine with simple sockets server solution performance: *1976 recv messages per second* (181802 [ recv messages] / 92 [s])

Good enough for home automation solution :-)

By using BaseHttpServer nad Flask HTTP server in benchamrking we can view how high is performence when we using SOCKETS and PROTOBUF combination.

```

$ py.test sender_test.py --benchmark-histogram
=================================================================================== test session starts ===================================================================================
platform linux -- Python 3.4.5, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/mbielak/Pulpit/_priv/projects/home-station, inifile: 
plugins: cov-2.2.1, benchmark-3.1.1, celery-4.0.2
collected 3 items 

sender_test.py ...


------------------------------------------------------------------------------------------------ benchmark: 3 tests ------------------------------------------------------------------------------------------------
Name (time in us)                        Min                   Max                  Mean              StdDev                Median                 IQR            Outliers         OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_socket_protobuf_custom         496.7924 (1.0)        695.7684 (1.0)        624.7026 (1.0)       40.9030 (1.0)        630.7166 (1.0)       50.6049 (1.0)          26;5  1,600.7616 (1.0)         100        1000
test_http_json_basehttpserver     2,431.6774 (4.89)     3,101.0362 (4.46)     2,834.8904 (4.54)      95.0810 (2.32)     2,829.8358 (4.49)     103.5050 (2.05)         23;5    352.7473 (0.22)        100        1000
test_http_json_flask              3,245.0367 (6.53)     4,231.0539 (6.08)     3,885.8517 (6.22)     184.3730 (4.51)     3,892.7702 (6.17)     237.9043 (4.70)         28;2    257.3438 (0.16)        100        1000
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Generated histogram: benchmark_20171015_145020.svg
Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
====================================================================== 3 passed, 1 pytest-warnings in 735.03 seconds ======================================================================

```

Graphical view of performance:


![alt text](https://raw.githubusercontent.com/bieli/home-station/master/benchmark_20171015_145020.png)


Additionally view of performance with Golang REST/HTTP server (based on Gorilla):


![alt text](https://raw.githubusercontent.com/bieli/home-station/master/benchmark_20171015_194125.png)



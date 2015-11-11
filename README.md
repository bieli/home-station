HOME STATION - client and server data measurement with PROTOBUF protocol
-----------------------------------------------------------------------

Prototype code for internal web services data messages in home automation, scada and things like that solutions.


Example test runs:
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
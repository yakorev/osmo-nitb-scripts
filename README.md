### Osmocom scripts

 Scripts for easy launch and some interesting functions. For testing purpose only!

  - Basic osmo-nitb GSM network
  - GSM with egprs
  - USSD-broadcast
  - SMS-broadcast
  - SMS-spam ;)

All software was tested on [LimeSDR-Mini + Orange Pi Zero](https://codeby.net/threads/miniatjurnaja-sotovaja-stancija-na-baze-limesdr-mini-i-orange-pi-zero.66747/) with Armbian Bionic

### Requirements
For network
```
osmo-trx-lms
osmocom-nitb
osmo-bts-trx
osmo-ggsn
osmo-sgsn
osmo-pcu
```
for scripts
```
python-sqlite3
python-telnetlib
```
### Usage
Start basic GSM network with with LimeSDR-Mini
```sh
# ./start_bts.sh
```
Start GSM network with EGPRS support (2.75G)
```sh
# start_bts_egprs.sh
```
Show all registered users
```sh
$ ./show_subscribers.py
```

send USSD message to all subscribers in the network
```sh
$ ./ussd_broadcast.py [0|1|2] [.MESSAGE]
```
send SMS message to all subscribers in the network from selected extension
```sh
$ ./sms_broadcast.py [extension] [.MESSAGE]
```
send sms from random numbers to selected extension
```sh
$ ./sms_spam.py [extension] [num of repeats] [.MESSAGE]
```


License
----

WTFPL

**Free Software, Hell Yeah!**

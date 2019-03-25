### Osmocom scripts

 This project is created for easy deployment of Osmocom GSM stack and contains some interesting scripts for interaction with users 

  - Basic osmo-nitb GSM network
  - GSM with egprs
  - GSM with Asterisk support
  - interaction with new users, like sms, ussd or autocall
  - USSD-broadcast
  - SMS-broadcast
  - SMS-spam ;)

All software was tested on [LimeSDR-Mini + Orange Pi Zero](https://codeby.net/threads/miniatjurnaja-sotovaja-stancija-na-baze-limesdr-mini-i-orange-pi-zero.66747/) with Armbian Bionic and Debian 9

### Requirements
For network
```
osmo-trx-lms
osmocom-nitb
osmo-bts-trx
osmo-ggsn
osmo-sgsn
osmo-pcu
osmo-sip-connector
libsofia-sip-ua-glib-dev
asterisk
```
for scripts
```
python-sqlite3
python-telnetlib
```
### Asterisk support
First of all, you need to configure and start asterisk. Asterisk must be running, before you start ```start_bts_sip.sh```
Basic configs for Asterisk:
- sip.conf
```
[GSM]
type=friend
host=10.9.1.110
dtmfmode=rfc2833
canreinvite=no
disallow=all
allow=gsm
context=gsmsubscriber
port=5069
```
- extensions.conf
```
[gsmsubscriber]
exten=>_XXXXX,1,Dial(SIP/GSM/${EXTEN})
exten=>_XXXXX,n,Playback(vm-nobodyavail)
exten=>_XXXXX,n,HangUp
```

### Usage
You can start classic GSM Network, GSM with (e)gprs (2.75G), or osmocom with Asterisk support.

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
### Monitor
```monitor``` shows all online subscribers and execute user-interactive script, when new phone is connected to the network. For example, it an be hello-message, ussd, or call from bot. The behavior of interactivity with new users is described in the ```config.json``` file.




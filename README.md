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
exten=>_XXX,1,Dial(SIP/GSM/${EXTEN})
exten=>_XXX,n,Playback(vm-nobodyavail)
exten=>_XXX,n,HangUp
```

### Usage
You can start classic GSM Network, GSM with (e)gprs (2.75G), or osmocom with Asterisk support.
```
# ./start_bts
```
```
# ./start_bts_egprs
```
```
# ./start_bts_sip
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
### Monitor
```monitor``` shows all online subscribers and execute user-interactive script, when new phone is connected to the network. For example, it can be SMS hello-message, USSD, or call from bot. The behavior of interactivity with new users is described in the ```config.json``` file.

![alt text](https://raw.githubusercontent.com/DrLafa/osmo-nitb-scripts/master/monitor.png)

### config.json
For easy setup of user-interactivity you can use config.json
- config.json example
```
{
   "scripts":{
      "sms":{
         "enabled": false,
         "sender_extension": 1337,
         "message":[
            "If you are reading this, then you are resistance"
         ]
      },
      "ussd":{
         "enabled": false,
         "ussd_type": 1,
         "message":[
            "Welcome to our l33t hax0r network.",
            "If you are reading this, then you are true L33T 1337 H4xXx0r"
         ]
      },
      "call":{
         "enabled": true,
         "caller_extension": 666,
         "voice-file": "tt-monkeys"
      }
   }
}
```
#### sms
Send sms to new users. When user connect to network, script choose 1 random message from ```message``` section and sending it from extension ```sender_extension```

#### ussd
Send ussd to new users. Script choose 1 random message from ```message``` section adn sending it to user

#### call
Make a call to new user. This function works only with Asterisk support. voice-file is 16-bit 8 kHz wav file. If ```caller_extension``` is false, then the user sees that the phone is not defined.

#!/bin/sh
iptables -A POSTROUTING -s 176.16.1.0/24 -t nat -o wlan0 -j MASQUERADE
sysctl -w kernel.sched_rt_runtime_us=-1
cd configs

osmo-ggsn &
GGSN=$!

osmo-sgsn &
SGSN=$!

osmo-nitb -c openbsc_egprs.cfg &
NITB=$!

chrt -rr 99 osmo-trx-lms &
TRX=$!
sleep 5

osmo-bts-trx &
BTS=$!

sleep 1
osmo-pcu &
PCU=$!

wait $GGSN $SGSN $NITB $BTS $TRX $PCU

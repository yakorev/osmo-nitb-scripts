#!/bin/sh
sysctl -w kernel.sched_rt_runtime_us=-1

osmo-nitb -c configs/openbsc.cfg -M /tmp/msc_mncc &
NITB=$!

osmo-sip-connector -c configs/osmo-sip-connector.cfg &
SIP=$!

chrt -rr 99 osmo-trx-lms -C configs/osmo-trx.cfg &
TRX=$!
sleep 5

osmo-bts-trx -c configs/osmo-bts.cfg &
BTS=$!

wait $NITB $BTS $TRX
wait 4
kill $SIP
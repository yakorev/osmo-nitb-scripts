#!/bin/sh
sysctl -w kernel.sched_rt_runtime_us=-1
cd configs

osmo-nitb &
NITB=$!

chrt -rr 99 osmo-trx-lms &
TRX=$!
sleep 5

osmo-bts-trx &
BTS=$!

wait $NITB $BTS $TRX


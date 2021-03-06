#!/bin/sh
sysctl -w kernel.sched_rt_runtime_us=-1

osmo-nitb -c configs/openbsc.cfg &
NITB=$!

chrt -rr 99 osmo-trx-lms -C configs/osmo-trx.cfg &
TRX=$!
sleep 5

osmo-bts-trx -c configs/osmo-bts.cfg &
BTS=$!

wait $NITB $BTS $TRX
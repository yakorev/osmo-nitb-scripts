sudo su -c "echo \"1\" > /proc/sys/net/ipv4/ip_forward"
iptables -A POSTROUTING -s 176.16.1.1/24 -t nat -o wlan0 -j MASQUERADE
sysctl -w kernel.sched_rt_runtime_us=-1

osmo-ggsn -c configs/osmo-ggsn.cfg &
GGSN=$!

osmo-sgsn -c configs/osmo-sgsn.cfg &
SGSN=$!

osmo-nitb -c configs/openbsc_egprs.cfg &
NITB=$!

chrt -rr 99 osmo-trx-lms -C configs/osmo-trx.cfg &
TRX=$!
sleep 10

osmo-pcu -c configs/osmo-pcu.cfg &
PCU=$!

osmo-bts-trx -c configs/osmo-bts.cfg &
BTS=$!

wait $GGSN $SGSN $NITB $BTS $TRX $PCU

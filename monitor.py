#!/usr/bin/env python3
import sqlite3
import time
import os, sys
import signal
import user_interact

def signal_handler(sig, frame):
	#os.system("sudo rm {}".format("hlr.sqlite3"))
	print("\n"*10)
	print("Exiting...")
	sys.exit(0)

def execute_script(user):
        time.sleep(2)
        print("executing script...")
        extension = user[5]
        user_interact.interact(extension)

def update_monitor(users):
	data  = "ID\t\tcreated\t\tIMSI\t\t\tTMSI\t\tnumber\n\n"
	data += "-"*80
	data += "\n\n"

	for sub in users:
		user_data = "{0:1}\t{1:2}\t{2:<15}\t\t{3:<10}\t{4}".format(
					sub[0],
					sub[1],
					sub[3],
					sub[7],
					sub[5]
					)
		data += user_data
		data += "\n"

	print ("\x1b[2J")
	print(data)
	print ("\x1b[{};{}H".format(0, 0))

def start_monitor(hlr_loc):
	os.system('clear')
	signal.signal(signal.SIGINT, signal_handler)

	db = sqlite3.connect(hlr_loc)
	c = db.cursor()

	subscribers = []
	TMSIs = []

	while 1:
		time.sleep(1)
		for user in c.execute("SELECT * FROM Subscriber"):
			if user[7] not in TMSIs and user[7] != None:
				TMSIs.append(user[7])
				subscribers.append(user)

				execute_script(user)

		update_monitor(subscribers)


if __name__ == "__main__":
	if len(sys.argv) == 2:
		hlr_loc = sys.argv[1]
	else:
		hlr_loc = "hlr.sqlite3"

	signal.signal(signal.SIGINT, signal_handler)

	start_monitor(hlr_loc)
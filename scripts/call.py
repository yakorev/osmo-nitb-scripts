#!/usr/bin/env python3
import os

def call(caller_extension, extension, voice_file):
	if not caller_extension:
		caller_extension = ""
	call_data = """Channel: SIP/GSM/{}
MaxRetries: 10
RetryTime: 10
WaitTime: 30
CallerID: {}
Application: Playback
Data: {}""".format(extension, caller_extension, voice_file)

	call_file = "{}.call".format(extension)
	with open(call_file, "w") as call_data:
		call_data.write(call_file)
		call_data.close()

	os.system("chown asterisk:asterisk {}".format(call_file))
	os.system("mv {} /var/spool/asterisk/outgoing/".format(call_file))
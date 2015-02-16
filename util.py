# $language = "python"
# $interface = "1.0"

# util.py
#
# Description: this is a tool class which provides common method

# impengpeng


import os
import subprocess

# open directory where the file is
def LaunchViewer(filename):
	try:
		os.startfile(filename)
	except AttributeError:
		subprocess.call(['open', filename])
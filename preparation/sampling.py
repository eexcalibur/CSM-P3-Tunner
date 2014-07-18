from core.commpara import commpara
import parse_config
import sys
import os

#handle preparation module
print commpara.preparation_method

#handle sampling method, using psuade tool
if (commpara.preparation_method == "sampling"):
	if (os.path.isfile(commpara.preparation_config) == False):
		print "preparation module config file does not exit!"
		sys.exit()


	sys.exit()
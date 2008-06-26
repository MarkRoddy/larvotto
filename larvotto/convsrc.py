"""
A set of functions for retrieving previous instant message conversations.
All functions return an interable whose items are tuples in the form of:
(date/time,screenname,message)
"""

import os


def PidginLogs(LogDir):
	"""Returns all conversations by parsing Pidgin log files"""
	assert os.path.isdir(LogDir), 'Not a directory: '+str(LogDir)
	

    

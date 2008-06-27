"""
A set of functions for retrieving previous instant message conversations.
All functions return an interable whose items are tuples in the form of:
(date/time,screenname,message)
"""

import os,re
from datetime import datetime


def PidginLogs(LogDir):
	"""Returns all conversations by parsing Pidgin log files"""
	assert os.path.isdir(LogDir), 'Not a directory: '+str(LogDir)
	messages=[]
	recordre=re.compile(r'^\((\d\d\:\d\d\:\d\d\s+[A|P]M)\)\s+(.*?)\:\s+(.*)\s*$', re.I|re.L)
	for d in [LogDir+os.sep+f for f in os.listdir(LogDir) if os.path.isdir(LogDir+os.sep+f)]:
		for logf in os.listdir(d):
			doy=logf.split('.')[0]
			logf=d+os.sep+logf
			for rec in open(logf).readlines()[1:]:
				m=recordre.search(rec.strip()) 
				if not m:
					raise ValueError("malformed log record: '%s'"%rec.strip())
				tod,scrnname,msg=m.groups()
				dtime=datetime.strptime('%s %s'%(doy,tod), '%Y-%m-%d %I:%M:%S %p')
				messages.append( (dtime,scrnname,msg,) )
	return messages

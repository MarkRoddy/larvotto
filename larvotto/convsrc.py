"""
A set of functions for retrieving previous instant message conversations.
All functions return an interable whose items are tuples in the form of:
(date/time,screenname,message)
"""

import os,re
from datetime import datetime

recordre=re.compile(r'^\((\d\d?\:\d\d\:\d\d(\s+[A|P]M)?)\)\s+(.*?)\:\s+(.*)\s*$', re.I|re.L)

def PidginLogs(LogDir):
	"""Returns all conversations by parsing Pidgin log files"""
	assert os.path.isdir(LogDir), 'Not a directory: '+str(LogDir)
	messages=[]
	for d in [LogDir+os.sep+f for f in os.listdir(LogDir) if os.path.isdir(LogDir+os.sep+f)]:
		for logf in os.listdir(d):
			doy=logf.split('.')[0]
			logf=d+os.sep+logf
			for rec in open(logf).readlines()[1:]:
				t=_ParsePidginRecord(rec,doy)
				if t:
					messages.append(t)
				elif not _IsSystemMessage(rec):
					pass
					#print "malformed log record '%s'"%rec
					#raise ValueError("malformed log record '%s' in file '%s'"%(rec,logf))
	return messages


def _ParsePidginRecord(recordtext,dayofyear):
	m=recordre.search(recordtext.strip())
	if not m:
		return
	tod,isampm,scrnname,msg=m.groups()
	if isampm:
		dtime=datetime.strptime('%s %s'%(dayofyear,tod), '%Y-%m-%d %I:%M:%S %p')	
	else:
		dtime=datetime.strptime('%s %s'%(dayofyear,tod), '%Y-%m-%d %H:%M:%S')
	return (dtime,scrnname,msg,)

_SysMsgSuffixes=[
	'has signed off.',
	'has signed on.',
	'logged out.',
	'logged in.',
	'is no longer idle.',
	'has become idle.',
	'has gone away.',
	'is no longer away.',
	'entered the room.',
	'left the room.',
	]

def _IsSystemMessage(recordtext):
	recordtext=recordtext.strip()
	for sfx in _SysMsgSuffixes:
		if recordtext.endswith(sfx):
			return True
	return False
	
#def _loadmap(self, filename):
	#each entry in the word map is a (precision+1)-tuple
	#each word of the precision, plus the number of occurrences
	#wordmap={}
	
	# when using the new, loaded map, use (precision-1) tokens, and get the possible next ones and their frequency, and randomly choose one given the frequency
	
	#self._precision= FROM FILE
	
	#for line in file 
	#	

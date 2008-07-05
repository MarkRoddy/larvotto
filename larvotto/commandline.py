"""Utilities for working with Larvotto from the command line"""

import larvotto
import larvotto.bot
import larvotto.response
import larvotto.convsrc
from optparse import OptionParser
from getpass import getpass
import sys,os

def main():
	"""Runs the Larvotto bot"""
	if sys.platform[:3]=='win':
		logsrc='C:\\Documents and Settings\\%s\\Application Data\\.purple\\logs\\aim'
	else:
		logsrc='/home/%s/.purple/logs/aim'
	logsrc=logsrc%os.environ['USERNAME']
	p=OptionParser(usage='%prog [options] screenname',version='%progv'+larvotto.__version__)
	p.add_option('-p','--password',dest='passwd',default='',help='Specify Password at Commandline')
	p.add_option('-l','--logsource',dest='logsource',default=logsrc,help='Path to Pidgin log files to train from')
	p.add_option('-c','--chain-length',dest='chainlen',default=2,help='Length of the markov chain used')
	p.add_option('-a','--alt-screenname',dest='altscn',default='',help="Username who's logged messages seed the markov chain.")
	(opts,args)=p.parse_args()
	if 1!=len(args):
		p.print_help()
		sys.exit(1)
	else:
		if opts.passwd:
			passwd=opts.passwd
		else:
			passwd=getpass('Password: ')
		screenname=args[0]
		if opts.altscn:
			altscn=opts.altscn
		else:
			altscn=screenname
		records=larvotto.convsrc.PidginLogs(opts.logsource+os.sep+altscn)
		larvotto.bot.Start(screenname, passwd, larvotto.response.MarkovChain(altscn,records,opts.chainlen))

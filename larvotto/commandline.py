"""Utilities for working with Larvotto from the command line"""

import larvotto
import larvotto.bot
import larvotto.response
import larvotto.convsrc
from optparse import OptionParser
from getpass import getpass
import sys

def main():
	"""Runs the Larvotto bot"""
	p=OptionParser(usage='%prog [options] screenname',version='%progv'+larvotto.__version__)
	p.add_option('-p','--password',dest='passwd',default='',help='Specify Password at Commandline')
	p.add_option('-l','--logsource',dest='logsource',default='C:\Documents and Settings\Jean\Application Data\.purple\logs\\aim\sketchyd1',help='Please provide the path to the log files to train from')
	(opts,args)=p.parse_args()
	if 1!=len(args):
		p.print_help()
		sys.exit(1)
	else:
		if opts.passwd:
			passwd=opts.passwd
		else:
			passwd=getpass('Password: ')
		records = larvotto.convsrc.PidginLogs(opts.logsource)
		larvotto.bot.Start(args[0],passwd,larvotto.response.MarkovChain(records))

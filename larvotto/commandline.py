"""Utilities for working with Larvotto from the command line"""

import larvotto
import larvotto.bot
import larvotto.response
from optparse import OptionParser
from getpass import getpass
import sys

def main():
	"""Runs the Larvotto bot"""
	p=OptionParser(usage='%prog [options] screenname',version='%progv'+larvotto.__version__)
	p.add_option('-p','--password',dest='passwd',default='',help='Specify Password at Commandline')
	(opts,args)=p.parse_args()
	if 1!=len(args):
		p.print_help()
		sys.exit(1)
	else:
		if opts.passwd:
			passwd=opts.passwd
		else:
			passwd=getpass('Password: ')
		larvotto.bot.Start(args[0],passwd,larvotto.response.Echo())

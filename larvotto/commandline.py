"""Utilities for working with Larvotto from the command line"""

import larvotto

from optparse import OptionParser
import sys

def main():
	"""Runs the Larvotto bot"""
	p=OptionParser(version='%progv'+larvotto.__version__)
	p.add_option('-p','--password',dest='passwd',help='Specify Password at Commandline')
	(opts,args)=p.parse_args()
	if 1!=len(args):
		print p.usage
		sys.exit(1)

	
	

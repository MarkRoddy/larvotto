"""Unit tests for the L{larvotto.convsrc} module"""

import unittest
import larvotto.convsrc


class TestPidginLogs(unittest.TestCase):
	"""Test case for the L{larvotto.convsrc.PidginLogs} function"""


	def testNonDirectoryPath(self):
		if __debug__:
			self.assertRaises(AssertionError, larvotto.convsrc.PidginLogs, '')


	def testSingleDigitHour(self):
		record='(1:12:16 PM) MyScreenName: test'
		d='2008-07-05'
		larvotto.convsrc._ParsePidginRecord(record,d)


if __name__=='__main__':
	unittest.main()

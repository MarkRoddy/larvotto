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

	def testNoAMPM(self):
		record='(22:20:45) MyScreeName: those are some tasty burgers'
		d='2008-07-05'
		larvotto.convsrc._ParsePidginRecord(record,d)

	def testSignOffSystemMessage(self):
		msg='(1:42:07 PM) AIMsweringMachin has signed off.'
		self.assert_(larvotto.convsrc._IsSystemMessage(msg))

	def testLoggedOffSystemMessage(self):
		msg='(04:34:28) Ahs123 logged out.'
		self.assert_(larvotto.convsrc._IsSystemMessage(msg))

	def testSignOffSystemMessageWithWhiteSapce(self):
		msg='(1:42:07 PM) AIMsweringMachin has signed off.   '
		self.assert_(larvotto.convsrc._IsSystemMessage(msg))

	def testLoggedInSystemMessage(self):
		msg='(00:51:44) Ahs123 logged in.'
		self.assert_(larvotto.convsrc._IsSystemMessage(msg))

if __name__=='__main__':
	unittest.main()

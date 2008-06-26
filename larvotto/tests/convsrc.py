"""Unit tests for the L{larvotto.convsrc} module"""

import unittest
import larvotto.convsrc


class TestPidginLogs(unittest.TestCase):
    """Test case for the L{larvotto.convsrc.PidginLogs} function"""


    def testNonDirectoryPath(self):
        if __debug__:
            self.assertRaises(AssertionError, larvotto.convsrc.PidginLogs, '')




if __name__=='__main__':
    unittest.main()

"""Unit tests for the L{larvotto.bot} module"""

import unittest
import larvotto.response
from larvotto.bot import MarkovBot

class TestMarkovBot(unittest.TestCase):



    def setUp(self):
		self.bot=MarkovBot('foo','bar',larvotto.response.Echo())


    def testInit(self):
        if __debug__:
			self.assertRaises(AssertionError, larvotto.bot.MarkovBot,'','',None)












if __name__=='__main__':
	unittest.main()

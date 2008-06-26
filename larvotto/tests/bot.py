

import unittest
import larvotto.bot

class TestMarkovBot(unittest.TestCase):



    def setUp(self):
		pass
		#self.bot=larvotto.bot.MarkovBot('foo','bar',None)


    def testInit(self):
        if __debug__:
			self.assertRaises(AssertionError, larvotto.bot.MarkovBot,'','',None)












if __name__=='__main__':
	unittest.main()

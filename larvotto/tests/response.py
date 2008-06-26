"""Unit tests for the L{larvotto.response} module"""

import unittest
import larvotto.response


class EchoTest(unittest.TestCase):
	"""Unit test for the L{larvotto.response.Echo} class"""

	def setUp(self):
		self.resp=larvotto.response.Echo()

	def testGetEcho(self):
		s='Some Message To Echo'
		self.assertEquals(s,self.resp.get('user',s))


if __name__=='__main__':
	unittest.main()

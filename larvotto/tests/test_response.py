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



class MarkovTest(unittest.TestCase):
	"""Unit test for the L{larvotto.response.MarkovChain} class"""
	precision=2
	convos=[
		(None,'me', "hey, how's it going"),
		(None,'you',"ah ok I guess"),
		(None,'me', "did you see the show?"),
		(None,'you',"no it was sold out"),
		(None,'me','Yes!')]

	def setUp(self):
		self.resp=larvotto.response.MarkovChain('me',self.convos,self.precision)

	def testGet(self):
		resp=self.resp.get('you','hey there')
		self.assert_(isinstance(resp,basestring))
		self.assertNotEquals(0, len(resp))


	def testAddSentenceToMap(self):
		words='Hello this is a sentence that should be parsed repeat should be parsed again'.lower().split()
		wordmap={}
		precision=2
		larvotto.response.MarkovChain._addSentenceToMap(wordmap, words, precision)
		for chain in wordmap.keys():
			self.assert_(isinstance(chain,tuple))
			self.assertEquals(precision,len(chain))
			wordlist=wordmap[chain]
			self.assert_(isinstance(wordlist,list))
			for val in wordlist:
				self.assert_(val is None or isinstance(val,basestring), str(type(val)))
		self.assertEquals(wordmap[('hello','this')], ['is'])
		self.assertEquals(wordmap[('parsed','again')],[None])
		self.assertEquals(wordmap[('should','be')],['parsed',]*2)
		self.assertEquals(wordmap[('be','parsed')],['repeat','again'])
                        


if __name__=='__main__':
	unittest.main()

"""Provides routines for generating different responses to incoming messages"""

import random

class BaseResponse(object):
	"""Defines the interface from which all 'response' objects must inherit"""

	def get(self,scnname,msg):
		"""Get a response to an incoming instant message"""
		raise NotImplementedError


class Echo(BaseResponse):
	"""Echos the incoming message back to the user"""

	@staticmethod
	def get(scnname,msg):
		return msg

class MarkovChain(BaseResponse):
	"""
	Generates a response to a user message using markov chain text generation
	For this basic implementation, all previous messages sent by the user are
	used to seed the markov chain.
	"""

	_screenname=None
	_precision=None

	def __init__(self, ScreenName, ConvoRecords, precision=4):
		"""
		ConvoRecords is a list of tuples in the form of (datetime,screenname,message)
		"""
		self._buildmap([r for r in ConvoRecords if r[1].upper()==ScreenName.upper()], precision)
		self._screenname=ScreenName
		self._precision=precision

	def _buildmap(self, records, precision):
		wordmap={}
		for r in records:
			words=r[2].lower().split()
			self._addSentenceToMap(wordmap, words, precision)
				
		self.wordmap=wordmap

	@staticmethod
	def _addSentenceToMap(wordmap, words, precision):
		wordst=[None,]*precision
		wordst.extend(words)
		words=wordst
		i=0
		while (i+precision) < len(words):
			wordmap.setdefault(tuple(words[i:i+precision]),[]).append(words[i+precision])
			i+=1
		wordmap.setdefault(tuple(words[-precision:]),[]).append(None)


	def get(self,scnname,msg):
		resp=[None,]*self._precision
		newword=random.choice(self.wordmap[tuple(resp[-self._precision:])])
		while newword:
			newword=random.choice(self.wordmap[tuple(resp[-self._precision:])])
			resp.append(newword)
		return ' '.join([w for w in resp if w])

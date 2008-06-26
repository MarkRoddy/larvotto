"""Provides routines for generating different responses to incoming messages"""


import larvotto.convsrc

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

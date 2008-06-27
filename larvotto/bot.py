"""Implements the instant messager bot that handles communication"""


from twisted.words.protocols import toc
from twisted.internet import reactor, protocol
import twisted.words.im.tocsupport as ts

import larvotto.response
import time

class MarkovBot(toc.TOCClient):
	"""
    Handles all IM connection and event issues
	Also, twisted is lame and won't give you access to the object that it
	constructs, this is why the __call__ method is override to simulate a
    constructor
	"""

	_resp=None

	def __init__(self,response):
		assert isinstance(response,larvotto.response.BaseResponse)
		self._resp=response

	def __call__(self,*args,**kwargs):
		toc.TOCClient.__init__(self,*args,**kwargs)
		return self

	def hearMessage(self,username, message, autoreply):
		#Override base class method
		self.say(username,self._resp.get(username,message))


def Start(ScreenName,Passwd,ResponseObj):
	"""Starts the bot"""
	cc = protocol.ClientCreator(reactor, MarkovBot(ResponseObj), ScreenName, Passwd)
	cc.connectTCP("toc.oscar.aol.com", 9898)
	reactor.run()


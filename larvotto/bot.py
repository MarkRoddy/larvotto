"""Implements the instant messager bot that handles communication"""

from toc import TocTalk,BotManager
import larvotto.response
import time

class MarkovBot(TocTalk):
	"""Handles all IM connection issues"""

	_resp=None

	def __init__(self,scnname,passwd,response):
		"""
		@param scnname: AIM Screen Name
		@param passwd: AIM password
		@param markov:
		"""
		assert isinstance(response,larvotto.response.BaseResponse)
		TocTalk.__init__(self,scnname,passwd)
		self._resp=response


	def on_IM_IN(self,data):
		#Override base class method
		self.do_SEND_IM(self._resp.get(*date.split(':')))


def Start(ScreenName,Passwd,ResponseObj):
	"""Starts the bot"""
	b=MarkovBot(ScreenName,Passwd,ResponseObj)
	bm=BotManager()
	bm.addBot(b,"MarkovBot")
	time.sleep(4)  # time to login
	b.go()

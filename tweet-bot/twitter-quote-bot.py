# -*- coding: utf-8 -*-

''' 
Requirements:

https://github.com/bufferapp/buffer-python
https://bufferapp.com/developers/apps/create


Copyright Programming for Marketers, Justin Mares and Nathaniel Eliason, 2015
Free for use with attribution
'''


from buffpy.managers.profiles import Profiles
from buffpy.managers.updates import Updates
from buffpy.api import API
from bufferinfo import *
from quote_bot_quotes import *
import random

api = API(client_id=CLIENTID,
          client_secret=CLIENTSECRET,
          access_token=ACCESSTOKEN)

profile = Profiles(api=api).filter(service='twitter')[0]

"""
def add_quotes_to_buffer(count):
	bufferQuotes = random.sample(quotes, count)

	for j in bufferQuotes:
		try:
			profile.updates.new(j, now=False)
		except:
			add_quotes_to_buffer(1)
"""
def add_content_to_buffer(count):
	bufferContent = random.sample(content, count)

	for j in bufferContent:
		try:
			profile.updates.new(j, now=False)
		except:
			add_content_to_buffer(1)


if __name__ == "__main__":
	#add_quotes_to_buffer(2)
	add_content_to_buffer(1)
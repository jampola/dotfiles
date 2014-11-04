#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import time
import os
import sys

class weatherData:
	def __init__(self):
		self.current_temp = ""
		self.current_conditions = ""

		self.file = '/tmp/weather_output'
		

	def get(self,woeid,unit_format):
		
		q='SELECT%20*%20FROM%20weather.forecast%20WHERE%20woeid="{}"%20and%20u="{}"&format=json'.format(woeid,unit_format)
		weather_req_url = 'http://query.yahooapis.com/v1/public/yql?q={}'.format(q)
		request = urllib2.urlopen(weather_req_url).read()
		self.data = json.loads(request)

		self.title = self.data['query']['results']['channel']['item']['title']
		self.humidity = self.data['query']['results']['channel']['atmosphere']['humidity']
		self.desc = self.data['query']['results']['channel']['description'][7:]
		self.current_temp = self.data['query']['results']['channel']['item']['condition']['temp']
		self.current_conditions = self.data['query']['results']['channel']['item']['condition']['text']
		self.current_forcast_min_temp = self.data['query']['results']['channel']['item']['forecast'][0]['low']
		self.current_forcast_max_temp = self.data['query']['results']['channel']['item']['forecast'][0]['high']

		formatted = "{}c, {}".format(self.current_temp,self.current_conditions)

		return formatted

	def run(self):
		while True:
			self.fo = open(self.file,"wb")
			print "getting weather"
			print  self.get('1226059','c')
			print "sleeping"
			self.fo.write(self.get('1226059','c'))
			self.fo.close()
			time.sleep(60)

if __name__ == '__main__':
	app = weatherData()
	app.run()

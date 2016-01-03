#!/usr/bin/python
# -*- coding: utf-8 -*-
# Credits to python port of nrf24l01, Joao Paulo Barrac & maniacbugs original c library, and this blog: http://blog.riyas.org


import time
import os
import random

import sys
import unicodedata


from datetime import datetime, timedelta
from ConfigParser import SafeConfigParser

import urllib
import urllib2

remote_url = 'http://192.168.0.13:8086'

def read():

	#values = {'db' : 'homelog', "q" :"SELECT * FROM testdata WHERE time > now() - 15m"}
	#values = {'db' : 'homelog', "q" :"SELECt * from testdata WHERE time > '2015-01-04T00:00:00Z' AND time < '2015-01-07T00:00:00Z'"}#, "pretty": "true"}
	values = {'db' : 'homelog', "q" :"SELECT * from testdata WHERE time > now() - 72h"}
	#values = {'db' : 'homelog', "q" :"SELECT * FROM testdata"}
	URL = "%s/query?%s" % (remote_url, urllib.urlencode(values))
	print URL
	response = urllib2.urlopen(URL)
	result = response.read()
	#print result


print "Reading"

start = time.time()
read()
end = time.time()
print(end - start)

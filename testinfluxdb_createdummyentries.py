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

origintimestamp = time.mktime(datetime.strptime("01/01/2010 00:00:00", "%d/%m/%Y %H:%M:%S").timetuple())

print "Origin is " + str(origintimestamp)

timedelta = long(0)
latesttimestamp = long(0)
nowtimestamp =  long( time.time()  * 1e9 )
print "Now is " + str(nowtimestamp)
totalNbEntries = 0

def generateEntries(howmuch, delta):

	global timedelta
	global latesttimestamp
	global origintimestamp
	global totalNbEntries

	data = ""
	for i in range(howmuch):
		timestamp = long( ( origintimestamp + timedelta ) * 1e9 )
		latesttimestamp = timestamp
		data = data + 'testdata,graph=watermeter' + ' value=' + str(random.uniform(0.0, 100.0)) + " " + str(timestamp)+ "\n "
		timedelta = timedelta + delta

	URL = "%s/write?db=homelog" % remote_url
	req = urllib2.Request(URL, data)
	req.add_header('Content-Length', '%d' % len(data))
	req.add_header('Content-Type', 'application/octet-stream')
	response = urllib2.urlopen(req)
	result = response.read()

	totalNbEntries = totalNbEntries + howmuch
	return result

print "Writing"

while latesttimestamp <  nowtimestamp:
	generateEntries(1000, 300L) ## generate batch of 1000 points 5 min apart
	time.sleep(10)
	print "latesttimestamp = " + str(latesttimestamp) + " , continuing..."





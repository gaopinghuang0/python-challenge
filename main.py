#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
import string, StringIO
import re
import requests, urllib
import Image
from bs4 import BeautifulSoup, Comment

headers = { "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; "\
	"rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6" }  # pretend to be browser 


# wrap a func to handle BeautifulSoup content, or
# return content as the default func
def soup(url, func=lambda x, y: x, **kw):
	req = requests.get(url, headers=headers, **kw).text
	content = BeautifulSoup(req)  
	return func(content, url)

def get_comment(url, index):
	comments = soup(url).findAll(text=lambda text:isinstance(text, Comment))
	return comments[index]

def cha0():
	print "change url to 2**38", 2**38

def cha1():
	def shift2(x):
		return chr(ord('a') + (ord(x) - ord('a') + 2) % 26) if x.isalpha() else x

	def trans(x):
		print "".join(map(shift2, x))

	s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."\
		" bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm"\
		" jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	trans(s)
	trans("map")  # ocr
	cha1_another(s)

def cha1_another(original, shift=2):
	az = string.ascii_lowercase
	table = string.maketrans(
		az, az[shift:] + az[:shift] 
	)
	print str(original).translate(table)

def cha2():
	uri = "http://www.pythonchallenge.com/pc/def/ocr.html"
	mess_data = get_comment(uri, 1)
	print re.sub(r'[^a-zA-Z]+', '', mess_data)  # equality
	print "".join(re.findall(r'[a-zA-Z]', mess_data))  # equality

def cha3():
	"""One small letter, surrounded by EXACTLY three big bodyguards
	 on each of its sides."""

	uri = "http://www.pythonchallenge.com/pc/def/equality.html"
	mess_data = get_comment(uri, 0)
	print "".join(re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', mess_data))

def cha4():
	uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
	nothing_rep = "and the next nothing is (\d+)"
	nothing = "8022"  # initial is "12345", be asked to change later, re-run

	while True:
		try:
			content = requests.get(uri, params={'nothing': nothing}).text
			print content
			nothing = re.search(nothing_rep, content).group(1)
		except:
			break

	print nothing

def cha5():
	"""Don't understand..."""
	import pickle
	handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
	data = pickle.load(handle)
	handle.close()

	for elt in data:  # "channel"
		print "".join([e[0] * e[1] for e in elt])

	del pickle

def cha6_wrong():
	"Result is: Collect the comments. But the method cannot get comment info"
	nothing_rep = 'Next nothing is (\d+)'
	nothing = "90052"

	while True:
		try:
			filename = './channel/%s.txt' % nothing
			with open(filename, 'r') as f:
				for line in f:
					print line
					nothing = re.search(nothing_rep, line).group(1)
		except:
			print nothing
			break

def cha6():
	import zipfile, collections
	out, nothing, f = [], "90052", "%s.txt"
	nothing_rep = "Next nothing is (\d+)"

	# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip

	file = zipfile.ZipFile('channel.zip')

	while True:
		try:
			nothing = re.search(nothing_rep, file.read(f % nothing)).group(1)
		except:
			print file.read(f % nothing)
			break

		out.append(file.getinfo(f % nothing).comment)

	print "".join(out)  # Not the big "hockey", but the letters "oxygen"!!

def cha7():
	"Copy the solution."
	img = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()
	i = Image.open(StringIO.StringIO(img))  # Image.open requires a file-like object
	# repeat every 7 pixels, the bar is in the middle of img
	row = [i.getpixel((x, i.size[1] / 2)) for x in range(0, i.size[0], 7)]
	ords = [r for r, g, b, a in row if r == g == b]  # only look at rgb
	# print "".join(map(chr, ords))
	# print "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
	# or merge above two lines into:
	print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))

def main():
	cha7()

if __name__ == '__main__':
	main()
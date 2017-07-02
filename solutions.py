#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
import string, StringIO
import re
import requests, urllib
from PIL import Image  # Pillow
from bs4 import BeautifulSoup, Comment

headers = { "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; "\
	"rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6" }  # pretend to be browser 


# wrap a func to handle BeautifulSoup content, or
# return content as the default func
def soup(url, func=lambda x, y: x, **kw):
	req = requests.get(url, headers=headers, **kw).text
	content = BeautifulSoup(req)  
	return func(content, url)

def get_comment(url, index=0):
	comments = soup(url).findAll(text=lambda text:isinstance(text, Comment))
	return comments[index]




def challenge0():
	print "change url to 2**38", 2**38

def challenge1():
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

def challenge1_another(original, shift=2):
	# Credit: inspired by https://the-python-challenge-solutions.hackingnote.com/level-1.html
	a2z = string.ascii_lowercase
	table = string.maketrans(
		a2z, a2z[shift:] + a2z[:shift] 
	)
	print str(original).translate(table)

def challenge2():
	uri = "http://www.pythonchallenge.com/pc/def/ocr.html"
	mess_data = get_comment(uri, 1)
	print re.sub(r'[^a-zA-Z]+', '', mess_data)  # equality
	# or
	print "".join(re.findall(r'[a-zA-Z]', mess_data))  # equality

def challenge3():
	"""One small letter, surrounded by EXACTLY three big bodyguards
	 on each of its sides."""

	uri = "http://www.pythonchallenge.com/pc/def/equality.html"
	mess_data = get_comment(uri, 0)
	print "".join(re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', mess_data))
	# >>> linkdedlist

def challenge4():
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
	# >>> peak.html

def challenge5():
	import pickle
	# Note: requests.get doesn't work, as it is unpickleable
	handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
	data = pickle.load(handle)
	handle.close()

	print data
	for line in data:
		print "".join([ch * num for ch, num in line])

	del pickle
	# >>> "channel"


def challenge6_wrong():
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

def challenge6():
	import zipfile

	# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip
	file = zipfile.ZipFile('channel.zip')

	# in readme.txt, start from 90052
	out, nothing, f = [], "90052", "%s.txt"
	nothing_ptn = "Next nothing is (\d+)"

	while True:
		try:
			content = file.read(f % nothing)
			# print content
			nothing = re.search(nothing_ptn, content).group(1)
		except:
			print file.read(f % nothing)
			break
		# collect comments for each archieve file
		# https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.comment
		out.append(file.getinfo(f % nothing).comment)

	print "".join(out)  # Not the big "hockey", but the letters "oxygen"!!


def challenge7():
	response = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
	im = Image.open(StringIO.StringIO(response.content))  # Image.open requires a file-like object
	pix = im.load()
	middle = im.size[1]/2

	# repeat every 7 pixels, the bar is in the middle of img
	for x in range(0, im.size[0], 7):
		r = pix[x, middle][0]
		# print chr(r),

	hint = [105, 110, 116, 101, 103, 114, 105, 116, 121]
	print "".join(map(chr, hint))

	###### Below is solution from Internet
	# row = [i.getpixel((x, i.size[1] / 2)) for x in range(0, i.size[0], 7)]
	# ords = [r for r, g, b, a in row if r == g == b]  # only look at rgb
	# print "".join(map(chr, ords))
	# print "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
	# or merge above two lines into:
	# print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))


def challenge8():
	# comments = get_comment('http://www.pythonchallenge.com/pc/def/integrity.html')
	# print comments
	# from solution: https://the-python-challenge-solutions.hackingnote.com/level-8.html
	# Another useful tool: 'file' command on unix. Learned from wiki.pythonchallenge.com
	# first write the data to a file: fn.
	# Note: do not use sublimeText or vim to create new file, which will change the file type
	# use python open(fn, 'w').write(data)
	# then call: file fn
	# from output, we can infer the compression format
	import bz2
	# 'BZ' means bzip, h means Huffman coding, 
	un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
	print bz2.decompress(un), bz2.decompress(pw)

def challenge9():
	from PIL import Image, ImageDraw
	first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
		310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
		190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
		389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
		215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
		290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
		279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
		327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
		328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
		259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
		352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
		120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
		214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
		102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
		113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
		133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
		111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
		332,155,348,156,353,153,366,149,379,147,394,146,399]
	second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
		157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
		125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
		77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
		158,121,157,128,156,134,157,136,156,136]
	im = Image.new('RGB', (500, 500))
	draw = ImageDraw.Draw(im)
	draw.polygon(first, fill="blue")
	draw.polygon(second, fill="blue")
	im.show()  # cow -> bull
	# http://www.pythonchallenge.com/pc/def/bull.html
	# similarly, use d3.js to draw a path


def challenge10():
	"""
	a = [1, 11, 21, 1211, 111221, 
	len(a[30]) = ?
	Hint: look_and_say sequence  (Wiki)
	"""
	from itertools import groupby
	def look_and_say(n):
		a = '1'
		for _ in xrange(n):
			# groupby  -> [(number, all appearances)]
			a = ''.join([str(len(list(j)))+i for i, j in groupby(a)])
		return a

	print len(look_and_say(30))  # 5808
	# http://www.pythonchallenge.com/pc/return/5808.html


def main():
	challenge10()

if __name__ == '__main__':
	main()
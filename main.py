#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
import string
import re

def cha1():
	print "change url to 2**38", 2**38

def cha2():
	def shift2(x):
		return chr(ord('a') + (ord(x) - ord('a') + 2) % 26) if x.isalpha() else x

	def trans(x):
		print "".join(map(shift2, x))

	s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."\
		" bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm"\
		" jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	trans(s)
	trans("map")  # ocr
	cha2_another(s)

def cha2_another(original, shift=2):
	az = string.ascii_lowercase
	table = string.maketrans(
		az, az[shift:] + az[:shift] 
	)
	print str(original).translate(table)

def cha3():
	from mess_data import MESS_DATA
	print re.sub(r'[^a-zA-Z]+', '', MESS_DATA)  # equality
	print "".join(re.findall(r'[a-zA-Z]', MESS_DATA))  # equality


def main():
	cha3()

if __name__ == '__main__':
	main()
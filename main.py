#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate

def c1():
	print "change url to 2**38" 

def c2():
	def shift2(x):
		return chr(97 + (ord(x) - 97 + 2) % 26) if x != ' ' else x

	s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
	print "".join(map(shift2, s))

def main():
	c2()

if __name__ == '__main__':
	main()
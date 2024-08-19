## VAMOS USAR ESSA BIBLIOTECA PARA CRIAR NOSSO AGENTE SSH!
from codecs import strict_errors
from sys import stdin, stdout, stderr

import paramiko
##################

## LEVANDO EM CONSIDERAÇÃO O SISTEMA DO KALI, PARA CRIAÇÃO DO SSH
## OS DAODS PODEM SER ALTERADOS...

host = "127.0.0.1"
user = "kalli"
passwd = "kalli"

##CRIANDO A CONEX
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = client.exec_command(input("Digite o Comando: "))
    for line in stdout.readlines():
        print(line.strip())
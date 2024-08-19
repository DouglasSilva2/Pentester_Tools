import dns.resolver
import sys

resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]
		
except:
	print("Usege: python 3 dnsbrute.py dominio wordlist.txt")
	sys.exit()

try:
	with open (wordlist, "r") as arq:
		subdominios = arq.read().splitlines()##pegar cada linha e separar (splitlines
except:	
	print(" Arquivo ao abrir não encontrado")
	sys.exit()
	

for subdominio in subdominios:
	try:
			sub_alvo = "{},{}".format(subdominio, alvo)
			resultados = resolver.resolve(sub_alvo, "A")
			for resultado in reultados:
					print("{} -> {}".format(sub_alvo, resultado))
					
	except:
		pass
	
##REDME
##  ------------- NÃO PRECISA USAR SIMPLESMENTE A SUA WORDLIST ###
##lembrando que o comando paraexecução seria
##
##python3 dnsbrute.py <dominio> + wordlist.tct
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client .settimeout(1)#dando um segundo para teste de conexão
try:
    client.connect(("google.com", 80))
    client.send("GET / HTTP/1.1\nHost: www.google.com\n\n\n".encode())
    ## Recebendo dados com o metodo recv
    ## imprimindo dados
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print(" Warning !!! ")
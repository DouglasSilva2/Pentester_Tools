import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    ##Criando um loop para que a conexao não se perca!!
    ## realizar a conversão das mensagem de str para bity
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
                ##usar o break para quebrar a conexão.
    client.close()
except Exception as error:
    print(" Erro de conexão com servidor ")
    print(error)
    client.close()
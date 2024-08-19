import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("0.0.0.0", 4433))
    server.listen(5)##numero de conexão que vai aceitar
    print("Listening.... ")## para exibir a mensagem que está escutando


    client_socket, address = server.accept()## retorna uma tupla
    print(" Received from: " + address[0])##pegando o primeiro dado
    while True:
        data = client_socket.recv(1024).decode()##pegando o dado e covertendo em bity
        print(data)
        ###Posso passar um dado para o servidor
        client_socket.send(input("Mensagem: ").encode())

    ##Print para ver a tupla
    #print(server.accept())## posso imprimir para ver
    server.close()##Fechar a conexão....
except Exception as error:
    print("Erro: ", error)
    server.close()
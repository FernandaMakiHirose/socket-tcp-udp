import socket

conexão = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')

host = 'localhost'
porta = 5432

conexão .bind((host, porta))
mensagem = 'Servidor: Olááááá lá lá!!!'

while 1:
    data, endereço = conexão.recvfrom(4096)

if data:
    print('Servidor enviando mensagem...')
    conexão.sendto(data + (mensagem.encode()), endereço)

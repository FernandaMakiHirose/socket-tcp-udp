import socket

conexão = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, serenão?'

try:

    print(f'Cliente: {mensagem}')
    conexão.sendto(mensagem.encode(), (host, 5432))

    data, server = conexão.recvfrom(4096)
    data = data.decode()
    print(f'Cliente: {data}')

finally:

    print(f'Cliente fechando a conexão')
    conexão.close()

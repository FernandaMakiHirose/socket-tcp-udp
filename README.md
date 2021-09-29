# Introdução a Socket, cliente TCP/UDP e Server
## Requisitos
- Visual Studio Code ou Terminal
- Python

## Licença
Distribuido sob a licença MIT License. Veja `LICENSE` para mais informações.

## Executar o projeto
No path `\socket-tcp-udp` (Substitua o `nomedoarquivo` pelo nome do arquivo que você quer executar):
>python nomedoarquivo.py

## Biblioteca Socket
- Esta biblioteca fornece acesso de baixo nível à interface de rede
- O S.O fornece a API socket que relaciona o programa com a rede

## TCP
- O TCP (Transmission Control Protocol) ou Protocolo de Controle de Transmissão é um dos protocolos de comunicação, que dão suporte a rede global Internet, verificando se os dados são enviados na sequência correta e sem erros
- Nosso programa verificará se dados são enviados de maneira íntegra 

## UDP
- O UDP (User Datagram Protocol) ou Protocolo de Datagrama de Usuário é um protocolo simples da camada de transporte que permite que a aplicação envie um datagrama dentro num pacote
- IPv4 ou IPvé a um destino, porém sem qualquer tipo de garantia que o pacote chegue corretamente

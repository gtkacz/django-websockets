import socket
import sys


class Server:
    def __init__(self, host: str = '127.0.0.1', port: int = 32218) -> None:
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind((self.host, self.port))

    def connect(self) -> None:
        self.socket.listen()
        print('Aguardando cliente...')

        conn, addr = self.socket.accept()
        print(f'\rConectado ao endereço: {addr[0]}:{addr[1]}...')

        try:
            while True:
                data = conn.recv(1024)

                if data.decode().upper() == 'QUIT':
                    print('Conexão encerrada pelo cliente.')
                    break

                print(f'Mensagem recebida: {data.decode()}')

                message = input('Digite uma mensagem: ')

                conn.send(message.encode())
                sys.stdout.write(f'\rMENSAGEM ENVIADA: {message}\n')

                if message.upper() == 'QUIT':
                    print('Conexão encerrada pelo servidor.')
                    break

        except Exception as ex:
            print(f'ERRO:\n\n{ex.with_traceback()}')

        finally:
            conn.close()


if __name__ == '__main__':
    server = Server()
    server.connect()

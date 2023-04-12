import socket
import sys


class Client:
    def __init__(self, host: str = '127.0.0.1', port: int = 32218) -> None:
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        print('Aguardando servidor...')
        self.socket.connect((self.host, self.port))
        print(f'\rConectado ao servidor: {self.host}:{self.port}...')

        try:
            while True:
                message = input('Digite uma mensagem: ')

                self.socket.send(message.encode())
                
                sys.stdout.write(f'\rMENSAGEM ENVIADA: {message}\n')

                if message.upper() == 'QUIT':
                    print('Conexão encerrada pelo cliente.')
                    break

                data = self.socket.recv(1024)

                if data.decode().upper() == 'QUIT':
                    print('Conexão encerrada pelo cliente.')
                    break

                print(f'Resposta do servidor: {data.decode()}')

        except Exception as ex:
            print(f'ERRO:\n\n{ex.with_traceback()}')

        finally:
            self.socket.close()


if __name__ == '__main__':
    cli = Client()
    cli.connect()

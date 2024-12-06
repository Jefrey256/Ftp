import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

FTP_HOST = os.getenv("FTP_HOST", "0.0.0.0")
FTP_PORT = int(os.getenv("FTP_PORT", 2121))
FTP_USER = os.getenv("FTP_USER", "user")
FTP_PASSWORD = os.getenv("FTP_PASSWORD", "password")
FTP_DIRECTORY = os.getenv("FTP_DIRECTORY", "ftp_root")

def run_ftp_server():
    # Criar o diretório base, se não existir
    if not os.path.exists(FTP_DIRECTORY):
        os.makedirs(FTP_DIRECTORY)

    # Configurar autorização
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    # Iniciar o servidor FTP
    server = FTPServer((FTP_HOST, FTP_PORT), handler)
    print(f"Servidor FTP rodando em {FTP_HOST}:{FTP_PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()


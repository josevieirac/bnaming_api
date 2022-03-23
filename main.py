"""
Arquivo main principal, onde importa todas as rotas e executa o server.

Toda rota criada deverá ser importada aqui nesse código.
"""

from src.server.server import server
from src.routes.evaluation_route import *

if __name__ == '__main__':
    server.run(debug=True,host="0.0.0.0")


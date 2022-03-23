"""
Código de definição e configuração da estrutura base do server.

Estudar como melhor configurar esse servidor
"""

from logging import debug
from flask import Flask, request, jsonify
from flask_restx import Api

class Server():

    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                        version = '1.0',
                        title = 'bNaming API',
                        description = 'Api de um sistema para auxiliara a avaliar a qualidade de um nome de uma marca.',
                        doc = '/docs'
                        )

    def run(self,debug = False, port = 5000, host=None):
        if host != None:
            self.app.run(debug=debug, port=port, host=host)
        else:
            self.app.run(debug=debug, port=port, host=host)

server = Server()
"""
Código de definição de rotas, para novas rotas utilizar esse código como template
"""

from src.server.server import server
from flask_restx import Resource

api = server.api

@api.route('/evaluation')
class Evaluation(Resource):

    def get(self,):
        return "Avaliar nome"
"""
Código de definição de rotas, para novas rotas utilizar esse código como template
"""

from src.server.server import *
from flask_restx import Resource

api = server.api

@api.route('/evaluation')
class Evaluation(Resource):

    def get(self,):
        print("Entrou no GET")
        return jsonify({"Messagem":"Utilize o método POST e envie o nome e o segmento para que possamos realizar a avaliação do nome."})

    def post(self,):
        dados = request.json

        nome = dados['nome']
        segmento = dados['segmento']

        print("VEIO ISSO:", dados)
        print("O nome é: ", nome)
        print("O segmento é: ", segmento)
        return jsonify(dados)
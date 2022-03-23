# Importando as bibliotecas e arquivos
from flask import Flask, request, jsonify
from flask_restx import Api, Resource

# Instannciando nossa API
app = Flask(__name__)
api = Api(app,
        version = '1.0',
        title = 'bNaming API',
        description = 'Api de um sistema para auxiliara a avaliar a qualidade de um nome de uma marca.',
        doc = '/docs'
        )

# Definindo nossas rotas

# Rotas de avaliação
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

# Executando nossa API
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


import json
import tensorflow as tf

from models.rede_neural_classificacao import *

# Carregando dados bases
with open('dados/variaveis.json', 'r', encoding='utf8') as f:
  dados = json.load(f)

# Montando variaveis
DIM_EMBEDDING = dados['DIM_EMBEDDING']
TAMANHO_INPUT = dados['TAMANHO_INPUT']
TAMANHO_NOMES = dados['TAMANHO_NOMES']
TAMANHO_VOCABULARIO = dados['TAMANHO_VOCABULARIO']

# Montando tokenizer
tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(dados['TOKENIZER'])

# Definindo os modelos de classificação para cada critério
grafia_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
pronuncia_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
sonoridade_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
conceito_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
originalidade_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT) # pode remover
potencial_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
popularidade_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
memorizacao_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
simplicidade_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT)
criatividade_class = RedeNeural_Class(TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT) # pode remover

# Carregando pesos dos modelos
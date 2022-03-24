import json
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

from src.models.rede_neural_classificacao import *

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
grafia_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
grafia_class.load_weights('dados/pesos/grafia_class.hdf5')
pronuncia_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
pronuncia_class.load_weights('dados/pesos/pronuncia_class.hdf5')
sonoridade_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
sonoridade_class.load_weights('dados/pesos/sonoridade_class.hdf5')
conceito_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
conceito_class.load_weights('dados/pesos/conceito_class.hdf5')
originalidade_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
originalidade_class.load_weights('dados/pesos/originalidade_class.hdf5')
potencial_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
potencial_class.load_weights('dados/pesos/potencial_class.hdf5')
popularidade_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
popularidade_class.load_weights('dados/pesos/popularidade_class.hdf5')
memorizacao_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
memorizacao_class.load_weights('dados/pesos/memorizacao_class.hdf5')
simplicidade_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
simplicidade_class.load_weights('dados/pesos/simplicidade_class.hdf5')
criatividade_class(tf.cast([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], tf.float32))
criatividade_class.load_weights('dados/pesos/criatividade_class.hdf5')


# Função para codificar o nome e segmento passado como input para o modelo
def codificar_input(input_name, input_seg, tam_padding = TAMANHO_NOMES+1):

  # Dicionário para traduzir o segmento em código
  index = len(tokenizer.word_index)
  dic = {'alimentos/bebidas' : index+1,
         'automotivo' : index+2,
         'bens de consumo' : index+3,
         'energia/combustível' : index+4,
         'entretenimento' : index+5,
         'financeiro' : index+6,
         'logistica' : index+7,
         'serviços' : index+8,
         'tecnologia' : index+9,
         'varejo' : index+10 }

  # Tokenizando nome de entrada
  name_code = tokenizer.texts_to_sequences([input_name])

  # Adicionando o código do segmento
  name_code[0].append(dic[input_seg])

  # Adicionando o padding no nome
  name_padded = pad_sequences(name_code, maxlen=tam_padding)

  # Convertendo em tensor
  name_output = tf.cast(name_padded, tf.float32)

  return name_output

# Função para avaliar nome e segmento codificado pela função acima
def avaliar_classificacao(input_code):
  # Avaliando critérios
  grafia = grafia_class(input_code)
  pronuncia = pronuncia_class(input_code)
  sonoridade = sonoridade_class(input_code)
  conceito = conceito_class(input_code)
  originalidade = originalidade_class(input_code)
  potencial = potencial_class(input_code)
  popularidade = popularidade_class(input_code)
  memorizacao = memorizacao_class(input_code)
  simplicidade = simplicidade_class(input_code)
  criatividade = criatividade_class(input_code)

  # Obtendo nota do critério
  l = grafia.numpy().tolist()[0]
  grafia = l.index(max(l))+1
  l = pronuncia.numpy().tolist()[0]
  pronuncia = l.index(max(l))+1
  l = sonoridade.numpy().tolist()[0]
  sonoridade = l.index(max(l))+1
  l = conceito.numpy().tolist()[0]
  conceito = l.index(max(l))+1
  l = originalidade.numpy().tolist()[0]
  originalidade = l.index(max(l))+1
  l = potencial.numpy().tolist()[0]
  potencial = l.index(max(l))+1
  l = popularidade.numpy().tolist()[0]
  popularidade = l.index(max(l))+1
  l = memorizacao.numpy().tolist()[0]
  memorizacao = l.index(max(l))+1
  l = simplicidade.numpy().tolist()[0]
  simplicidade = l.index(max(l))+1
  l = criatividade.numpy().tolist()[0]
  criatividade = l.index(max(l))+1

  return {
    "grafia":grafia,
    "pronuncia":pronuncia,
    "sonoridade":sonoridade,
    "conceito":conceito,
    "originalidade":originalidade,
    "potencial":potencial,
    "popularidade":popularidade,
    "memorizacao":memorizacao,
    "simplicidade":simplicidade,
    "criatividade":criatividade
  }

#Função principal para avaliar o nome
def predicao_classificacao(input_name, input_seg):
  input_code = codificar_input(input_name, input_seg)
  return avaliar_classificacao(input_code)
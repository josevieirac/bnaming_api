import tensorflow as tf

# Definindo modelo de classificacao

class RedeNeural_Class(tf.keras.Model):

  def __init__(self, TAMANHO_VOCABULARIO, DIM_EMBEDDING, TAMANHO_INPUT):
    super(RedeNeural_Class, self).__init__()

    # Input: (batch, 16)                       voc + qtd segmentos + 1 (pois o último ponto é aberto)
    self.embedding = tf.keras.layers.Embedding(TAMANHO_VOCABULARIO+10+1, DIM_EMBEDDING, input_length=TAMANHO_INPUT)    # Output: (batch, 16, 11) (batch, 16, DIM_EMBEDDING)

    self.flatten = tf.keras.layers.Flatten()                                                                           # Output: (batch, 176) (batch, 16 * DIM_EMBEDDING)

    self.dense1 = tf.keras.layers.Dense(10, activation=tf.nn.relu)
    self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.sigmoid)

  def call(self, input):
    x = self.embedding(input)
    x = self.flatten(x)
    x = self.dense1(x)
    x = self.dense2(x)
    return x

# Criando sua primeira MLP em Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy

# fix random seed for reproducibility
numpy.random.seed(7)

# Carregando pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.data", delimiter=",")

# definindo  input (X) e output (Y) 
X = dataset[:,0:8]
Y = dataset[:,8]

# criando modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilando Modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando
model.fit(X, Y, epochs=150, batch_size=10)

# Avaliando
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
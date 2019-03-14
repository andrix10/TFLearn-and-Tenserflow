import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.metrics import Accuracy

acc = Accuracy()
network = input_data(shape=[None, 100, 100, 3])

# Conv layers ------------------------------------
network = conv_2d(network, 80, 11, strides=1, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = conv_2d(network, 90, 5, strides=1, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = conv_2d(network, 100, 3, strides=1, activation='relu')
#network = max_pool_2d(network, 3, strides=2)
network = conv_2d(network, 100, 3, strides=1, activation='relu')
network = conv_2d(network, 90, 3, strides=1, activation='relu')
network = max_pool_2d(network, 3, strides=2)
# Fully Connected Layers --------------------------
network = fully_connected(network, 1024, activation='tanh')
network = dropout(network, 0.5)
# network = fully_connected(network, 1024, activation='tanh')
# network = dropout(network, 0.6)
# network = fully_connected(network, 1024, activation='tanh')
# network = dropout(network, 0.5)
network = fully_connected(network, 2, activation='softmax')
#network = dropout(network, 0.5)

# Final network
network = regression(network, optimizer='momentum',
                     loss='categorical_crossentropy',
                     learning_rate=0.001, metric=acc)
model = tflearn.DNN(network, tensorboard_verbose=3, tensorboard_dir="logs")
#model = tflearn.DNN(network)
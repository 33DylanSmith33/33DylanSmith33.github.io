from Layer import Dense
from Optimizer import SGD
from Activation import ReLU, SoftMax
import numpy as np

class Network:

    # will need to add methods to batch input data and get onehot encodings of labels for each batch


    def __init__(self):
        # to store layers (including activation functions)
        self.layers = []
        self.optimizer = None # will be set my a method

    def add(self, layer):
        """
            Add a layer to the network
            Layer could be a Dense layer or an activation function
            !!!!!! Don't add input layer !!!!!!
            :param layer: The layer to add to the network
        """
        self.layers.append(layer)

    def compile(self, optimizer):
        # TODO have to get (parameters, gradients) tuples from each layer and pass them to the optimizer
        """
            Compile the network by setting the optimizer
            :param optimizer: The optimizer to use
        Also where loss function would be stored
        """
        self.optimizer = optimizer

    def forward(self, input_data):
        """
            Compute the output of the network given the input data
            :param input_data: The input data
            :return: The output of the network
        """
        # iterate through each layer and compute the output of the current layer given the output of the previous layer
        output = input_data
        for layer in self.layers:
            output = layer.forward(output)
        # returns final output of the network
        return output

    def backward(self, loss_gradient):
        # for current implementation, loss_gradient will be one-hot encoded labels
        """
            Back propagate the loss through the network
            :param loss_gradient: The gradient of the loss with respect to the output of the network
            :return: The gradient of the loss with respect to the input of the network
        """
        # iterate through each layer in reverse order and back propagate the gradient through the layer
        grad_output = loss_gradient
        for layer in reversed(self.layers):
            grad_output = layer.backward(grad_output)
        # return the gradient of the loss with respect to the input of the network
        return grad_output

    def train_on_batch(self, x_batch, y_batch):
        pass

    def fit(self, x_train, y_train, epochs, batch_size):
        pass

    def predict(self, input_data):
        # self.forward(input_data) and then return the class
        pass
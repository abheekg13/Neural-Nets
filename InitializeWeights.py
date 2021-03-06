from random import *

def initialize_weights(number_of_input_neurons, number_of_hidden_neurons, number_of_output_neurons):

	input_to_hidden_layer_wts = []						#theta
	for i in range (0,number_of_input_neurons):
		temp = []
		for j in range(0, number_of_hidden_neurons):
			temp.append(round(random(),3))
		input_to_hidden_layer_wts.append(temp)
	input_to_hidden_layer_wts.append([1])		#bias term

	hidden_to_output_layer_wts = []
	for i in range(0,number_of_hidden_neurons):
		temp = []
		for j in range(0,number_of_output_neurons):
			temp.append(round(random(),3))
		hidden_to_output_layer_wts.append(temp)
	hidden_to_output_layer_wts.append([1])		#bias term

	return input_to_hidden_layer_wts, hidden_to_output_layer_wts
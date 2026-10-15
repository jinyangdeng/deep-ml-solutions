import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	# 学会了 numpy.pad，今后不用手搓
	# 学会了如何计算 output_height 与 output_width
	# i.e. (original_dim + 2 * padding - kernel_dim) // stride + 1 
	# 学会了如何在矩阵里直接选择区域, [i:..., j:...]
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	padded_input_matrix = np.pad(input_matrix, padding)
	
	output_height = (input_height + 2 * padding - kernel_height) // stride + 1
	output_width = (input_width + 2 * padding - kernel_width) // stride + 1

	output_matrix = np.zeros((output_width, output_height))
	
	for i in range(output_height):
		for j in range(output_width):
			row_start = i * stride
			col_start = j * stride
			output_matrix[i, j] = np.sum(np.multiply(padded_input_matrix[row_start:row_start+kernel_width, col_start:col_start+kernel_height], kernel))
    
	return output_matrix

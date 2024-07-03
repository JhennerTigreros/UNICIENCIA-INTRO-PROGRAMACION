import tensorflow as tf

# Definir matrices
matriz_a = tf.constant([[1, 2], [3, 4]])
matriz_b = tf.constant([[5, 6], [7, 8]])

# Multiplicación de matrices
resultado = tf.matmul(matriz_a, matriz_b)

print("Resultado de la multiplicación de matrices:\n", resultado)
import numpy as numpy # importing numpy libreary

# Creating a vector of 20 random numbers with numbers from 1 to 20
rand_vect = numpy.random.uniform(low=1, high=20, size=20)
print(rand_vect)
print("\n")
# Reshape the array to a 4 by 5
vec_reshape = rand_vect.reshape(4,5)
print(vec_reshape)
print("\n")
# Replace the max in each row by 0
vec_reshape[numpy.arange(len(vec_reshape)), vec_reshape.argmax(axis=1)] = 0
print(vec_reshape)

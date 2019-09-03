import numpy as np
import tensorflow as tf

data = np.genfromtxt('day_head_circumference.csv', delimiter=',')
x_train = np.transpose(np.mat(data[:, 0]))
y_train = np.transpose(np.mat(data[:, 1]))


class NonlinearRegressionModel:
    def __init__(self):
        # Model input
        self.x = tf.placeholder(tf.float32)
        self.y = tf.placeholder(tf.float32)

        # Model variables
        self.W = tf.Variable([[0.0]])
        self.b = tf.Variable([[0.0]])

        # Predictor
        f = 20 * tf.sigmoid(tf.matmul(self.x, self.W) + self.b) + 31

        # Mean Squared Error
        self.loss = tf.reduce_mean(tf.square(f - self.y))


model = NonlinearRegressionModel()

# Training: adjust the model so that its loss is minimized
minimize_operation = tf.train.GradientDescentOptimizer(0.0000001).minimize(model.loss)

# Create session object for running TensorFlow operations
session = tf.Session()

# Initialize tf.Variable objects
session.run(tf.global_variables_initializer())

for epoch in range(10000):
    session.run(minimize_operation, {model.x: x_train, model.y: y_train})

# Evaluate training accuracy
W, b, loss = session.run([model.W, model.b, model.loss], {model.x: x_train, model.y: y_train})
print("W = %s, b = %s, loss = %s" % (W, b, loss))

session.close()

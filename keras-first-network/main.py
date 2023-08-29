# We choose age, delivery number, delivery time, blood pressure and heart status.
# We classify delivery time to Premature, Timely and Latecomer. As like the delivery time we consider blood pressure in three statuses of Low, Normal and High moods. Heart Problem is classified as apt and inept.
#
# @attribute 'Age' { 22,26,28,27,32,36,33,23,20,29,25,37,24,18,30,40,31,19,21,35,17,38 }
# @attribute 'Delivery number' { 1,2,3,4 }
# @attribute 'Delivery time' { 0,1,2 } -> {0 = timely , 1 = premature , 2 = latecomer}
# @attribute 'Blood of Pressure' { 2,1,0 } -> {0 = low , 1 = normal , 2 = high }
# @attribute 'Heart Problem' { 1,0 } -> {0 = apt, 1 = inept }
#
# @attribute Caesarian { 0,1 } -> {0 = No, 1 = Yes }





# @attribute 'Age' { 22,26,28,27,32,36,33,23,20,29,25,37,24,18,30,40,31,19,21,35,17,38 }
# @attribute 'Delivery number' { 1,2,3,4 }
# @attribute 'Delivery time' { 0,1,2 }
# @attribute 'Blood of Pressure' { 2,1,0 }
#
# @attribute 'Heart Problem' { 1,0 }
# @attribute Caesarian { 0,1 }


import tensorflow
import numpy as np
import keras as K

# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # suppress CPU msg
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel('INFO')
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed


class MyLogger(K.callbacks.Callback):
    def __init__(self, n):
        self.n = n  # print loss & acc every n epochs

    def on_epoch_end(self, epoch, logs={}):
        if epoch % self.n == 0:
            curr_loss = logs.get('loss')
            curr_acc = logs.get('accuracy') * 100
            print("epoch = %4d  loss = %0.6f  acc = %0.2f%%" % \
                  (epoch, curr_loss, curr_acc))


# Normalizarea valorilor din data base / Scalarea datelor
def scalare(data):
    n = len(data[0])
    for col in range(n):
        max_value = np.max(data[:, col])
        min_value = np.min(data[:, col])
        data[:, col] = (data[:, col] - min_value) / (max_value - min_value)
    return data


def main():
    print("\nCaesarian Section Classification Dataset Data Set \n")
    np.random.seed(1)

    # 1. load data
    # print("Loading data into memory ")
    train_file = "C:\\Users\\momoi\\Desktop\\FACULTATE\ANU III\\INTELIGENTA ARTIFICIALA\\Laboratoare\\tema4\\modeling_train.txt"
    test_file = "C:\\Users\\momoi\\Desktop\\FACULTATE\ANU III\\INTELIGENTA ARTIFICIALA\\Laboratoare\\tema4\\modeling_test.txt"

    train_x = np.loadtxt(train_file, delimiter=',',
                         usecols=[0, 1, 2, 3], dtype=np.float32)

    train_x = scalare(train_x)

    train_y = np.loadtxt(train_file, delimiter=',',
                         usecols=[4], dtype=np.float32)

    test_x = np.loadtxt(test_file, delimiter=',',
                        usecols=[0, 1, 2, 3], dtype=np.float32)
    test_x = scalare(test_x)

    test_y = np.loadtxt(test_file, delimiter=',',
                        usecols=[4], dtype=np.float32)

    # 2. define 4-(x-x)-1 deep NN model
    print("Creating 4-(8-8)-1 binary NN classifier \n")  # hidden layers
    my_init = K.initializers.glorot_uniform(seed=1)
    model = K.models.Sequential()
    model.add(K.layers.Dense(units=8, input_dim=4,
                             activation='tanh', kernel_initializer=my_init))
    model.add(K.layers.Dense(units=8, activation='tanh',
                             kernel_initializer=my_init))
    model.add(K.layers.Dense(units=1, activation='sigmoid',
                             kernel_initializer=my_init))

    # 3. compile model
    simple_sgd = K.optimizers.SGD(lr=0.01)
    model.compile(loss='binary_crossentropy',
                  optimizer=simple_sgd, metrics=['accuracy'])

    # 4. train model
    max_epochs = 500
    my_logger = MyLogger(n=50)
    h = model.fit(train_x, train_y, batch_size=32,
                  epochs=max_epochs, verbose=0, callbacks=[my_logger])

    # 5. evaluate model
    np.set_printoptions(precision=4, suppress=True)
    eval_results = model.evaluate(test_x, test_y, verbose=0)
    print("\nLoss, accuracy on test data: ")
    print("%0.4f %0.2f%%" % (eval_results[0],\
                             eval_results[1] * 100))

   # 6. save model
    mp = ".\\Models\\caesarian_model.h5"
    model.save(mp)

    # 7. make a prediction
    inpts = np.array([[0.5, 0.5, 0.5, 0.5]], dtype=np.float32)
    pred = model.predict(inpts)
    print("\nPredicting authenticity for: ")
    print(inpts)
    print("Probability that class = 1 (fake):")
    print(pred)


if __name__ == "__main__":
    main()

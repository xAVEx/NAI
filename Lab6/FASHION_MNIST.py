'''Zadanie nr 2 - Filip Wrzesień oraz Patryk Szczepański

Rozpoznawanie ubran poprzez siec neuronowa ze zbioru Fashion-Mnist'''

'''__________________________________________________________________________________________________'''

import tensorflow as tf
import matplotlib.pyplot as plt

'''__________________________________________________________________________________________________'''

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

'''__________________________________________________________________________________________________'''

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

'''__________________________________________________________________________________________________'''

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

'''__________________________________________________________________________________________________'''

train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

'''__________________________________________________________________________________________________'''

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

'''__________________________________________________________________________________________________'''

model.compile(optimizer='adam', loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

'''__________________________________________________________________________________________________'''

model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(train_images, train_labels, verbose=2)

'''__________________________________________________________________________________________________'''

print("Test accuracy: ", test_acc)
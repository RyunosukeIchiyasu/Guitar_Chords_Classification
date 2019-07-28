import glob
from PIL import Image
import numpy as np
from keras import optimizers
from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, Dropout, Input
from keras.layers.convolutional import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

class GtCNN:
    mainDir = "/content/drive/My Drive/DNN/Guitar/"
    batchsize = 32
    iteration = 50
    optimizer = optimizers.SGD(lr=0.005)
    loss = "categorical_crossentropy"

    def __init__(self):
        print("Function...initialize")
        self.data = []
        self.label = []
        self.model = Sequential()
        self.x_train = 0
        self.x_test = 0
        self.y_train = 0
        self.y_test = 0

    def readFile(self):
        print("Function...readFile")
        chords = ["32_C_Augument","32_Dm_Augument","32_Em_Augument","32_F_Augument","32_G_Augument","32_Am_Augument","32_Bm_Augument"]
        for index, chord in enumerate(chords):
            chordDir = self.mainDir + chord
            allPaths = glob.glob(chordDir + "/*.jpg")
            for path in allPaths:
                print(path)
                image = Image.open(path)
                image = image.resize((150, 150))
                image = np.array(image)
                image = image.astype("float32")
                image = image / 255
                self.data.append(image)
                self.label.append(index)

        self.data = np.array(self.data)
        self.label = np.array(self.label)
        self.label = np_utils.to_categorical(self.label, 7)

    def makeModel(self):
        print("Function...makeModel")

        self.model.add(Conv2D(32,(3,3),activation="relu",input_shape=(150,150,3)))
        self.model.add(Conv2D(32,(3,3),activation="relu"))
        self.model.add(Conv2D(32,(3,3),activation="relu"))
        self.model.add(MaxPooling2D((2,2)))
        self.model.add(Dropout(0.25))
        self.model.add(Conv2D(64,(3,3),activation="relu"))
        self.model.add(Conv2D(64,(3,3),activation="relu"))
        self.model.add(Conv2D(64,(3,3),activation="relu"))
        self.model.add(MaxPooling2D((2,2)))
        self.model.add(Dropout(0.25))
        self.model.add(Conv2D(128,(3,3),activation="relu"))
        self.model.add(Conv2D(128,(3,3),activation="relu"))
        self.model.add(Conv2D(128,(3,3),activation="relu"))
        self.model.add(MaxPooling2D((2,2)))
        self.model.add(Dropout(0.25))
        self.model.add(Conv2D(256,(3,3),activation="relu"))
        self.model.add(Conv2D(256,(3,3),activation="relu"))
        self.model.add(Conv2D(256,(3,3),activation="relu"))
        self.model.add(MaxPooling2D((2,2)))
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(512, activation="relu"))
        self.model.add(Dense(7, activation="softmax"))

        self.model.summary()

    def trainCNN(self):
        print("Function...trainCNN")

        self.model.compile(optimizer=self.optimizer, loss=self.loss, metrics=["accuracy"])

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data, self.label, test_size=0.20)
        history = self.model.fit(x=self.x_train, y=self.y_train, batch_size=self.batchsize, epochs=self.iteration, validation_data=(self.x_test, self.y_test))

        return history

gtcnn = GtCNN()
gtcnn.readFile()
gtcnn.makeModel()
result = gtcnn.trainCNN()

#Visualization
from keras import backend as K
import cv2

from PIL import Image
import numpy as np
from matplotlib import pylab as plt

image = Image.open("/content/drive/My Drive/DNN/Guitar/31_C/C 050.jpg")
image = image.resize((150, 150))
image = np.array(image)
image = image.astype("float32")
image = image / 255
image = np.expand_dims(image, axis=0)

preds = gtcnn.model.predict(image)
chords = ["C","D","E","F","G","A","B"]
for index, pred in enumerate(preds[0]):
    print(chords[index]+": "+str(round(pred, 3)))
pred_argmax = np.argmax(preds[0])
chord_output = gtcnn.model.output[:, pred_argmax]

last_conv_layer = gtcnn.model.get_layer('conv2d_12').output
grads = K.gradients(chord_output, last_conv_layer)[0]

iterate = K.function([gtcnn.model.input],[last_conv_layer, grads])
output, grads_val = iterate([image])
output, grads_val = output[0], grads_val[0]
weights = np.mean(grads_val, axis=(0,1))
cam = np.dot(output, weights)
cam = cv2.resize(cam, (150,150), cv2.INTER_LINEAR)
cam = np.maximum(cam, 0)
cam = cam / cam.max()

plt.imshow(cam)

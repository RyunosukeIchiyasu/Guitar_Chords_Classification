import matplotlib.pyplot as plt
%matplotlib inline

plt.figure()
plt.plot(range(1, gtcnn.iteration+1), result.history['acc'], label="training")
plt.plot(range(1, gtcnn.iteration+1), result.history['val_acc'], label="validation")
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.figure()
plt.plot(range(1, gtcnn.iteration+1), result.history['loss'], label="training")
plt.plot(range(1, gtcnn.iteration+1), result.history['val_loss'], label="validation")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

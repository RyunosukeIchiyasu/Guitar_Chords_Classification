# Guitar_Chords_Classification

## Overview
I came up with this idea when my friend had practiced playing guitar while he was looking at the music score on the internet. He needed it that has been already existed to play the song. But usually there is music score for brand new songs that he wanted to play because these songs were just released. The dictation that means copy the song by using our ears are difficult for an amateur. 

However, if we knew how to play the song by preparing only movie like MV, live movie, it would be efficient and convenient for us. In this work, I focused on the simple guitar chords. I built CNN model to classify which chord the guitarist is playing now.  

## Dataset Shooting
I let my friend play seven chords(C, Dm, Em, F, G, Am, Bm), and I shot the video of them. The format of the movie is 30 FPS, and the chords were taken on every position like center, corner in the movie evenly because the model had to be improved its robustness about finger location on the pictures.

<img src="https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/shooting.PNG" width="600">
 
## Dataset Expansion
These data can be used to train the model, but it’s possible to memorize all the information instead of grab the feature of fingering several chords. To make the model stronger about difference of guitar neck angle and lefty guitar, the dataset should include various data.
Each data was expanded to ten times more by changing the angle and flip it.

<img src="https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/data_augument.PNG" width="600">

## Model
The MaxPooling layer have to be set appropriate number to make feature map smaller before it reaches the Dense layer. Dropout layers were put to avoid overfit the model, and the Convolution layers were changed for comparison depends on the accuracy.

![pic](https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/model.PNG)


## Train Result
Not only training accuracy, but validation accuracy followed along  improving of training accuracy. However, these test dataset was split 20% from all dataset, and all dataset was made of common data by expanding it. Thus it showed that this result was easy to occur different with classification of dog and cat that use individual dataset.

![pic](https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/ver3_model_3_acc.jpg)
![pic](https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/ver3_model_3_loss.jpg)

## Visualization
I made visualization of each layer to confirm that the model classified the chords by recognizing fingers position like human beings do.
This below layer is the 9th convolution layer that became certain abstract feature map but not so much, so we can see which part of the picture affected to be judged the classification. An interesting fact is that the model didn’t see the thumb to classify Am and Em chords.

|F|Em|Am|
|---|---|---|
|<img src="https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/visualization1.PNG" width="400">|<img src="https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/visualization2.PNG" width="400">|<img src="https://github.com/RyunosukeIchiyasu/Guitar_Chords_Classification/blob/master/pics/visualization3.PNG" width="400">

However, the model also reacted to its background as much as fingers. Considerable reason is that the variety of dataset was monotony. When we think of the way to use this system into our real life, the test data is supposed to be MV and live movie, so the model has to deal with any noise except for fingering position. If I had made these dataset with different background, it could”ve reacted only fingers.

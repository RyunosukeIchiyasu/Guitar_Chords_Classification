import glob
from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import re

def readFile(directory):
    #------------------------------------------------------
    # directory : root directory of chords
    #------------------------------------------------------
    print("readFile...")
    chords = ["31_C","31_Dm","31_Em","31_F","31_G","31_Am","31_Bm"]
    images_read = []
    chords_read = []
    for index, chord in enumerate(chords):
        chordDir = directory + chord
        allPaths = glob.glob(chordDir + "/*.jpg")
        counter = 0
        for index, path in enumerate(allPaths):
            image = Image.open(path)
            image = image.resize((150, 150))
            image_numpy = np.array(image)

            images_read.append(image_numpy)
            chords_read.append(chord + str(index))
            print(chord + str(index))
    return images_read, chords_read

def crop(image_numpy, chord):
    #------------------------------------------------------
    # image_numpy : image data of numpy
    # chord : chord name
    #------------------------------------------------------
    images_crop = []
    chords_crop = []
    counter = 0
    for i in range(3):
        for j in range(3):
            images_crop.append(image_numpy[(x//5*i):(x//5*(i+3)),(y//5*j):(y//5*(j+3)),:])
            chords_crop.append(chord + "_crop" + str(counter))
            counter = counter + 1
    return images_crop, chords_crop

def angle(image_numpy, chord):
    #------------------------------------------------------
    # image_numpy : image data of numpy
    # chord : chord name
    #------------------------------------------------------
    images_angle = []
    chords_angle = []
    for i in range(5):
        temp = Image.fromarray(image_numpy)
        temp = temp.rotate(15*i - 30) #-30, -15, 0, 15, 30 degree
        temp = np.array(temp)
        images_angle.append(temp)
        chords_angle.append(chord + "_angle" + str(i))
    return images_angle, chords_angle

def flip(image_numpy, chord):
    #------------------------------------------------------
    # image_numpy : image data of numpy
    # chord : chord name
    #------------------------------------------------------
    images_flip = []
    chords_flip = []
    for i in range(2):
        if i == 0:
            temp_image = image_numpy
            temp_chord = chord + "_flip" + str(i)
        elif i == 1:
            temp_image = np.fliplr(image_numpy)
            temp_chord = chord + "_flip" + str(i)

        images_flip.append(temp_image)
        chords_flip.append(temp_chord)
    return images_flip, chords_flip

def saveFile(directory, images, chords):
    #------------------------------------------------------
    # directory : folder path that save images to
    # images : image data of numpy list
    # chords : filename
    #------------------------------------------------------
    print("Save...")
    for index, chord in enumerate(chords):
        if re.match(r"^31_C", chord):
            subfolder = "32_C_Augument/"
        elif re.match(r"^31_D", chord):
            subfolder = "32_Dm_Augument/"
        elif re.match(r"^31_E", chord):
            subfolder = "32_Em_Augument/"
        elif re.match(r"^31_F", chord):
            subfolder = "32_F_Augument/"
        elif re.match(r"^31_G", chord):
            subfolder = "32_G_Augument/"
        elif re.match(r"^31_A", chord):
            subfolder = "32_Am_Augument/"
        elif re.match(r"^31_B", chord):
            subfolder = "32_Bm_Augument/"

        saveDir = directory + subfolder + chord + ".jpg"
        Image.fromarray(images[index]).save(saveDir)

#------------------------------------------------------
# Initialize
#------------------------------------------------------
dir = "/content/drive/My Drive/DNN/Guitar/"
x = 500
y = 500

#------------------------------------------------------
# Main
#------------------------------------------------------

#read
images_read, chords_read = readFile(dir)
'''
#crop
images_crop = []
chords_crop = []
for index, image in enumerate(images_read):
    temps_crop, temps_chord = crop(image, chords_read[index])
    images_crop = images_crop + temps_crop
    chords_crop = chords_crop + temps_chord
'''
images_crop = images_read
chords_crop = chords_read

#angle
print("angle...")
images_angle = []
chords_angle = []
for index, image in enumerate(images_crop):
    temps_angle, temps_chord = angle(image, chords_crop[index])
    images_angle = images_angle + temps_angle
    chords_angle = chords_angle + temps_chord

#flip
print("flip...")
images_flip = []
chords_flip = []
for index, image in enumerate(images_angle):
    temps_flip, temps_chord = flip(image, chords_angle[index])
    images_flip = images_flip + temps_flip
    chords_flip = chords_flip + temps_chord

#save
saveFile(dir, images_flip, chords_flip)

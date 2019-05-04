import os
from keras.models import Sequential, save_model
from keras.layers import Dense, Dropout
import numpy as np
import librosa as lb
from keras.utils.np_utils import to_categorical
from keras.constraints import maxnorm
from keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.utils import shuffle
from keras.optimizers import Adam
print("Modules imported")

# In[2]:


file_name = 'C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\testset_new'
numbers = 'zero one two three four five six seven eight nine double triple'.split()
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# In[3]:


def Append(list1, list2, mfccs, num):
	list1.append(mfccs)
	list2.append(num)
	return list1, list2


# In[5]:


X = []                 #This would store the mfccs values of all data
y = []                 #This would store the number which corressponding mfccs values imply
#Taking in the values of all the audio files
print("Taking in values")
for num in numbers:
    audio_data_num = os.listdir(file_name + '\\' + num)
    for audio in audio_data_num:
        aud, sr = lb.core.load(file_name + '\\' + num + '\\' + audio)
        #aud = signal.medfilt(aud, 23)
        mfccs = np.mean(lb.feature.mfcc(y=aud, sr=sr, n_mfcc=50), axis = 1)
        X.append(mfccs)
        y.append(num)
    print(num, "done")
dicti = {}

# In[6]:

X, y = shuffle(X, y, random_state = 5)         #12, 13 gave maximum

X = np.array(X)
y = np.array(y)

#Giving labels to all the outputs
y_label = []
for i in y:
    y_label.append(num_list[numbers.index(i)])
y_label = to_categorical(y_label)
train_X, test_X = np.split(X, [int(0.7 * len(X))])
train_y, test_y = np.split(y_label, [int(0.7 * len(y))])
    
    
    # In[7]:
    
    
#Developing the Neural network model. Pre-processing is over
model = Sequential()
model.add(Dense(100, input_shape = train_X[0].shape, kernel_initializer = 'normal', kernel_constraint = maxnorm(3), activation = 'relu'))
model.add(Dropout(0.05))
model.add(Dense(50, activation = 'relu', kernel_initializer = 'normal', kernel_constraint = maxnorm(3)))
model.add(Dropout(0.05))
model.add(Dense(25, kernel_initializer = 'normal', kernel_constraint = maxnorm(3), activation = 'relu'))
model.add(Dropout(0.05))
model.add(Dense(12, activation = 'softmax'))
    
    
# In[8]:
    
    
adam = Adam(lr = 0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 10**(-8), decay = 0.000001, amsgrad = False)
    
    
# In[9]:
    
    
#Compiling the above model and subsequently fitting it
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])
    
    
#Enabling for early stopping of model if necessary
outputFolder = ".\\weightsStore"
if not os.path.exists(outputFolder):
 	os.makedirs(outputFolder)
    
filepath = outputFolder + "\\weights-{epoch}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor = 'val_acc', save_weights_only = True, period = 10) 
earlystopping = EarlyStopping(monitor = 'acc', patience = 50, min_delta = 0.01, mode = 'auto') 
callbacks_list = [checkpoint, earlystopping]
model.fit(train_X, train_y, epochs = 2000, batch_size = 10, callbacks = callbacks_list, validation_split = 0.1)
    
#Evaluating our model
scores = model.evaluate(test_X, test_y, batch_size = 10)
print("Testing accuracy: {}".format(scores[1]))


#%%

if scores[1] >= 0.8:
    model_save_path = "C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\saved_models\\{0}_acc.hdf5".format(scores[1])
    save_model(model, model_save_path)
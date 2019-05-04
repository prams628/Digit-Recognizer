import os
import numpy as np
import librosa as lb
from keras.models import load_model
import tkinter as tk

#%%
def predict():
    filepath_prediction = 'C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\SplitOnSilenceFiles'
    model_load_path = "C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\saved_models"
    
    prediction_X = []
    prediction_X_num = []
    for file in os.listdir(filepath_prediction):
        aud, sr = lb.core.load(filepath_prediction + "\\" + file)
        #aud = signal.medfilt(aud, 23)
        mfccs = np.mean(lb.feature.mfcc(y=aud, sr=sr, n_mfcc=50), axis = 1)
        prediction_X.append(mfccs)
        prediction_X_num.append(aud)
    prediction_X_num = np.array(prediction_X_num)
    model = load_model(model_load_path + "\\" + os.listdir(model_load_path)[-2])
    #Prediction of numbers according to a saved model
    predictions = model.predict_classes(np.array(prediction_X))
    predictions = list(predictions)

    global final_string_num
    final_string_num = ""
    while predictions[-1] == 10 or predictions[-1] == 11:
        predictions.pop()
    
    l = len(predictions)
    i = 0
    while i < l:
        if predictions[i] == 10:
            i += 1
            final_string_num += ((str(predictions[i]) + "-") * 2)
            
        elif predictions[i] == 11:
            i += 1
            final_string_num += ((str(predictions[i]) + "-") * 3)
        
        else:
            final_string_num += ((str(predictions[i]) + "-"))
        i += 1
    #print(final_string_num)
    #tkWindow()
    return predictions, prediction_X_num

def tkWindow():
    root = tk.Tk()
    root.geometry("200x100")
    root.title("Model Predictions")
    root.configure(bg = "black")
    tk.Label(root, text = final_string_num[:-1]).place(relx = 0.25, rely = 0.5, anchor = tk.CENTER)
    tk.Button(root, text = "OK", command = root.destroy).place(relx = 0.75, rely = 0.5, anchor = tk.CENTER)
    root.mainloop()
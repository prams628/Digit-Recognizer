import pyaudio
import wave
#from tkinter import Label
import tkinter as tk
import threading

class infinite_record():
    def __init__(self, master):
        self.isrecording = False
        self.button = tk.Button(main, text='Click and hold here to record', bg = "white")
        self.button.bind("<Button-1>", self.start)
        self.button.bind("<ButtonRelease-1>", self.stop)
        self.button.place(anchor = tk.CENTER, relx = 0.5, rely = 0.5)
        global WAVE_OUTPUT_FILENAME, FORMAT, CHANNELS, RATE, stream, audio, frames, CHUNK
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 22050
        CHUNK = 1024
        BASIC_PATH = "C:\\Users\\Lakshminagaraj\\Documents\\Pramod\\ML project\\Implement_set"
        
        WAVE_OUTPUT_FILENAME = BASIC_PATH + "\\test.wav"
        audio = pyaudio.PyAudio() 
        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
        					rate=RATE, input=True,
        					frames_per_buffer=CHUNK)
        frames = []
    
    def start(self, event):
        self.isrecording = True
        t = threading.Thread(target = self._record)
        t.start()
    
    def stop(self, event):
        # stop Recording
        self.isrecording = False
        stream.stop_stream()
        stream.close()
        audio.terminate()
         
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        main.destroy()
        
    def _record(self):
        while self.isrecording:
            data = stream.read(CHUNK)
            frames.append(data)
        
main = tk.Tk()
record = infinite_record(main)
main.title("Audio Recording")
main.configure(bg = "black")
main.geometry("500x200")
main.mainloop()

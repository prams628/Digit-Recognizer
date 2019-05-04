import pyaudio
import wave
#from tkinter import Label

def infinite_rec():
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
    print("recording...")
    frames = []
    while 1:
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except KeyboardInterrupt:
            print("finished recording")
            break

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
     
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
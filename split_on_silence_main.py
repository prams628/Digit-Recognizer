from pydub import AudioSegment
from pydub.silence import split_on_silence

def sos():
    print("Starting")
    sound = AudioSegment.from_wav("Implement_set\\test.wav")
    print(sound.dBFS)
    chunks = split_on_silence(sound, 

            min_silence_len=200,
        
            # consider it silent if quieter than a value closest to the average value of the sound track
            silence_thresh= sound.dBFS,
        	
            # keep silence extends audio file by 50 ms
            keep_silence = 200)
        
    #print(chunks)
    for i, chunk in enumerate(chunks):
            chunk.export("SplitOnSilenceFiles\\chunk{}.wav".format(i), format="wav")
    
    print(len(chunks), "files exported")
    return len(chunks)
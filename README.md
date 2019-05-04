# Digit-Recognizer
A program to recognize the digits spoken in audio files

### Input:<br>
  The input file will consist of numbers spoken from 0 - 9 just as we tell phone numbers (99 can be told as "double nine").
  Between every word a gap of about one-tenth of a second is expected.
 
### Dataset:<br>
  The dataset has been stored as a collection of .wav files for every word which can be spoken. The recordings were made in a specific
  format as illustrated in the code to facilitate the comparison between two audio files. A program was written to achieve the same.

### Libraries used:<br>
  <t>Keras<br>
  <t>Librosa<br>
  <t>PyAudio<br>
  <t>PyDub<br>

### Output:<br>
  The output shall consist of the set of numbers being spoken
  
### Result:<br>
  A prediction accuracy of around 75% for men and around 60% for women has been obtained (The dataset is biased towards men's voice due to
  insufficient resources for women's voice)

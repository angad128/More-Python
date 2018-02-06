#Step 1 - import libary
import cmu_sphinx4

#Step 2 - read audio file
audio_URL = 'http://www-mobile.ecs.soton.ac.uk/hth97r/links/Database/man1_nb.wav'
trancriber = cmu_sphinx4.Trancriber(audio_URL)

#Step 3 - Print it out
for line in trancriber.transcript_stream():
	print(line)
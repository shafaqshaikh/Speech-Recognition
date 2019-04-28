import speech_recognition as sr
r=sr.Recognizer()
r.energy_threshold=1000

with sr.Microphone() as source:
	print('Speak Anything: ')
	audio =r.listen(source)

	try:
		text = r.recognize_google(audio)
		print('you said : {}'.format(text))
	except:
		print('sorry could not recognize your voice')


		
		
		
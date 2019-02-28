import speech_recognition as sr  #speech recogntion as written as sr#

r = sr.Recognizer()  #work as recognizer of audio#
with sr.Microphone() as source:      #intializing microphone as sr.microphone#
    print("Speak Anything :")
    audio = r.listen(source)     
    try:                            
        text = r.recognize_google(audio)    #to convert text into audio#
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

import speech_recognition as sr



def listen_for_command():
    recognizer = sr.Recognizer()
    global command

    with sr.Microphone() as source:
            print("Smelling For Girth")
            recognizer.adjust_for_ambient_noise(source)
            
            audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("the Girth Mule said:\n", command)
        return command.lower()
    except sr.UnknownValueError:
        print("could not smell Girth")
            
        return None
    except sr.RequestError:
        print("can't get through boss")
        return None
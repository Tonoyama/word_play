import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("なんか言ってみて！")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print ("Now to recognize it...")

    try:
        print(r.recognize_google(audio, language='ja-JP'))

    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
# 1) input --> english audio (mic)
# 2) convert --> audio to english text
# 3) translate --> english text to arabic text
# 4) convert --> arabic text to audio
# 5) output --> Arabic audio

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os


recog1 = spr.Recognizer()

mc = spr.Microphone()

translator = Translator()


from_lang = 'en'
to_lang = 'ar'

with mc as source:

    print("Speak a stentence...")
    recog1.adjust_for_ambient_noise(source, duration=0.2)

    # Storing the speech into audio variable
    audio = recog1.listen(source)

    # convert audio into text
    get_sentence = recog1.recognize_google(audio)

    try:
      # Printing Speech which need to
      # be translated.
        print("Phase to be Translated :" + get_sentence)

        text_to_translate = translator.translate(
            get_sentence, src=from_lang, dest=to_lang)

        # Storing the translated text in text var
        text = text_to_translate.text
        # print(text)

        speak = gTTS(text=text, lang=to_lang, slow=False)
        speak.save("voice.mp3")

        # Using OS module to run the translated voice.
        os.system("start voice.mp3")

    except spr.UnknownValueError:
        print("Unable to Understand the Input")

    except spr.RequestError as e:
        print("Unable to provide Required Output".format(e))

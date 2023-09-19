from multiprocessing import Process
import speech_recognition as sr
import time

from text2speech import speak
from translation import translate

sr.__version__ = '3.10.0'

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def process_sound():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        try:
            audio2 = recognizer.listen(source, phrase_time_limit=5)
            original_text = recognizer.recognize_google(audio2, language="id")
            original_text = original_text.lower()
            print(original_text)
            translated_text = translate(original_text, lang="en")
            if original_text == translated_text:
                return False
            if translated_text:
                speak(translated_text)
        except Exception as e:
            print(e)
            return False
        
if __name__ == '__main__':
    number_of_processors = 10

    key_logger = input("Run Speech Recognition by pressing enter")
    if key_logger != None:
        while True:
            time_interval = 4.99997
            processed = []
            for i in range(number_of_processors + 1):
                recognizer_function = Process(
                    target=process_sound, args=())
                processed.append(recognizer_function)
                recognizer_function.start()
                time.sleep(time_interval)

            for process in processed:
                process.join()
            
def process_sound():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        try:
            audio2 = recognizer.listen(source, phrase_time_limit=5)
            original_text = recognizer.recognize_google(audio2, language="id")
            original_text = original_text.lower()
            return original_text
        except Exception as e:
            return False
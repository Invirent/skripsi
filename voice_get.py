from multiprocessing import Process
import speech_recognition as sr
import pyttsx3 as tts
import time

from translation import translate

sr.__version__ = '3.10.0'

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speaktext(voice):
    engine = tts.init()
    engine.say(voice)
    engine.runAndWait()

def process_sound():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio2 = recognizer.listen(source, timeout=3, phrase_time_limit=8)
        try:
            original_text = recognizer.recognize_google(audio2, language="id")
            original_text = original_text.lower()
            
            translated_text = translate(original_text, lang="en")
            speaktext(translated_text)
        except Exception as e:
            return False
        
if __name__ == '__main__':
    number_of_processors = 3

    key_logger = input("Run Speech Recognition by pressing enter")
    if key_logger != None:
        while True:
            time_interval = 7.999999
            processed = []
            for i in range(3):
                recognizer_function = Process(
                    target=process_sound, args=())
                processed.append(recognizer_function)
                recognizer_function.start()
                time.sleep(time_interval)

            for process in processed:
                process.join()
            

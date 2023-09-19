# Google Translate API
# from googletrans import Translator

# Translator.__version__ = '4.0.0rc1'

# translator = Translator()

# def translate(to_translate, lang):
#     return translator.translate(text=to_translate, dest=str(lang), src="id").text

# text = "Perkenalkan, nama saya carlos dan saya merupakan mahasiswa UPH"
# print(translate(text, "en"))

# My Memory API
import requests

def translate(to_translate, lang):
    if lang == "en":
        src = "id"
    else:
        src = "en"
        
    langpair = "%s|%s" % (src,lang)
    get_value = f"get?q={to_translate}&langpair={langpair}"
    api_key = f"https://api.mymemory.translated.net/{get_value}"
    
    response = requests.get(str(api_key))
    if response.status_code == 200:
        translated = response.json()["responseData"]["translatedText"]
        matches = response.json()["matches"]
        for data in matches:
            if data["created-by"] == "MT!":
                translated = data["translation"]
        print(translated)
        return translated
    else:
        return False
    

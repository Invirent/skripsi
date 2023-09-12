from googletrans import Translator

Translator.__version__ = '4.0.0rc1'

translator = Translator()

def translate(to_transalte, lang):
    return Translator.translate(to_transalte, dest=str(lang))

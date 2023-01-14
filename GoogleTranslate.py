from googletrans import Translator



class GoogleTranslate:

    def __init__(self, text):
        self.text = text
        self.langUA = 'uk'
        self.langRU = 'ru'
        self.langDE = 'de'
        self.langEN = 'en'

    def get_translated(self, fromlang, tolang):
        translator = Translator()
        result = translator.translate(self.text, src=fromlang, dest=tolang)
        return result.text.replace("'", '&apos;').replace('\n', '<br>').replace('\r', '')







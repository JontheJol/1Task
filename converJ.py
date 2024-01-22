import codecs
import json
class Archivo:

    def safe(self, path, text):
        with codecs.open(path, "w", encoding="utf-8") as file:
            text = text.replace("'", '"')
            file.write(text)
            file.close

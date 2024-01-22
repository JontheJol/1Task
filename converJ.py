import codecs
import json
class Archivo:

    def safe(self, path, text):
        with codecs.open(path, "w", encoding="utf-8") as file:
            text = text.replace("'", '"')
            text = text.replace("{","{\n")
            text = text.replace("}","\n}")
            file.write(text)
            file.close

    def read(self, path):
        with codecs.open(path, "r", encoding="utf-8") as file:
            text =json.load(file)
            return text

import codecs
import json
class Archivo:
    def safe(self, path, text):
        file = codecs.open(path, "w", "utf-8")
        file.write(json.dumps(text, indent=4, quoting=json.QUOTE_SINGLE))
        file.close()

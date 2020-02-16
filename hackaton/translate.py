from googletrans import Translator
translator = Translator()
result = translator.translate(["Best notebook","Best hui"], dest="ru")
print(result[0].text, result[1].text)
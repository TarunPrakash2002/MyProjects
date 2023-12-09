from translate import Translator

translator = Translator(to_lang="hi")
try:
    with open('textEN.txt', mode="r") as file:
        t = file.read()
        trans = translator.translate(t)
        with open('textHI.txt', mode="w", encoding='utf8') as f:
            f.write(trans)

except FileNotFoundError:
    print('File doesnt exist')

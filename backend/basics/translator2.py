from googletrans import Translator

tr = Translator()

s = input("Enter your sentence: ")

dest = input("Enter the language code of preferred language: ")

print(f'This sentence translates to: {tr.translate(s, dest=dest).text}')
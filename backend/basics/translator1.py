from googletrans import Translator

tr = Translator()

s = input("Enter your sentence: ")

print(f'This sentence translates to: {tr.translate(s).text}')
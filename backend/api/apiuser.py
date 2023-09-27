import requests

s = input("Enter your sentence: ")

dest = input("Enter the language code of preferred language (default en): ") 

rt = requests.get(f"http://127.0.0.1:8000/api/translate/?s={s}&dest={dest if dest else 'en'}").json()
rd = requests.get(f"http://127.0.0.1:8000/api/detect/?s={s}").json()

print(f"language detected: {rd['lang-name']}")
print(f"destination: {rt['destination']}")
print(f"This sentence translates to: {rt['translation']}")
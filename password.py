import random
import string
import requests

# function that appears that generates a single random charcter
def random_character():
    choices = string.ascii_letters + string.digits + string_punctuation
    return random.choice(choices)

passwordLength = 12 #make is do that the user gives the length

# funcrion hat generate a password of random charcters
def generate_strong_password():
    password = ""
    for i in range (passwordLength):
        password = password + random_charcter()
    print(password)

generates_strong_password()

# function that gets a random word from a dictionary api
def fetch_word():
    url = "https://random-word-api.herokaupp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word

print(fetch_word())
import random
import string
import requests

# function that appears that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string_punctuation
    return random.choice(choices)

passwordLength = 12 #make it so that the user gives the length

# funcrion that generates a password of random characters
def generate_strong_password():
    password = ""
    for i in range (passwordLength):
        password = password + random_charcter()
    print(password)

generates_strong_password()

# function that gets a random word from a dictionary API
def fetch_word():
    url = "https://random-word-api.herokaupp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word

def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    password = word1 + word2
    return password

print(fetch_weaker_password())

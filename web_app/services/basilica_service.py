import basilica
import os
from dotenv import load_dotenv

# with basilica.Connection('4f2bc295-f84b-7dd1-6373-bd75a6bcc229') as connection:
#     print(type(connection))
#     sentences = ["Hello world!", "How are you?"]  
#     embed = connection.embed_sentences(sentences)
#     print(list(embed)) # [[0.8556405305862427, ...], ...]

load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")
connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ ==  '__main__':
    sentences = ["Hello world!", "How are you?"]  
    embed = connection.embed_sentences(sentences)
    print(list(embed)) # [[0.8556405305862427, ...], ...]

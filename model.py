import __future__
from builtins import print

from random import random, randrange
from answers import answers

# import nltk
# nltk.download("stopwords")

class AI:
    def __init__(self) -> None:
        pass

    def length(self,c):
        print("length:", len(c))

    def greet(self):
        greeting = ["hello.", "hey, how are you doing?", "yo.", "hi there.", "hi!", "how are you?", "how are you doing?"]
        rnumber = randrange(len(greeting))
        print(greeting[rnumber])

    def analyze(self, q):
        self.length(q)
        print(q)

    def answer(self, q):
        original_query = q
        split_query = q.split()
        self.analyze(q)
        print(split_query)

ai = AI()

ai.greet()

ai.answer("blah test")

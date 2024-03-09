"""
https://www.youtube.com/watch?v=3ohzBxoFHAY
https://www.youtube.com/watch?v=3iJjBOne2sM
https://www.youtube.com/watch?v=sugvnHA7ElY # if __name__=="__main__"

https://www.youtube.com/watch?v=1I3fuDR2S9A
"""


class Dunder:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


d1 = Dunder("Tommy")
print(d1.name)
d1.name = "Bob"
print(d1.name)

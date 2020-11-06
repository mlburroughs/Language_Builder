"""

Classification of French words:
type, m/f

Author: Michelle Burroughs

"""

class Francais:

    def __init__(self, type, gender):
        self.type = type
        self.gender = gender

    def genderGen(self):
        if self.gender == "f":
            article1 = "la"
            article2 = "une"
        elif self.gender == "m":
            article1 = "le"
            article2 = "un"
        elif self.gender == "na":
            article1 = "not appliciable"
            article2 = "not appliciable"

    def typeGen(self):
        if self.type == "verb":
            print("I am a verb")
        elif self.type == "noun":
            print("I am a noun")
        elif self.type == "adj":
            print("I am an adjective")
        elif self.type == "pronoun":
            print("I am a pronoun")

moi = Francais("pronoun", "na")
print(moi.type)
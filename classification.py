"""

Classification of French words:
type, m/f

Author: Michelle Burroughs

"""

class francais:

    def __init__(self, type, gender):
        self.type = type
        self.gender = gender

    def genderGen(self):
        if self.gender == f:
            article1 = "la"
            article2 = "une"
        elif self.gender == m:
            article1 = "le"
            article2 = "un"

    def typeGen(self):
        if self.type == verb:
            # function to generate tenses
        elif self.type == noun:
            # function tbd
        elif self.type == adjectif:
            # function tbd
        elif self.type == pronoun:
            # function tbd

"""
Verb Tense Generator for French Language

Author: Michelle Burroughs

"""

def presentTense(inf, type):

    # Irregular verbs:
    if type == "irreg":
        if inf == "avoir":
            je = "ai"
            tu = "as"
            il_elle = "a"
            nous = "avons"
            vous = "avez"
            ils_elles = "ont"

        if inf == "etre":
            je = "suis"
            tu = "es"
            il_elle = "e"
            nous = "sommes"
            vous = "etes"
            ils_elles = "sont"

        if inf == "aller":
            je = "vais"
            tu = "vas"
            il_elle = "va"
            nous = "allons"
            vous = "allez"
            ils_elles = "vont"

        if inf == "faire":
            je = "fais"
            tu = "fais"
            il_elle = "fait"
            nous = "faisons"
            vous = "faites"
            ils_elles = "font"

    if type == "model":
        if inf == "vouloir":
            je = "veux"
            tu = "veux"
            il_elle = "veut"
            nous = "voulons"
            vous = "voulez"
            ils_elles = "veulent"

        if inf == "pouvoir":
            je = "peux"
            tu = "peux"
            il_elle = "peut"
            nous = "pouvons"
            vous = "pouvez"
            ils_elles = "peuvent"

        if inf == "devoir":
            je = "dois"
            tu = "dois"
            il_elle = "doit"
            nous = "devons"
            vous = "devez"
            ils_elles = "doivent"

        if inf == "savoir":
            je = "sais"
            tu = "sais"
            il_elle = "sait"
            nous = "savons"
            vous = "savez"
            ils_elles = "savent"

    if type == "irreg_g":
        if inf == "manger":
            je = "mange"
            tu = "manges"
            il_elle = "mange"
            nous = "mangeons"
            vous = "mangez"
            ils_elles = "mangent"

        if inf == "bouger":
            je = "bouge"
            tu = "bouges"
            il_elle = "bouge"
            nous = "bougeons"
            vous = "bougez"
            ils_elles = "bougent"

        if inf == "corriger":
            je = "corrige"
            tu = "corriges"
            il_elle = "corrige"
            nous = "corrigeons"
            vous = "corrigez"
            ils_elles = "corrigent"

        if inf == "voyager":
            je = "voyage"
            tu = "voyages"
            il_elle = "voyage"
            nous = "voyageons"
            vous = "voyagez"
            ils_elles = "voyagent"

    if type == "irreg_er":
        if inf == "appeler":
            je = "appelle"
            tu = "appelles"
            il_elle = "appelle"
            nous = "appelons"
            vous = "appelez"
            ils_elles = "appellent"

        if inf == "rappeler":
            je = "rappelle"
            tu = "rappelles"
            il_elle = "rappelle"
            nous = "rappelons"
            vous = "rappelez"
            ils_elles = "rappellent"

        if inf == "jeter":
            je = "jette"
            tu = "jettes"
            il_elle = "jette"
            nous = "jetons"
            vous = "jetez"
            ils_elles = "jettent"

        if inf == "rire":
            je = "ris"
            tu = "ris"
            il_elle = "rit"
            nous = "rions"
            vous = "riez"
            ils_elles = "rient"

        if inf == "dire":
            je = "dis"
            tu = "dis"
            il_elle = "dit"
            nous = "disons"
            vous = "dites"
            ils_elles = "disent"

        if inf == "ecrire":
            je = "ecris"
            tu = "ecris"
            il_elle = "ecrit"
            nous = "ecrivons"
            vous = "ecrivez"
            ils_elles = "ecrivent"

        if inf == "lire":
            je = "lis"
            tu = "lis"
            il_elle = "lit"
            nous = "lisons"
            vous = "lisez"
            ils_elles = "lisent"

    if type == "irreg_ir":
        if inf == "tenir":
            je = "tiens"
            tu = "tiens"
            il_elle = "tient"
            nous = "tenons"
            vous = "tenez"
            ils_elles = "tiennent"

        if inf == "venir":
            je = "viens"
            tu = "viens"
            il_elle = "vient"
            nous = "venons"
            vous = "venez"
            ils_elles = "viennent"

        if inf == "tenir":
            je = "tiens"
            tu = "tiens"
            il_elle = "tient"
            nous = "tenons"
            vous = "tenez"
            ils_elles = "tiennent"

        if inf == "ouvrir":
            je = "ouvre"
            tu = "ouvres"
            il_elle = "ouvre"
            nous = "ouvrons"
            vous = "ouvrez"
            ils_elles = "ouvrent"

        if inf == "couvrir":
            je = "couvre"
            tu = "couvres"
            il_elle = "couvre"
            nous = "couvrons"
            vous = "couvrez"
            ils_elles = "couvrent"

        if inf == "decouvrir":
            je = "decouvre"
            tu = "decouvres"
            il_elle = "decouvre"
            nous = "decouvrons"
            vous = "decouvrez"
            ils_elles = "decouvrent"

        if inf == "devenir":
            je = "deviens"
            tu = "deviens"
            il_elle = "devient"
            nous = "devenons"
            vous = "devenez"
            ils_elles = "deviennent"

        if inf == "obtenir":
            je = "obtiens"
            tu = "obtiens"
            il_elle = "obtient"
            nous = "obtenons"
            vous = "obtenez"
            ils_elles = "obtiennent"

        if inf == "appartenir":
            je = "appartiens"
            tu = "appartiens"
            il_elle = "appartient"
            nous = "appartenons"
            vous = "appartenez"
            ils_elles = "appartiennent"

    if type == "irreg_oir":
        if inf == "voir":
            je = "vois"
            tu = "vois"
            il_elle = "voit"
            nous = "voyons"
            vous = "voyez"
            ils_elles = "voient"

        if inf == "recevoir":
            je = "recois"
            tu = "recois"
            il_elle = "recoit"
            nous = "recevons"
            vous = "recevez"
            ils_elles = "recoivent"

    if type == "irreg_restem":
        if inf == "prendre"
            je = "prends"
            tu = "prends"
            il_elle = "prend"
            nous = "prenons"
            vous = "prenez"
            ils_elles = "prennent"

        if inf == "apprendre":
            je = "apprends"
            tu = "apprends"
            il_elle = "apprend"
            nous = "apprenons"
            vous = "apprenez"
            ils_elles = "apprennent"

        if inf == "comprendre":
            je = "comprends"
            tu = "comprends"
            il_elle = "comprend"
            nous = "comprenons"
            vous = "comprenez"
            ils_elles = "comprennent"

        if inf == "surprendre":
            je = "surprends"
            tu = "surprends"
            il_elle = "surprend"
            nous = "surprenons"
            vous = "surprenez"
            ils_elles = "surprennent"

        if inf == "croire":
            je = "crois"
            tu = "crois"
            il_elle = "croit"
            nous = "croyons"
            vous = "croyez"
            ils_elles = "croient"

        if inf == "boire":
            je = "bois"
            tu = "bois"
            il_elle = "boit"
            nous = "buvons"
            vous = "buvez"
            ils_elles = "boivent"

        if inf == "battre":
            je = "bats"
            tu = "bats"
            il_elle = "bat"
            nous = "battons"
            vous = "battez"
            ils_elles = "battent"

        if inf == "mettre":
            je = "mets"
            tu = "mets"
            il_elle = "met"
            nous = "mettons"
            vous = "mettez"
            ils_elles = "mettent"

        if inf == "admettre":
            je = "admets"
            tu = "admets"
            il_elle = "admet"
            nous = "admettons"
            vous = "admettez"
            ils_elles = "admettent"

        if inf == "permettre":
            je = "permets"
            tu = "permets"
            il_elle = "permet"
            nous = "permettons"
            vous = "permettez"
            ils_elles = "permettent"

        if inf == "promettre":
            je = "promets"
            tu = "promets"
            il_elle = "promet"
            nous = "promettons"
            vous = "promettez"
            ils_elles = "promettent"

        if inf == "vivre":
            je = "vis"
            tu = "vis"
            il_elle = "vit"
            nous = "vivons"
            vous = "vivez"
            ils_elles = "vivent"

    # For all regular verbs:
    if type == "er":
        root = inf[:-2]
        je = root + "e"
        tu = root + "es"
        il_elle = root + "e"
        nous = root + "ons"
        vous = root + "ez"
        ils_elles = root + "ent"

    if type == "ir":
        root = inf[:-2]
        je = root + "is"
        tu = root + "is"
        il_elle = root + "it"
        nous = root + "issons"
        vous = root + "issez"
        ils_elles = root + "issent"

    if type == "re":
        root = inf[:-2]
        je = root + "s"
        tu = root + "s"
        il_elle = root
        nous = root + "ons"
        vous = root + "ez"
        ils_elles = root + "ent"

    return je, tu, il_elle, nous, vous, ils_elles


def pastParticipe(inf, type):

    if type == "er":
        pp = inf[:-1]

    if type == "irreg_restem":
        pp = inf[:-1]

    if type == "ir":
        pp = inf[:-1]

    if type == "re":
        pp = inf[:-2]
        pp += "u"

    return pp

irregpp = {'acquerir': 'acquis','apprendre': 'appris','atteindre': 'atteint', 'avoir': 'eu',
           'boire': 'bu', 'comprendre': 'compris', 'conduire': 'conduit', 'connaitre': 'connu',
           'construire': 'construit', 'courir': 'couru', 'couvrir': 'couvert', 'craindre': 'craint',
           'croire': 'cru', 'decevoir': 'decu', 'decouvrir': 'decouvert', 'devoir': 'du',
           'dire': 'dit', 'ecrire': 'ecrit', 'etre': 'ete', 'faire': 'fait', 'instruire': 'instruit',
           'joindre': 'joint', 'lire': 'lu', 'mettre': 'mis', 'mourir': 'mort', 'naitre': 'ne',
           'offrir': 'offert', 'ouvrir': 'ouvert', 'paraitre': 'paru', 'peindre': 'peint',
           'pouvoir': 'pu', 'prendre': 'pris', 'produire': 'produit', 'recevoir': 'recu',
           'savoir': 'su', 'souffrir': 'souffert', 'suivre': 'suivi', 'tenir': 'tenu', 'venir': 'venu',
           'vivre': 'vecu', 'voir': 'vu', 'vouloir': 'voulu'}

def imparfaitTense(inf, type):
    if type == "er" or "ir" or "re" or "model" or "irreg_er" or "irreg_oir" or "irreg_ir" or "irreg_restem":
        root = inf[:-2]
        je = root + "ais"
        tu = root + "ais"
        il_elle = root + "ait"
        nous = root + "ions"
        vous = root + "iez"
        ils_elles = root + "aient"

    # Irregular verbs:
    if type == "irreg":
        if inf == "avoir":
                je = "avais"
                tu = "avais"
                il_elle = "avait"
                nous = "avions"
                vous = "aviez"
                ils_elles = "aient"

        if inf == "etre":
                je = "etais"
                tu = "etais"
                il_elle = "etait"
                nous = "etions"
                vous = "etiez"
                ils_elles = "etaient"

        if inf == "aller":
                je = "allais"
                tu = "allais"
                il_elle = "allait"
                nous = "allions"
                vous = "alliez"
                ils_elles = "allaient"

        if inf == "faire":
                je = "faisais"
                tu = "faisais"
                il_elle = "faisait"
                nous = "faisions"
                vous = "faisiez"
                ils_elles = "fasaient"

    if type == "irreg_ir":
        root = inf[:-2]
        je = root + "issais"
        tu = root + "issais"
        il_elle = root + "issait"
        nous = root + "issions"
        vous = root + "issiez"
        ils_elles = root + "issaient"

    if type == "irreg_g":
        if inf == "manger":
            je = "mangeais"
            tu = "mangesais"
            il_elle = "mangeait"
            nous = "mangions"
            vous = "mangiez"
            ils_elles = "mangeaient"

        if inf == "bouger":
            je = "bouge"
            tu = "bouges"
            il_elle = "bouge"
            nous = "bougeons"
            vous = "bougez"
            ils_elles = "bougent"

        if inf == "corriger":
            je = "corrige"
            tu = "corriges"
            il_elle = "corrige"
            nous = "corrigeons"
            vous = "corrigez"
            ils_elles = "corrigent"

        if inf == "voyager":
            je = "voyage"
            tu = "voyages"
            il_elle = "voyage"
            nous = "voyageons"
            vous = "voyagez"
            ils_elles = "voyagent"

    return je, tu, il_elle, nous, vous, ils_elles


def futurprocheTense(inf):
    first = presentTense("aller", "irreg")
    je = first[0] + " " + inf
    tu = first[1] + " " + inf
    il_elle = first[2] + " " + inf
    nous = first[3] + " " + inf
    vous = first[4] + " " + inf
    ils_elles = first[5] + " " + inf

    return je, tu, il_elle, nous, vous, ils_elles


def futurTense(inf, type):

    if type == "er" or "ir" or "re" or "model" or "irreg_er" or "irreg_oir" or "irreg_ir" or "irreg_restem":
        je = inf + "ai"
        tu = inf + "as"
        il_elle = inf + "a"
        nous = inf + "ons"
        vous = inf + "ez"
        ils_elles = inf + "ont"

    # Irregular verbs:
    if type == "irreg":
        if inf == "avoir":
                je = "aurai"
                tu = "auras"
                il_elle = "aura"
                nous = "aurons"
                vous = "aurez"
                ils_elles = "auront"

        if inf == "etre":
                je = "serai"
                tu = "seras"
                il_elle = "sera"
                nous = "serons"
                vous = "serez"
                ils_elles = "seront"

        if inf == "aller":
                je = "irai"
                tu = "iras"
                il_elle = "ira"
                nous = "irons"
                vous = "irez"
                ils_elles = "iront"

        if inf == "faire":
                je = "ferai"
                tu = "feras"
                il_elle = "fera"
                nous = "ferons"
                vous = "ferez"
                ils_elles = "feront"

    return je, tu, il_elle, nous, vous, ils_elles


def conditionelpresentMood(inf):

    je = inf + "ais"
    tu = inf + "ais"
    il_elle = inf + "ait"
    nous = inf + "ions"
    vous = inf + "iez"
    ils_elles = inf + "ont"

    return je, tu, il_elle, nous, vous, ils_elles

# Plus-que-parfait Tense
def plusqueparfaitTense(inf, type, subtype, reflexive):

    if subtype or reflexive:
        imparfaitEtre = imparfaitTense("etre", "irreg")
        je = imparfaitEtre[0] + " " + pastParticipe(inf,type)
        tu = imparfaitEtre[1] + " " + pastParticipe(inf,type)
        il_elle = imparfaitEtre[2] + " " + pastParticipe(inf,type)
        nous = imparfaitEtre[3] + " " + pastParticipe(inf,type)
        vous = imparfaitEtre[4] + " " + pastParticipe(inf,type)
        ils_elles = imparfaitEtre[5] + " " + pastParticipe(inf,type)
    else:
        impartfaitAvoir = imparfaitTense("avoir", "irreg")
        je = imparfaitAvoir[0] + " " + pastParticipe(inf, type)
        tu = imparfaitAvoir[1] + " " + pastParticipe(inf, type)
        il_elle = imparfaitAvoir[2] + " " + pastParticipe(inf, type)
        nous = imparfaitAvoir[3] + " " + pastParticipe(inf, type)
        vous = imparfaitAvoir[4] + " " + pastParticipe(inf, type)
        ils_elles = imparfaitAvoir[5] + " " + pastParticipe(inf, type)

    return je, tu, il_elle, nous, vous, ils_elles

# Future Anterieur Tense
def futuranterieurTense(inf, type, subtype, reflexive):

    if subtype or reflexive:
        condEtre = conditionelpresentMood("etre", "irreg")
        je = condEtre[0] + " " + pastParticipe(inf, type)
        tu = condEtre[1] + " " + pastParticipe(inf, type)
        il_elle = condEtre[2] + " " + pastParticipe(inf, type)
        nous = condEtre[3] + " " + pastParticipe(inf, type)
        vous = condEtre[4] + " " + pastParticipe(inf, type)
        ils_elles = condEtre[5] + " " + pastParticipe(inf, type)
    else:
        condAvoir = conditionelpresentMood("avoir", "irreg")
        je = condAvoir[0] + " " + pastParticipe(inf, type)
        tu = condAvoir[1] + " " + pastParticipe(inf, type)
        il_elle = condAvoir[2] + " " + pastParticipe(inf, type)
        nous = condAvoir[3] + " " + pastParticipe(inf, type)
        vous = condAvoir[4] + " " + pastParticipe(inf, type)
        ils_elles = condAvoir[5] + " " + pastParticipe(inf, type)

    return je, tu, il_elle, nous, vous, ils_elles


# Subjontif
def subjoctifTense(inf, type):
    return


# Passe Compose
def passecomposeTense(inf, type, subtype, reflexive):

    if subtype or reflexive:
        etre = presentTense("etre","irreg")
        je = etre[0] + pastParticipe(inf, type)
        tu = etre[1] + pastParticipe(inf, type)
        il_elle = etre[2] + pastParticipe(inf, type)
        nous = etre[3] + pastParticipe(inf, type)
        vous = etre[4] + pastParticipe(inf, type)
        ils_elles = etre[5] + pastParticipe(inf, type)
    else:
        avoir = presentTense("avoir","irreg")
        je = avoir[0] + pastParticipe(inf, type)
        tu = avoir[1] + pastParticipe(inf, type)
        il_elle = avoir[2] + pastParticipe(inf, type)
        nous = avoir[3] + pastParticipe(inf, type)
        vous = avoir[4] + pastParticipe(inf, type)
        ils_elles = avoir[5] + pastParticipe(inf, type)

    return je, tu, il_elle, nous, vous, ils_elles


def passesimpleTense(inf, type):
    return

def imperatifMood(inf, type):
    return

def participeMood(inf, type):

    return

def indicatifMood(inf, type):

    return

print(presentTense("avoir", "irreg"))
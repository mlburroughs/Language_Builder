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
        elif inf == "etre":
            je = "suis"
            tu = "es"
            il_elle = "e"
            nous = "sommes"
            vous = "etes"
            ils_elles = "sont"
        elif inf == "aller":
            je = "vais"
            tu = "vas"
            il_elle = "va"
            nous = "allons"
            vous = "allez"
            ils_elles = "vont"
        elif inf == "faire":
            je = "fais"
            tu = "fais"
            il_elle = "fait"
            nous = "faisons"
            vous = "faites"
            ils_elles = "font"

    elif type == "model":
        if inf == "vouloir":
            je = "veux"
            tu = "veux"
            il_elle = "veut"
            nous = "voulons"
            vous = "voulez"
            ils_elles = "veulent"
        elif inf == "pouvoir":
            je = "peux"
            tu = "peux"
            il_elle = "peut"
            nous = "pouvons"
            vous = "pouvez"
            ils_elles = "peuvent"
        elif inf == "devoir":
            je = "dois"
            tu = "dois"
            il_elle = "doit"
            nous = "devons"
            vous = "devez"
            ils_elles = "doivent"
        elif inf == "savoir":
            je = "sais"
            tu = "sais"
            il_elle = "sait"
            nous = "savons"
            vous = "savez"
            ils_elles = "savent"

    elif type == "irreg_g":
        if inf == "manger":
            je = "mange"
            tu = "manges"
            il_elle = "mange"
            nous = "mangeons"
            vous = "mangez"
            ils_elles = "mangent"
        elif inf == "bouger":
            je = "bouge"
            tu = "bouges"
            il_elle = "bouge"
            nous = "bougeons"
            vous = "bougez"
            ils_elles = "bougent"
        elif inf == "corriger":
            je = "corrige"
            tu = "corriges"
            il_elle = "corrige"
            nous = "corrigeons"
            vous = "corrigez"
            ils_elles = "corrigent"
        elif inf == "voyager":
            je = "voyage"
            tu = "voyages"
            il_elle = "voyage"
            nous = "voyageons"
            vous = "voyagez"
            ils_elles = "voyagent"

    elif type == "irreg_er":
        if inf == "appeler":
            je = "appelle"
            tu = "appelles"
            il_elle = "appelle"
            nous = "appelons"
            vous = "appelez"
            ils_elles = "appellent"
        elif inf == "rappeler":
            je = "rappelle"
            tu = "rappelles"
            il_elle = "rappelle"
            nous = "rappelons"
            vous = "rappelez"
            ils_elles = "rappellent"
        elif inf == "jeter":
            je = "jette"
            tu = "jettes"
            il_elle = "jette"
            nous = "jetons"
            vous = "jetez"
            ils_elles = "jettent"
        elif inf == "rire":
            je = "ris"
            tu = "ris"
            il_elle = "rit"
            nous = "rions"
            vous = "riez"
            ils_elles = "rient"
        elif inf == "dire":
            je = "dis"
            tu = "dis"
            il_elle = "dit"
            nous = "disons"
            vous = "dites"
            ils_elles = "disent"
        elif inf == "ecrire":
            je = "ecris"
            tu = "ecris"
            il_elle = "ecrit"
            nous = "ecrivons"
            vous = "ecrivez"
            ils_elles = "ecrivent"
        elif inf == "lire":
            je = "lis"
            tu = "lis"
            il_elle = "lit"
            nous = "lisons"
            vous = "lisez"
            ils_elles = "lisent"

    elif type == "irreg_ir":
        if inf == "tenir":
            je = "tiens"
            tu = "tiens"
            il_elle = "tient"
            nous = "tenons"
            vous = "tenez"
            ils_elles = "tiennent"
        elif inf == "venir":
            je = "viens"
            tu = "viens"
            il_elle = "vient"
            nous = "venons"
            vous = "venez"
            ils_elles = "viennent"
        elif inf == "tenir":
            je = "tiens"
            tu = "tiens"
            il_elle = "tient"
            nous = "tenons"
            vous = "tenez"
            ils_elles = "tiennent"
        elif inf == "ouvrir":
            je = "ouvre"
            tu = "ouvres"
            il_elle = "ouvre"
            nous = "ouvrons"
            vous = "ouvrez"
            ils_elles = "ouvrent"
        elif inf == "couvrir":
            je = "couvre"
            tu = "couvres"
            il_elle = "couvre"
            nous = "couvrons"
            vous = "couvrez"
            ils_elles = "couvrent"
        elif inf == "decouvrir":
            je = "decouvre"
            tu = "decouvres"
            il_elle = "decouvre"
            nous = "decouvrons"
            vous = "decouvrez"
            ils_elles = "decouvrent"
        elif inf == "devenir":
            je = "deviens"
            tu = "deviens"
            il_elle = "devient"
            nous = "devenons"
            vous = "devenez"
            ils_elles = "deviennent"
        elif inf == "obtenir":
            je = "obtiens"
            tu = "obtiens"
            il_elle = "obtient"
            nous = "obtenons"
            vous = "obtenez"
            ils_elles = "obtiennent"
        elif inf == "appartenir":
            je = "appartiens"
            tu = "appartiens"
            il_elle = "appartient"
            nous = "appartenons"
            vous = "appartenez"
            ils_elles = "appartiennent"

    elif type == "irreg_oir":
        if inf == "voir":
            je = "vois"
            tu = "vois"
            il_elle = "voit"
            nous = "voyons"
            vous = "voyez"
            ils_elles = "voient"
        elif inf == "recevoir":
            je = "recois"
            tu = "recois"
            il_elle = "recoit"
            nous = "recevons"
            vous = "recevez"
            ils_elles = "recoivent"

    elif type == "irreg_restem":
        if inf == "prendre":
            je = "prends"
            tu = "prends"
            il_elle = "prend"
            nous = "prenons"
            vous = "prenez"
            ils_elles = "prennent"
        elif inf == "apprendre":
            je = "apprends"
            tu = "apprends"
            il_elle = "apprend"
            nous = "apprenons"
            vous = "apprenez"
            ils_elles = "apprennent"
        elif inf == "comprendre":
            je = "comprends"
            tu = "comprends"
            il_elle = "comprend"
            nous = "comprenons"
            vous = "comprenez"
            ils_elles = "comprennent"
        elif inf == "surprendre":
            je = "surprends"
            tu = "surprends"
            il_elle = "surprend"
            nous = "surprenons"
            vous = "surprenez"
            ils_elles = "surprennent"
        elif inf == "croire":
            je = "crois"
            tu = "crois"
            il_elle = "croit"
            nous = "croyons"
            vous = "croyez"
            ils_elles = "croient"
        elif inf == "boire":
            je = "bois"
            tu = "bois"
            il_elle = "boit"
            nous = "buvons"
            vous = "buvez"
            ils_elles = "boivent"
        elif inf == "battre":
            je = "bats"
            tu = "bats"
            il_elle = "bat"
            nous = "battons"
            vous = "battez"
            ils_elles = "battent"
        elif inf == "mettre":
            je = "mets"
            tu = "mets"
            il_elle = "met"
            nous = "mettons"
            vous = "mettez"
            ils_elles = "mettent"
        elif inf == "admettre":
            je = "admets"
            tu = "admets"
            il_elle = "admet"
            nous = "admettons"
            vous = "admettez"
            ils_elles = "admettent"
        elif inf == "permettre":
            je = "permets"
            tu = "permets"
            il_elle = "permet"
            nous = "permettons"
            vous = "permettez"
            ils_elles = "permettent"
        elif inf == "promettre":
            je = "promets"
            tu = "promets"
            il_elle = "promet"
            nous = "promettons"
            vous = "promettez"
            ils_elles = "promettent"
        elif inf == "vivre":
            je = "vis"
            tu = "vis"
            il_elle = "vit"
            nous = "vivons"
            vous = "vivez"
            ils_elles = "vivent"

    # For all regular verbs:
    elif type == "er":
        root = inf[:-2]
        je = root + "e"
        tu = root + "es"
        il_elle = root + "e"
        nous = root + "ons"
        vous = root + "ez"
        ils_elles = root + "ent"

    elif type == "ir":
        root = inf[:-2]
        je = root + "is"
        tu = root + "is"
        il_elle = root + "it"
        nous = root + "issons"
        vous = root + "issez"
        ils_elles = root + "issent"

    elif type == "re":
        root = inf[:-2]
        je = root + "s"
        tu = root + "s"
        il_elle = root
        nous = root + "ons"
        vous = root + "ez"
        ils_elles = root + "ent"

    return je, tu, il_elle, nous, vous, ils_elles


# Past Participe
def pastParticipe(inf, type):

    if type == "er":
        pp = inf[:-1]
    elif type == "irreg_restem":
        pp = inf[:-1]
    elif type == "ir":
        pp = inf[:-1]
    elif type == "re":
        pp = inf[:-2]
        pp += "u"
    else:
        pp = irregpp[inf]

    return pp

# Irregular verb past participe dictionary
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


#Imparfait Verb Tense
def imparfaitTense(inf, type):

    # Irregular verbs:
    if type == "irreg":
        if inf == "avoir":
            je = "avais"
            tu = "avais"
            il_elle = "avait"
            nous = "avions"
            vous = "aviez"
            ils_elles = "aient"
        elif inf == "etre":
            je = "etais"
            tu = "etais"
            il_elle = "etait"
            nous = "etions"
            vous = "etiez"
            ils_elles = "etaient"
        elif inf == "aller":
                je = "allais"
                tu = "allais"
                il_elle = "allait"
                nous = "allions"
                vous = "alliez"
                ils_elles = "allaient"
        elif inf == "faire":
                je = "faisais"
                tu = "faisais"
                il_elle = "faisait"
                nous = "faisions"
                vous = "faisiez"
                ils_elles = "fasaient"
    elif type == "irreg_ir":
        root = inf[:-2]
        je = root + "issais"
        tu = root + "issais"
        il_elle = root + "issait"
        nous = root + "issions"
        vous = root + "issiez"
        ils_elles = root + "issaient"
    elif type == "irreg_g":
        if inf == "manger":
            je = "mangeais"
            tu = "mangesais"
            il_elle = "mangeait"
            nous = "mangions"
            vous = "mangiez"
            ils_elles = "mangeaient"
        elif inf == "bouger":
            je = "bouge"
            tu = "bouges"
            il_elle = "bouge"
            nous = "bougeons"
            vous = "bougez"
            ils_elles = "bougent"
        elif inf == "corriger":
            je = "corrige"
            tu = "corriges"
            il_elle = "corrige"
            nous = "corrigeons"
            vous = "corrigez"
            ils_elles = "corrigent"
        elif inf == "voyager":
            je = "voyage"
            tu = "voyages"
            il_elle = "voyage"
            nous = "voyageons"
            vous = "voyagez"
            ils_elles = "voyagent"
    #Regular Verbs
    else:
        root = inf[:-2]
        je = root + "ais"
        tu = root + "ais"
        il_elle = root + "ait"
        nous = root + "ions"
        vous = root + "iez"
        ils_elles = root + "aient"

    return je, tu, il_elle, nous, vous, ils_elles


# Future Proche Verb Tense
def futurprocheTense(inf):
    first = presentTense("aller", "irreg")
    je = first[0] + " " + inf
    tu = first[1] + " " + inf
    il_elle = first[2] + " " + inf
    nous = first[3] + " " + inf
    vous = first[4] + " " + inf
    ils_elles = first[5] + " " + inf

    return je, tu, il_elle, nous, vous, ils_elles


# Futur Simple Tense
def futurTense(inf, type):

    # Irregular verbs:
    if type == "irreg":
        if inf == "avoir":
            je = "aurai"
            tu = "auras"
            il_elle = "aura"
            nous = "aurons"
            vous = "aurez"
            ils_elles = "auront"
        elif inf == "etre":
            je = "serai"
            tu = "seras"
            il_elle = "sera"
            nous = "serons"
            vous = "serez"
            ils_elles = "seront"
        elif inf == "aller":
            je = "irai"
            tu = "iras"
            il_elle = "ira"
            nous = "irons"
            vous = "irez"
            ils_elles = "iront"
        elif inf == "faire":
            je = "ferai"
            tu = "feras"
            il_elle = "fera"
            nous = "ferons"
            vous = "ferez"
            ils_elles = "feront"
    else:
        je = inf + "ai"
        tu = inf + "as"
        il_elle = inf + "a"
        nous = inf + "ons"
        vous = inf + "ez"
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


# Conditionnel Passe Verb Tense
def conditionnelpasseTense(inf, type, subtype, reflexive):

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


# Subjontif Verb Tense
def subjoctifTense(inf, type):

    # Irregular Verbs
    if type == "irreg" or "model":
        if inf == "avoir":
            je = "aie"
            tu = "aies"
            il_elle = "ait"
            nous = "ayons"
            vous = "avez"
            ils_elles = "aient"
        elif inf == "etre":
            je = "sois"
            tu = "sois"
            il_elle = "soit"
            nous = "soyons"
            vous = "soyez"
            ils_elles = "soient"
        elif inf == "aller":
            je = "aille"
            tu = "ailles"
            il_elle = "aille"
            nous = "allions"
            vous = "alliez"
            ils_elles = "aillent"
        elif inf == "faire":
            je = "fasse"
            tu = "fasses"
            il_elle = "fasse"
            nous = "fassions"
            vous = "fassiez"
            ils_elles = "fassent"
        elif inf == "savoir":
            je = "sache"
            tu = "saches"
            il_elle = "sache"
            nous = "sachions"
            vous = "sachiez"
            ils_elles = "sachent"
        elif inf == "pouvoir":
            je = "puisse"
            tu = "puisses"
            il_elle = "puisse"
            nous = "puissions"
            vous = "puissiez"
            ils_elles = "puissent"
        elif inf == "vouloir":
            je = "veuille"
            tu = "veuilles"
            il_elle = "veuille"
            nous = "voulions"
            vous = "vouliez"
            ils_elles = "veuillent"
        elif inf == "valoir":
            je = "vaille"
            tu = "vailles"
            il_elle = "vaille"
            nous = "vailions"
            vous = "vailiez"
            ils_elles = "vaillent"

    elif type == "er" or "re" or "irreg_g":
        root = inf[:-2]
        je = root + "e"
        tu = root + "es"
        il_elle = root + "e"
        nous = root + "ions"
        vous = root + "iez"
        ils_elles = root + "ent"

    elif type == "ir":
        root = inf[:-2]
        je = root + "sse"
        tu = root + "sses"
        il_elle = root + "sse"
        nous = root + "ssions"
        vous = root + "ssiez"
        ils_elles = root + "ssent"


    return je, tu, il_elle, nous, vous, ils_elles


# Passe Compose Verb Tense
def passecomposeTense(inf, type, subtype, reflexive):

    if subtype or reflexive:
        etre = presentTense("etre", "irreg")
        je = etre[0] + pastParticipe(inf, type)
        tu = etre[1] + pastParticipe(inf, type)
        il_elle = etre[2] + pastParticipe(inf, type)
        nous = etre[3] + pastParticipe(inf, type)
        vous = etre[4] + pastParticipe(inf, type)
        ils_elles = etre[5] + pastParticipe(inf, type)
    else:
        avoir = presentTense("avoir", "irreg")
        je = avoir[0] + pastParticipe(inf, type)
        tu = avoir[1] + pastParticipe(inf, type)
        il_elle = avoir[2] + pastParticipe(inf, type)
        nous = avoir[3] + pastParticipe(inf, type)
        vous = avoir[4] + pastParticipe(inf, type)
        ils_elles = avoir[5] + pastParticipe(inf, type)

    return je, tu, il_elle, nous, vous, ils_elles

# Passe Simple Verb Tense
def passesimpleTense(inf, type):
    return


# Moods
# Conditionnel Present Mood
def conditionnelpresentMood(inf):
    je = inf + "ais"
    tu = inf + "ais"
    il_elle = inf + "ait"
    nous = inf + "ions"
    vous = inf + "iez"
    ils_elles = inf + "ont"

    return je, tu, il_elle, nous, vous, ils_elles


# Imperatif Mood
def imperatifMood(inf, type):

    if type == "ir" or "re":
        tu = presentTense(inf,type)[1]
    else:
        tu = presentTense(inf,type)[2]
    nous = presentTense(inf,type)[3]
    vous = presentTense(inf,type)[4]

    return tu, nous, vous


# Participe Present Mood
def participepresentMood(inf, type):

    if type == "oir":
        root = inf[:-2]
        participepresent = root + "yant"
    elif type == "ir":
        root = inf[:-2]
        participepresent = root +"issant"
    elif type == "irreg":
        if inf = "etre":
            participepresent = etant
        elif inf = "avoir":
            participepresent = ayant
        elif inf = "savoir":
            participepresent = sachant
    else:
        root = inf[:-2]
        participepresent = root + "ant"

    return participepresent




print(presentTense("avoir", "irreg"))
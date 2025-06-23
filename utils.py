import Levenshtein

def get_strings_similarity(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return Levenshtein.distance(w1, w2)

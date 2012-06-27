from espeak import Espeak

def init(filepath=None, debug=False):
    espeak = Espeak(filepath, debug)
    return espeak

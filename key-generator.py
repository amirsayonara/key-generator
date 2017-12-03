import random

class Key:
    def __init__(s, format=None, validasi=False):
        s.karakter = [chr(x) for x in range(65,65+26)]+[str(x) for x in range(10)]
        s.format = format;s.validasi = validasi
        if not format: s.no_format()

    def no_format(s):
        while True:
            s.key=''
            for x in range(10): s.key += random.choice(s.karakter)
            if not s.validasi: return
            elif s.validasi_key(): return

    def validasi_key(s):
        return s.key.count(s.key[0])==5

    def __str__(s):
        return s.key

    def __repr__(s):
        return s.key

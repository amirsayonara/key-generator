import random

class Key:
    def __init__(s, format=None, validasi=False):
        s.angka = [str(x) for x in range(10)]
        s.huruf = [chr(x) for x in range(65,65+26)]
        s.format = format;s.validasi = validasi
        if not format: s.no_format()
        elif format: s.with_format()

    def no_format(s):
        while True:
            s.key=''
            for x in range(10): s.key += random.choice(s.karakter+s.huruf)
            if not s.validasi: return
            elif s.validasi_key(): return

    def with_format(s):
        if s.validasi and not s.valid_format():
            s.key='Format salah, pastikan setidaknya mengandung 6 angka jika format key pertama adalah angka, begitu juga dengan huruf'
            return
        while True:
            s.key=''
            for x in s.format.upper():
                if x in s.angka: s.key += random.choice(s.angka)
                elif x in s.huruf: s.key += random.choice(s.huruf)
                else: s.key += x
            if not s.validasi: return
            elif s.validasi_key(): return
        
    def valid_format(s):
        c = 0;tmp=s.format.upper()
        for x in tmp:
            if x in s.huruf and tmp[0] in s.huruf: c+=1
            elif x in s.angka and tmp[0] in s.angka: c+=1
        return c > 5
    
    def validasi_key(s):
        return s.key.count(s.key[0])==5

    def __str__(s):
        return s.key

    def __repr__(s):
        return s.key

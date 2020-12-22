from pykakasi import kakasi
import re
import kana2vowel

f = open('goi.txt')
text = f.readline()

kakasi = kakasi()
# モードの設定：H(Hiragana) to K(Katakana)
kakasi.setMode('H', 'K')
conv = kakasi.getConverter()

while text:
    text = conv.do(text)
    hira_val = kana2vowel.kana2vowel(text)
    text = hira_val.rstrip("\n")
    print(text)
    text = f.readline()
f.close
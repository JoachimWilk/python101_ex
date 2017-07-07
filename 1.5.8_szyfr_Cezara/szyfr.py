#! /usr/bin/env python
# -*- coding: utf-8 -*-

KLUCZ = int(raw_input("Podaj wartość klucza szyfrującego: "))


def szyfruj(txt):
    zaszyfrowany = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowany += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowany += chr(ord(txt[i]) + KLUCZ)
    
    return zaszyfrowany


def deszyfruj(txt):
    odszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for i in range(len(txt)):
        if (ord(txt[i]) - KLUCZM < 97):    
            odszyfrowany += chr(ord(txt[i]) - KLUCZM + 26)
        else:
            odszyfrowany += chr(ord(txt[i]) - KLUCZM)
    return odszyfrowany



u_tekst = raw_input("Podaj ciąg do zaszyfrowania:\n")
print "Ciąg zaszyfrowany:\n", szyfruj(u_tekst)
print "=" * 50
u_tekst = raw_input("Podaj ciąg do deszyfrowania:\n")
print "Ciąg odszyfrowany:\n", deszyfruj(u_tekst)

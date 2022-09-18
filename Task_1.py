#Напишите программу, удаляющую из текста все слова, содержащие ""абв""
from pickletools import string1

string1 = "абвраз абвдва абвтри"
def find_Tekst(string):
    string=string.replace("абв","")
    return string
print(find_Tekst(string1))
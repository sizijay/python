#!/usr/bin/python
# Kasun De Zoysa @ UCSC
import sys
import re


def load(filename):
    fp = open(filename, "r")
    text = fp.read()
    fp.close
    return text

def save(filename,txt):
    fp = open(filename, "w")
    fp.write(txt)
    fp.close

def doCount(letters,txt):
    dict = {}
    for i in range(0, len(letters)):
       s = letters[i]
       dict[s]=len(re.findall(s,txt.lower()))
    return dict

def caesar(text,shift):  
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",  
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
  
    #Create our substitution dictionary  
    dic={}  
    for i in range(0,len(alphabet)):  
        dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]  
    #Convert each letter of plaintext to the corrsponding  
    #encrypted letter in our dictionary creating the cryptext  
    ciphertext=""  
    for l in text.lower():  
        if l in dic:  
            l=dic[l]  
        ciphertext+=l  
  
    return ciphertext  

if len(sys.argv)<3:
   print 'caesar <key> <input> <output>'
   sys.exit(0)

text=load(sys.argv[2])
cipher=caesar(text,int(sys.argv[1]))
save(sys.argv[3],cipher)

c1 = doCount('abcdefghijklmnopqrstuvwxyz',text)
c2 = doCount('abcdefghijklmnopqrstuvwxyz',cipher)
for x in 'abcdefghijklmnopqrstuvwxyz':  
   print '%c\t%2d\t%2d' % (x,c1[x],c2[x])


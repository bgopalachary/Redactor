import pyap as ap
from pyap import parser
from pyap import address
import glob
import re
import nltk
from nltk import word_tokenize,sent_tokenize
from nltk import ne_chunk, pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
def readdata(dat):
    with open(dat) as f:
      line = f.read()
    return line
def dates(data):
    text=data
    DateC=0
    for f in text:
        x = re.sub("[[0-9]*/[0-9]*/[0-9]*]*", "██████", text)
    DateC= re.findall("█+",x)
    return x,DateC
def phone(Y):
    text1=Y
   # PhoneC=0
    for f in text1:
        z= re.sub("[[0-9]*-[0-9]*-[0-9]*]*|[0-9]{10}","██████",text1)
       # PhoneC=PhoneC+1
    return z
def addr(P):
    text3= P
    AddC=0
    Address = ap.parse(text3, country='US')
    #print(Address)
    for i in Address:
         text3 = text3.replace(str(i),"█"*len(str(i)))
         AddC=AddC+1
    return text3,AddC
def name(Q):
    text2=Q
    name=[]
    nameC=0
    for i in sent_tokenize(text2):
        chunked_data= ne_chunk(pos_tag(word_tokenize(text2)))
        #print(chunked_data)
        for chunk in chunked_data:
            if hasattr(chunk, 'label') and chunk.label()=="PERSON":
                nameC=nameC+1
                s=""
                for c in chunk.leaves():
                    s+=c[0]
                name.append(s)
        for k in name:
            text2=text2.replace(str(k),"█"*len(str(k)))
    return text2,nameC
def genders(N):
    gender =['he','she','him','her','his','hers','male','herself','himself','female','man','woman','men','women',
 'He','She','Him','Her','His','Hers','Male','Female','Man','Woman','Men','Women','HE','SHE','HIM','HER','HIS',     
'HERS','MALE','FEMALE','MAN','WOMAN','MEN','WOMEN']
    genC=0
    for i in gender:
        New = re.sub('\\b' +i+ '\\b', '█'* len(i), N)
    for n in N:
        if n in gender:
            genC=genC+1
   # print(genC)
    return New
def concept(Text):
    syns=wn.synsets("kids")
    synonyms=[]
    conC=0
    k=[]
    for i in syns:
        for l in i.lemmas():
            synonyms.append(l.name())
            text4=Text
    lemmatizer = WordNetLemmatizer()
    N= nltk.sent_tokenize(text4)
    S= str(N).split(',')
    M = nltk.word_tokenize(str(S))
    for i in N:
        #print(i)
        for n in synonyms:
            if (i.find(n) != -1):
                conC=conC+1
                text4 = text4.replace(str(i),"█"*len(str(i)))
    print(text4)
    return text4,conC
def output(F):
    final=F
    
    for i in range(5):
        f = open("project1/files/redacted"+str(i)+".txt",'w')
        f.write(final)
        f.close()
        
    import os
    O= os.path.isfile("project1/files/redacted"+str(i)+".txt")
    return O
def stats(y,q,n,f):
    Rdate=y
    Radd=q
    Rname=n
    Rconc=f
    for i in range(5):
        data= "project1/files/redacted"+str(i)+".txt"
        with open(data) as f:
         line = f.read()
         x=re.findall("█+",line)
    print("The number of words redacted in total are:",len(x))
    print("The number of words redacted in dates are:",len(Rdate))
    print("The number of words redacted in address are:",Radd)
    print("The number of words redacted in concepts are:",Rconc)


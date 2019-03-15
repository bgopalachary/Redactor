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
    
    return New
def concept(Text,conc):
    syns=wn.synsets(conc)
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
def output(F,dat):
    k = dat.split('/')
    f = open("project1/files/"+ k[2] +".redacted",'w')
    f.write(F)
    f.close()
    import os
    O= os.path.isfile("project1/files/"+k[2]+".redacted")
    return O
def stats(y,q,n,f,dat,file_name):
    Rdate=y
    Radd=q
    Rname=n
    Rconc=f
    k=dat.split('/')
    data= "project1/files/"+k[2]+".redacted"
    with open(data,'r') as f:
        line = f.read()
        x=re.findall("█+",line)
    print("The number of words redacted in total are:",len(x))
    print("The number of words redacted in dates are:",len(Rdate))
    print("The number of words redacted in address are:",Radd)
    print("The number of words redacted in concepts are:",Rconc)
    







import argparse
import glob
#import main

def mainn(conc, sts):
    for dat in glob.glob('project1/text/*.txt'):
        print(dat)
        data=readdata(dat)
        Y,y=dates(data)
        P=phone(Y)
        Q,q=addr(P)
        N,n=name(Q)
        Text=genders(N)
        F,f=concept(Text, conc)
        Out=output(F,dat)
        stats(y,q,n,f,dat,sts)
        print("Sucess")
    for dat in glob.glob('project1/*.txt'):
        print(dat)
        data=readdata(dat)
        Y,y=dates(data)
        P=phone(Y)
        Q,q=addr(P)
        N,n=name(Q)
        Text=genders(N)
        F,f=concept(Text, conc)
        Out=output(F,dat)
        stats(y,q,n,f,dat,sts)
        print("Sucess")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=glob.glob, required=True, action='append', nargs = '?',
                         help="Please make sure there are .text input files in current or specified folder.")
    parser.add_argument("--names",action='store_true')
    parser.add_argument("--dates",action='store_true')
    parser.add_argument("--addresses",action='store_true')
    parser.add_argument("--gender",action='store_true')
    parser.add_argument("--phones",action='store_true')
    parser.add_argument("--concept", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--stats",type=str)
    args = parser.parse_args()
    mainn(args.concept, args.stats)

import pytest
#from pytest import pytest
import project1
from project1 import redactor
import glob

def test_readdata():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        assert data is not None

def test_dates():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        Y,y=redactor.dates(data)
        assert len(y) > 0

def test_names():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        Y,y=redactor.dates(data)
        P=redactor.phone(Y)
        Q,q=redactor.addr(P)
        N,n=redactor.name(Q)
        assert n >= 0

def test_addr():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        Y,y=redactor.dates(data)
        P=redactor.phone(Y)
        Q,q=redactor.addr(P)
        assert q >= 0

def test_concept():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        Y,y=redactor.dates(data)
        P=redactor.phone(Y)
        Q,q=redactor.addr(P)
        N,n=redactor.name(Q)
        Text=redactor.genders(N)
        F,f=redactor.concept(Text)
        assert f >= 0

def test_output():
    for dat in glob.glob('project1/text/*.txt'):
        data=redactor.readdata(dat)
        Y,y=redactor.dates(data)
        P=redactor.phone(Y)
        Q,q=redactor.addr(P)
        N,n=redactor.name(Q)
        Text=redactor.genders(N)
        F,f=redactor.concept(Text)
        Out=redactor.output(F)
        assert Out== True 




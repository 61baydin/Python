#PYTHON PROGRAMLAMA 401 

#NESNE YONELIMLI PROGRAMLAMA

#Sinif Nedir?

#class VeriBilimci():
#    print("Bu bir siniftir")

#Sinif Ozellikleri (Class attributes)
    
class VeriBilimci():
    bolum=''
    sql='Evet'
    deneyim_yili=0
    bildigi_diller=[]

#Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

#Siniflarin ozelliklerini degistirmek
VeriBilimci.sql="Hayir"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali= VeriBilimci()#ali sinifin ozelliklerini tasir
ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli= VeriBilimci()
veli.sql
veli.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller =["R","PYTHON"]
    bolum=''
    sql='Evet'
    deneyim_yili=0
    #self orneklemleri temsil eder
    def __init__(self):#constructor
        self.bildigi_diller=[]
        self.bolum =''

ali = VeriBilimci()
ali.bildigi_diller
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller

ali.bolum
VeriBilimci.bolum
ali.bolum="Istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum="end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum

#Ornek Metodlari

class VeriBilimci():
    calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum =''
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali=VeriBilimci()
ali.bildigi_diller
ali.bolum

veli=VeriBilimci()
veli.bildigi_diller
veli.bolum

VeriBilimci.dil_ekle
#VeriBilimci.dil_ekle("R") hata verir

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

# Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FistName=""
        self.LastName =""
        self.Address=""

class DataScience(Employees):
    def __init__(self):
      self.Programming=""
      
veribilimci1 = DataScience()      

class Marketing(Employees):
    def __init__(self):
      self.StoryTelling=""

mar1= Marketing()

class Employee_yeni():
    def __init__(self,FistName,LastName,Address):
        self.FistName=FistName
        self.LastName =LastName
        self.Address=Address

ali = Employee_yeni("a","b","c")
ali.FistName

#Python'da Fonksiyonel Programlama
# =============================================================================
# 
# Fonksiyonlar dilin bastacidir.
# (birinci sinif nesnelerdir)
# Yan etkisiz fonksiyonlar (stateless,girdi-cikti)
# yuksek seviye fonksiyonlar
# vektorel operasyonlar
# =============================================================================

#Yan Etkisiz Fonksiyonlar(Pure Functions)

#Ornek1:Bagimsizlik

A = 9

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

impure_sum(6) #yan etki var
pure_sum(3,4) #her zaman ayni sonuc


#Ornek2:Olumcul yan etkiler
#OOP
class LineCounter:
    def __init__(self , filename):
        self.file = open(filename, 'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)
    
lc=LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]
def count(lines):
    return len(lines)

example_lines=read('deneme.txt')
lines_count=count(example_lines)
lines_count

#Isimsiz Foksiyonlar (Anonymus Functions)

def old_sum(a,b):
    return a+b

old_sum(4,5)

new_sum= lambda a,b : a+b
new_sum(4,5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste,key=lambda x:x[1])

#Vektorel Operasyonlar(vectorel Operations)
#OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0,len(a))

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
    print(i)
ab

#FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b

#map & filter & reduce

liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

#map verilen nesnenin üzerinde 
#tanimlanacak fonk. calistirma imkani verir.
list(map(lambda x: x+10,liste))

#filter

liste=[1,2,3,4,5,6,7,8,9,10]

#filter  fonk: sartı saglayanları
# filtreler ve geri dondurur .
list(filter(lambda x:x%2==0,liste)) 

#reduce

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a+b, liste)

#Modul Olusturmak (kutuphane,paket)
import HesapModulu

HesapModulu.yeni_maas(1000)

import HesapModulu as hm

hm.yeni_maas(3000)

from HesapModulu import yeni_maas
yeni_maas(4000)

import HesapModulu as hm
hm.maaslar

#Hatalar / istisnalar (exceptions)
# try - except yapisi

#ZeroDivisionError hatasi
a=10
b=0
a/b

try:
    print(a/b)
except ZeroDivisionError :
    print("Payda da sifir olmaz")

#TypeError hatasi
a=10
b="2"
a/b

try:
    print(a/b)
except TypeError:
    print("Sayi ve String problemi")

#Sorular
    
A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]


for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))    

A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))

def islem(x,y,z):
    if y == 0:
        print("hatali islem")
    else:
        return x/y*z

islem()
islem(1,0,2)

list(map(lambda x: x*1, [2,7,4]))

import numpy as np
a = np.array([1,1,1])
b = np.array([2])

a+b

list(filter(lambda x: len(x) > 8, ["pazartesi","sali","carsamba","persembe","cuma"]))

list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))

from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

list(map(lambda x: x.capitalize(), ["abc","bcd","cde"]))

from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])


A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))

class BolumSorulari():
    fonksiyonlar = []
    OOP = []

BolumSorulari.OOP

liste = [1,2,3,4]
A = []

for i in liste:
    A.append(i**2)

print(A)

list(map(lambda x: x**2, liste))

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

a = [1,2,3]
list(map(lambda x: x*2, a))



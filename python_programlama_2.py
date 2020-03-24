#VERI YAPILARI

#listeler
#kapsayici,sirali,degistirilebilir.
#[]
#list()

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90,notlar]
len(list_genis)

type(list_genis[3])

tum_liste = [liste,list_genis]
#del tum_liste

#listeler - Eleman Islemleri

liste = [10,20,30,40,50]
liste[0]
liste[1]

liste[0:2]
liste[:2]#üsteki ile ayni
liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste
yeni_liste[2]
yeni_liste[0:2]
yeni_liste[2][1]


#Listeler - Eleman Degistirme

liste = ["ali","veli","berkcan","ayse"]
liste

liste[1] ="velinin_babasi"
liste
liste[1]="veli"

liste[0:3] ="alinin_babasi","velinin_babasi","berkcanin_babasi"
liste
liste = ["ali","veli","berkcan","ayse"]
liste =liste + ["kemal"]
liste
#del liste[2]
liste

#Liste - Liste Metodları

liste=["ali","veli","isik"]
dir(liste) #liste metodlarını gösterir
liste

#append - sona veriekleme-kalicidir
liste.append("berkcan") 
liste
#remove listeden eleman silme
liste.remove("berkcan")
liste

#insert - eleman ekleme -istedigin indekse 

liste.insert(0,"ayse")
liste
liste.insert(2,"mehmet")
liste
liste.insert(5,"berk")
liste
len(liste)
liste.insert(len(liste),"beren")
liste

#pop - indekse gore eleman silme
liste.pop(0)
liste
liste.pop(1)
liste

#count

liste = ["ali","veli","isik","ali","veli"]
liste.count("ali")
liste.count("isik")
liste.count("veli")

#copy - listeninin yedegini al

liste_yedek = liste.copy()

#extend - liste birlestirme

liste.extend(["a","b",10])
liste

#indeks() - hangi index te ogrenme

liste.index("ali")

#reverse() - listeyi ters cevirme

liste.reverse()
liste

#sort() - kucukten buyuge siralama yapma

liste= [10,40,5,90]
liste.sort()
liste

#clear - listenin icini bosaltma

liste.clear()
liste

#Veri Yapilari - Tuple (demet) Olusturma

#Tuple: kapsayici,sirali,degistirilemezler.
#degismesini istemedigin liste yerine kullanilir
t = ("ali","veli",1,2,3.2,[1,2,3,4])

t = "ali","veli",1,2,3.2,[1,2,3,4]

#tuple()

t= ("eleman",)
type(t) #tek elemanken sonuna virgul atilmali

#Tuple Elaman Islemleri

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t

t[1]
t[0:3]
# t[2] = 99 hata verir tuple degistirlemez

#Veri Yapıları - Dictionary (Sözlük) Olusturma
#kapsayici,sirasiz,degisirilebilirdir
#listelerdeki gibi indeksleme yok.

sozluk = {"REG" : 10,
          "LOJ" : "Logistik Regresyon",
          "CART" : "Classification and Reg"}
sozluk
len(sozluk) # 3 eleman
sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" :["SSE",30] }
sozluk

#Sozluk Elemanlari Islemleri
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Logistik Regresyon",
          "CART" : "Classification and Reg"}

# sozluk[0] hata verir sozluk sirasizdir
sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : {"RMSE":10,
                   "MSE":20,
                   "SSE":30},
          "LOJ" : {"RMSE":10,
                   "MSE":20,
                   "SSE":30},
          "CART" : {"RMSE":10,
                   "MSE":20,
                   "SSE":30}}
sozluk
sozluk["REG"]["SSE"]

#Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Logistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk
sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

l = [1]
l
#sozluk[l]="yeni bir sey"
#hata verir sabit veri yapisi olmali str veya int


t= ("tuple",)

sozluk[t] ="yeni bir sey"
sozluk

#Veri Yapilari - Setler (kümeler)
#sirasizdir,degerleri essizdir,degistirilebilir,farkli tipleri barindirabilir.

#Set Olusturma

s = set()
s

l= [1,"a","ali",123]
s = set(l)
s

t=("a","ali")
s= set(t)
s

ali="ali_ata_bak"
type(ali)
s=set(ali)
s

l=["ali","ata","bak","ali","git","git"]
l
s = set(l)
s

len(s)
l[0]
#s[0] hata verir setler sirasiz

#Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]
s= set(l)
s
dir(s)
s.add("ile")
s
s.add("gelecege_git")
s

s.add("ile")#var olan deger tekrar eklenmez.
s 
s.remove("ali")# set te ali yok hata verir.
s
s.discard("ali")#silmek icin bulamazsa hata vermez
s

#Setler - Klasik Kume Islemleri

# =============================================================================
# difference() ile iki küme farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kume birlesimi
# symetric_difference() ikisinde de olmayanlari
# =============================================================================

#diffrence

set1= set([1,3,5])
set2= set([1,2,3])
set1.difference(set2)
set2.difference(set1)
set1.symmetric_difference(set2)
set1-set2
set2-set1

#intersection & union

set1.intersection(set2)
set2.intersection(set1)
kesisim= set1&set2
kesisim
birlesim=set1.union(set2)
birlesim
set1.intersection_update(set2)
set1 #set1 artik kesisim kumesi oldu.

#Set Sorgu Islemleri

set1=set([7,8,9])
set2=set([5,6,7,8,9,10])

#iki kumenin kesiminin bos olup olmadigi
set1.isdisjoint(set2)
#set1 set2'nin alt kumesi mi
set1.issubset(set2)
#bir kume diger kumeyi kapsiyor mu
set2.issuperset(set1)

# =============================================================================
# SORULAR
# 
# =============================================================================
liste = [1,1,2,3,4,5,1,2,1]
liste.count(1)

liste = [10,20,30,40]
liste.pop(1)
liste

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

liste = [10,10,20,40]
liste.clear()
liste

liste = ["a","b","c"]
liste.reverse()
print(liste)

set1 = set([5,7,9])
set2 = set([5,6,7])
set2.difference(set1)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

sozluk = {"REG" : {"RMSE": 10,
"MSE": 11,
"SSE": 12},
 
"LOJ" : {"RMSE": 111,
"MSE": 2222,
"SSE": 333},
 
"CART" : {"RMSE": 99,
"MSE": 00,
"SSE": 66}}

sozluk["CART"]["SSE"]

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.difference(set2)

sozluk = {"reg" : "regresyon modeli",
"loj" : "lojistik regresyon",
"cart" : "classification and regression trees"}


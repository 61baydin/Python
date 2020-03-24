#PYTHON PROGRAMLAMA 301 
#FONKSİYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI


# '?' fonksiyon dokumantasyonu gosterir
#?print()
#sep degerlerin arasina bir string yerlestirir.
print("a","b",sep="_")

len("a")
print()

#Fonksiyon nasıl yazılır.
4*4 #carpma
2**3 #ust alma

def kare_al(x):
    print(x**2)

kare_al(3)

def kare_al(x):
    print("Girilen Sayini: " +str(x)+" Karesi:"+ str(x**2))
kare_al(3)

#Iki argumanli Fonksiyon Tanimlamak

def carpma_yap(x,y):
    print(x*y)

carpma_yap(2,3)

#On Tanimli Argumanlar
#default atanmis

def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(3)

#Argumanlarin Siralamasi

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(2,3)

#Ne Zaman Fonksiyon Yazilir?

#isi,nem,sarj

(40+25)/90

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

direk_hesap(30,40,70)

#Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

cikti= direk_hesap(25,40,70)
cikti 
print(cikti) 

def direk_hesap(isi,nem,sarj):
    return #fonksiyon burda cikar
    (isi+nem)/sarj

cikti= direk_hesap(25,40,70)#cikti vermez

#Local ve Global Degiskenleri

x=10 #Global degiskenler
y=20

def carpma_yap(x,y):
    return x*y #Local degiskenler

carpma_yap(2,3)

#Local Etki Alanindan Global Alanini Degistirmek

x=[]
def eleman_ekle(y):
    x.append(y) #blok icinde x tanimli olmadiginden globaldekini kullanilir
    print(str(y)+" ifadesi eklendi")

eleman_ekle("ali")
eleman_ekle("veli")
x

# KARAR 6 KONTROL YAPILARI

#True-False sorgulamaları

sinir=5000

sinir==5000
sinir==4000

#if
sinir=50000
gelir=60000
gelir1=60000
gelir2=50000
gelir3=35000

if gelir< sinir:
    print("Gelir sinirdan kucuk")

#else
    
if gelir> sinir:
    print("Gelir sinirdan buyuk")
else:
     print("Gelir sinirdan kucuk")

if gelir== sinir:
    print("Gelir sinira esit")
else:
     print("Gelir sinira esit degil")

#elif
if gelir1> sinir:
    print("Tebrikler,hediye kazandiniz")
elif gelir1 <sinir:
    print("uyari!")
else:
     print("Takibe devam")

if gelir2> sinir:
    print("Tebrikler,hediye kazandiniz")
elif gelir2 <sinir:
    print("uyari!")
else:
     print("Takibe devam")    

#mini uygulama

sinir=50000
magaza_adi=input("Magaza Adi Nedir?")
gelir=int(input("Gelirinizi Giriniz:"))

if gelir>sinir:
    print("Tebrikler:"+magaza_adi+" promosyon kazandiniz!")
elif gelir<sinir:
    print("uyari! Cok dusuk gelir"+str(gelir))
else:
    print("Takibe devam")

# DONGULER - for

ogrenci=["ali","veli","isik","berk"]    
ogrenci[0]    

for i in ogrenci:
    print(i)

maaslar=[1000,2000,3000,4000,5000]

#dongu ve fonksiyonlar birlikte kullanmak

def kare_al(x):
    print(x**2)
kare_al(2)

for i in maaslar:
    print(i)

#maaslara yuzde 20 zam yapilacak
def yeni_maas(x):
    print(x*20/100+x)

for i in maaslar:
    yeni_maas(i)

#mini uygulama
#if,for ve fonksiyonlari birlikte kullanma

maaslar=[1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)
def maas_alt(x):
    print(x*20/100+x)

for i in maaslar:
    if i >=3000:
        maas_ust(i)
    else:
        maas_alt(i)

#break & contiune
maaslar=[8000,5000,1000,3000,7000,1000]

dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i==3000:
        print("kesildi")
        break #isteilen degere geldikten sonra kesme
    print(i)
  
for i in maaslar:
    if i==3000:
        print("kesildi")
        continue # degeri atlamak icin kullanilir
    print(i)
 
#while
sayi=1
while sayi<10:
    sayi +=1
    print(sayi)
# =============================================================================
# 
# SORULAR 
#     
# =============================================================================
def islem(x):
    if (x<0):
        return "NO"
    else:
        x*5
 
islem(2)
    
    
A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())
    
def harf_say(x):
    len(x)
 
harf_say("Merhaba!")

def islem(x, y):
    print(x - y)

islem(3)

urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)

sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        continue
    print(i)

liste = ["a","b","c"]
liste.reverse()
print(liste)

def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")


sayilar = [10,20,31]
 
for i in sayilar:
    if i > 20:
        print(i/2)

a = [2,4,6,8]
for i in a:
    print(i**2)

if [1,2,3,4][1] == 2:
    print("YES".lower())
else:
    print("NO")

def islem(x, y):
    print(x + y)
 
islem(1,9)

def mesaj():
    print("Merhaba!")    
    
mesaj()  








#PYTHON PROGRAMLAMA 101 
#SAYILAR VE STRİNGLERE GİRİŞ
9
9.2
9+9
9*9
print('HELLO')
"HELLO"
type(9.2)
type("hello")
#stringlere bakalım

123
type(123)
"123"
type("123")
"a" +"b"
"a"*3

#string metotları (fonksiyon) -len() 
gel_yaz = "gelecegi_yazanlar"
#del mvk
a = 9
b = 10
a*b
len(gel_yaz)

#string metotları- upper() & lower()

B= gel_yaz.upper()
gel_yaz.lower()
#kontrol true folse döner
B.islower() 

#string metotları - replace() - yerine kullanma
gel_yaz = "gelecegi_yazanlar"
#replace atama yapmaz
gel_yaz.replace("e","a")
gel_yaz.replace("a","i")

#string metotları - strip() 15/20
#kırpma işlemini boşluklara göre bak
gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()
gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l") #boşluk yerine

#METODLARA GENEL BAKIS 16/20

gel_yaz = "gelecegi_yazanlar"
dir(gel_yaz) #veri tipinin üzerine uygulanabilecek olan metotlara gider

gel_yaz.capitalize()
gel_yaz.title()

#SUBSTRINGLER 17/20
gel_yaz = "gelecegi_yazanlar"
# [] seçim işlemi yapilcak anlasilir
gel_yaz[1]

gel_yaz[0:3] # 0 dahil 3 dahil değil arasi
gel_yaz[3:7]

#DEGISKENLER 18/20

a = 9
b= "ali_uzaya_git"
c = a*2
a/c
a*c
a*5
type(100)
type(100.2)
type(1+2j)
a=100.2

#TYPE_DONUSUMLERI 19/20

#input() kullanıcıdan bilgi almak için kullanılır
toplama_bir = input()
toplama_iki = input()
type(toplama_bir)
toplama_bir+toplama_iki
int(toplama_bir)+int(toplama_iki)
int(11.0)
12
float(12)
type(str(12))

# print() kullanimi

print("HELLO AI ERA")

print("gelecegi","yazanlar", sep = "_")
print()
#?print

#denemeler
"_Python_".strip("_")
ifade = "1012340"
ifade = ifade+"1"
ifade.strip("1")

ifade="Merhaba! "
ifade.strip("")


import random
secim_sayisi=0
dogru_sayisi=0
oran=0

A="A"
B="B"
C="C"

kapilar=["A","B","C"]
sayac=1000

print("\n10 defa monty hall oyunu oynatılacak")
while sayac!=0:
    sayac-=1
    araba=random.choice(kapilar)
    secilecek_random_araba=random.choice(kapilar)
    print("seçilen random kapı :%r" % secilecek_random_araba)
    secim_sayisi+=1
    if secilecek_random_araba==araba:
        kalan=list(set(kapilar)-set(araba))
        acik_kapi=random.choice(list(set(kapilar)-set(random.choice(kalan))))
        alternatif_kapi=random.choice(list(set(kapilar)-set(acik_kapi)-set(araba)))
    else:
        acik_kapi=random.choice(list(set(kapilar)-set(secilecek_random_araba)-set(araba)))
        alternatif_kapi= random.choice(list(set(kapilar)-set(acik_kapi)-set(secilecek_random_araba)))
    print("sunucu şu kapiyi açıyor: %r" % acik_kapi)
    print("kapı değiştirilecek")
    print("Seçmiş olduğunuz yeni kapı : %r " % alternatif_kapi)
    if alternatif_kapi == araba:
        dogru_sayisi += 1
        print("tebrikler kazandınız...")

    else:
        print("kaybettiniz...")
    oran = dogru_sayisi / secim_sayisi
    print("oynanan oyun sayısı: %r" % secim_sayisi)
    print("kazandığın oyun sayısı: %r" % dogru_sayisi)
    print("kazanma oranı: %r" % oran)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


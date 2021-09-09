#MUHAMMET ENES AY 
import time
urunler = dict()
keyler=[]         # unique barkod numaralari olusturmak için kontrol saglıyor

def ana():
    print(
    """***DEPO STOK TAKİP OTOMASYONU***
1)ÜRÜN EKLE \n2)ÜRÜN GÜNCELLE \n3)ÜRÜN ARA \n4)ÜRÜN SİL \n5)KDV'Lİ FİYAT HESAPLA \n6)ÜRÜN LİSTELE \n7)SATIŞ YAP \n8)STOK KONTROL\n9)ÇIKIŞ""")
    sec = int(input("Lütfen seçiminizi giriniz:"))
    if sec == 1:
        urun_ekle()
    if sec == 2:
        urun_guncelle()
    if sec == 3:
        urun_ara()
    if sec == 4:
        urun_sil()
    if sec == 5:
        kdv_hesapla()
    if sec == 6:
        urun_listele()
    if sec==7:
        satisyap()
    if sec==8:
        stok_kontrol()
    return sec
def urun_ekle():
        while True:
            try:
                sayi = int(input("Lütfen eklenecek ürün sayısını giriniz :"))
                def dosyaya_yaz():
                    with open("19010011077.txt", "a", encoding="utf-8") as dosya:
                        for a, d in urunler.items():
                            dosya.write('%s:%s\n' % (a, d))
                def bilgi_al():
                    for i in range(1, int(sayi) + 1):
                        liste = []
                        while True:
                            with open("19010011077.txt", "r", encoding="utf=8") as dosya1:
                                kontrol = dosya1.readlines()
                            kontrol_tf = None
                            barkod = int(input("{}. ürünün barkod numarasını giriniz :".format(i)))
                            for a in kontrol:  # Aynı barkod numarasının girilmesini engeller.
                                if str(barkod) == a.split(":")[0]:
                                    kontrol_tf = True
                                else:
                                    continue
                            if kontrol_tf == True:
                                print("Bu barkod numarasını kullanan ürün halihazırda bulunuyor.Tekrar deneyiniz.")
                            elif barkod in keyler:
                                print("Bu barkod numarasını kullanan ürün halihazırda bulunuyor.Tekrar deneyiniz.")
                            else:
                                break
                        ad = input("{}. ürünün adını giriniz :".format(i))
                        fiyat = int(input("{}. ürünün fiyatını giriniz :".format(i)))
                        adet = int(input("{}. ürünün adetini giriniz :".format(i)))
                        liste.append(ad.upper())
                        liste.append(fiyat)
                        liste.append(adet)
                        urunler[barkod] = liste
                        keyler.append(barkod)
                bilgi_al()    #İNNER FONKSİYON
                dosyaya_yaz()  #İNNER FONKSİYON
                urunler.clear()
                print("Ürün(ler) başarıyla eklendi.")
                while True:
                    ekle_secim = input("Tekrar ürün eklemek içim (D) Menüye dönmek için (M) :")
                    if ekle_secim.upper() != "D" and ekle_secim.upper() != "M":
                        print("HATA! lütfen geçerli bir seçim yapınız.")
                    else:
                        break
                if ekle_secim.upper() == "D":
                    continue
                elif ekle_secim.upper() == "M":
                    break
            except ValueError:
                print("HATA! Sayı değeri haricinde değer girilemez!")
                continue
def urun_ara():
    while True:
        barkod_ara=input("Lütfen aranacak ürünün barkod numarasını giriniz : ")
        with open("19010011077.txt", "r", encoding="utf=8") as dosya2:
            oku_urun = dosya2.readlines()
        check=None
        for a in oku_urun:
            if barkod_ara == a.split(":")[0] :
                check=True
                print("ÜRÜN ADI : "+ a.split("'")[1])  #urun adına ulasmamızı saglayan koordınat
                print("ÜRÜN FİYATI :"+ a.split(",")[1] +"TL")
                print("ÜRÜN ADEDİ :"+ a.split(",")[2].replace("]",""))
        if check!=True:
            print("Bu barkod numarası ile ürün bulunmuyor!")
        devam=input("Tekrar sorgulamak için (D) menüye dönmek için (M):")
        if devam.upper()=="D":
            continue
        elif devam.upper()=="M":
            break
def urun_sil():
    while True:
        barkod_sil=input("Lütfen silmek istediğiniz ürünün barkod numarasını giriniz : ")
        with open("19010011077.txt", "r", encoding="utf=8") as dosya3:
            sil_urun = dosya3.readlines()
        check2=None
        secim_sil=None
        for sil in sil_urun:
            if barkod_sil == sil.split(":")[0] :
                check2=True
                print("ÜRÜN ADI : "+ sil.split("'")[1])  #urun adına ulasmamızı saglayan koordınat
                print("ÜRÜN FİYATI :"+ sil.split(",")[1] +"TL")
                print("ÜRÜN ADEDİ :"+ sil.split(",")[2].replace("]",""))
                secim_sil=input("Seçili ürünü silmek istediğinize emin misiniz? (E)(H) : ")
        if str(secim_sil).upper()=="E":
            with open("19010011077.txt","w",encoding="utf=8") as dosya4:
                for sil in sil_urun:
                    if barkod_sil != sil.split(":")[0]:
                        dosya4.write(sil)
            if not keyler:    #ilk açılışta silme yaparken keyler listesi boş olacagından,hata olmasını engeller.
                pass
            else:
                if int(barkod_sil) in keyler:
                    keyler.remove(int(barkod_sil))       #ürün silindiginde tekrar eklenirse barkod hatası vermesini engeller
        if check2!=True:
            print("Bu barkod numarası ile ürün bulunmuyor!")
        else:
            if str(secim_sil).upper() == "E":
                print("Ürün başarıyla silindi.")
        devams=input("Tekrar ürün silmek için (S) menüye dönmek için (M):")
        if devams.upper()=="S":
            pass
        elif devams.upper()=="M":
            break
def urun_guncelle():
    while True:
        urunler_gnc=dict()
        liste2=[]
        barkod_guncelle = input("Lütfen güncellemek istediğiniz ürünün barkod numarasını giriniz : ")
        with open("19010011077.txt", "r", encoding="utf=8") as dosya5:
            guncelle_urun = dosya5.readlines()
        devam3=None
        check3 = None
        secim_guncelle = None
        for gnc in guncelle_urun:
            if barkod_guncelle == gnc.split(":")[0]:
                check3 = True
                print("ÜRÜN ADI : " + gnc.split("'")[1])  # urun adına ulasmamızı saglayan koordınat
                print("ÜRÜN FİYATI :" + gnc.split(",")[1] + "TL")
                print("ÜRÜN ADEDİ :" + gnc.split(",")[2].replace("]", ""))
                secim_guncelle = input("Seçili ürünü güncellemek istediğinize emin misiniz? (E)(H) : ")
        if str(secim_guncelle).upper()=="H":
            break
        if check3!=True:
            print("Bu barkod numarası ile ürün bulunmuyor!")
            devam3=input("Tekrar sorgulamak için (D) menüye dönmek için (M):")
        if str(devam3).upper()=="D":
            continue
        elif str(devam3).upper()=="M":
            break
        if secim_guncelle.upper()=="E":
            gnc_ad = input("Yeni ürün adını giriniz : ")
            gnc_fiyat = int(input("Yeni ürün fiyatını giriniz : "))
            gnc_adet = int(input("Yeni ürün adedini giriniz : "))
            liste2.append(gnc_ad.upper())
            liste2.append(gnc_fiyat)
            liste2.append(gnc_adet)
            urunler_gnc[barkod_guncelle] = liste2
            print("GUNCELLENİYOR", end="")
            for i in range(3):
                time.sleep(0.4)
                print(".", end="")
            with open("19010011077.txt","w",encoding="utf=8") as dosya6:
                for sil in guncelle_urun:
                    if barkod_guncelle != sil.split(":")[0]:
                        dosya6.write(sil)
            with open("19010011077.txt","a",encoding="utf=8") as dosya7:
                for a, d in urunler_gnc.items():
                    dosya7.write('%s:%s\n' % (a, d))
            print("Ürün güncellendi")
            break
def urun_listele():
        with open("19010011077.txt", "r", encoding="utf=8") as dosya8:
            listele_urun = dosya8.readlines()
        i=0
        for l in listele_urun:
            i=i+1
            print(str(i)+")"+" ÜRÜN BARKOD NO : "+l.split(":")[0]+"\t"+"|",end="")
            print(" ÜRÜN ADI : " + l.split("'")[1] + "\t" + "|", end = "")
            print(" ÜRÜN FİYATI :" + l.split(",")[1] + "TL"+"\t"+"|",end="")
            print(" ÜRÜN ADEDİ :" + l.split(",")[2].replace("]", ""),end="")
            time.sleep(0.5)
        input("Menüye dönmek için bir tuşa basınız : ")
def kdv_hesapla():
    while True:
        try:
            barkod_kdv = input("Lütfen kdv dahil fiyatı hesaplanacak ürünün barkod numarasını giriniz : ")
            with open("19010011077.txt", "r", encoding="utf=8") as dosya9:
                kdv_urun = dosya9.readlines()
            kontrol = None
            for kdv in kdv_urun:
                if barkod_kdv == kdv.split(":")[0]:
                    kontrol = True
                    print("ÜRÜN ADI : " + kdv.split("'")[1])
                    print("ÜRÜN FİYATI :" + kdv.split(",")[1] + "TL")
                    print("ÜRÜN ADEDİ :" + kdv.split(",")[2].replace("]", ""))
                    oran = int(input("Lütfen seçili ürün için güncel kdv oranını giriniz % :"))
                    kdvli = (int(kdv.split(",")[1]) * (oran / 100) + int(kdv.split(",")[1]))
                    print(kdv.split("'")[1] + " adlı ürün için" + " kdv dahil fiyat :" + str(kdvli) + "TL")
            if kontrol != True:
                print("Bu barkod numarası ile ürün bulunmuyor!")
            devam_kdv = input("Tekrar hesaplamak için (D) menüye dönmek için (M):")
            if devam_kdv.upper() == "D":
                continue
            elif devam_kdv.upper() == "M":
                break
        except ValueError:
            print("HATA! girdiğiniz alan ile girilen değer uyumsuz.(İşlem tekrar başlatıldı)")
def satisyap():
    def sat_urun(barkod_sat):
        fiyat=None
        adet=None
        ad=None
        with open("19010011077.txt", "r", encoding="utf=8") as dosya_sat2:
            oku2_urun = dosya_sat2.readlines()
        for sat2 in oku2_urun:
            if barkod_sat == sat2.split(":")[0]:
                ad=sat2.split("'")[1]
                fiyat=sat2.split(",")[1]
                adet=sat2.split(",")[2].replace("]", "")
        urunler_sat = dict()
        liste_sat = []
        sat_fiyat = int(input("Lütfen satış fiyatını giriniz : "))
        while True:
            sat_adet = int(input("Satış adedini giriniz : "))
            if int(adet)<(sat_adet):
                print("Stoktaki adeti aştınız lütfen tekrar deneyiniz.")
                continue
            else:
                break
        liste_sat.append(ad)
        liste_sat.append(int(fiyat))
        liste_sat.append(int(adet)-(sat_adet))
        urunler_sat[barkod_sat] = liste_sat
        with open("19010011077.txt", "w", encoding="utf=8") as dosya_yaz:
            for sat in oku2_urun:
                if barkod_sat != sat.split(":")[0]:
                    dosya_yaz.write(sat)
        with open("19010011077.txt", "a", encoding="utf=8") as dosya_ekle:
            for b, c in urunler_sat.items():
                dosya_ekle.write('%s:%s\n' % (b, c))
        print("Ürün satıldı.")
        print("Net kar : {} TL".format((sat_fiyat*sat_adet)-(int(fiyat)*sat_adet)))
        devam_sat2 = input("Tekrar satış yapmak için (D) menüye dönmek için (M):")
        a="devam"
        b="menü"
        if devam_sat2.upper()=="D":
            return a
        if devam_sat2.upper()=="M":
            return b
    while True:
        barkod_sat = input("Lütfen satılacak ürünün barkod numarasını giriniz : ")
        with open("19010011077.txt", "r", encoding="utf=8") as dosya_oku:
            oku_urun = dosya_oku.readlines()
        kontrol_sat = None
        secim_sat=None
        devam_sat=None
        for sat in oku_urun:
            if barkod_sat == sat.split(":")[0]:
                kontrol_sat = True
                print("ÜRÜN ADI : " + sat.split("'")[1])  # urun adına ulasmamızı saglayan koordınat
                print("ÜRÜN FİYATI :" + sat.split(",")[1] + "TL")
                print("ÜRÜN ADEDİ :" + sat.split(",")[2].replace("]", ""))
                secim_sat = input("Seçili ürünü satmak istediğinize emin misiniz? (E)(H) : ")
        if kontrol_sat !=True:
            print("Bu barkod numarası ile ürün bulunmuyor!")
            devam_sat = input("Tekrar denemek için (D) menüye dönmek için (M):")
        if str(devam_sat).upper()=="D":
            continue
        elif str(devam_sat).upper()=="M":
            break
        if str(secim_sat).upper() == "H":
            break
        if secim_sat.upper()=="E":
            secim=sat_urun(barkod_sat)
            if secim=="devam":
                continue
            if secim=="menü":
                break
def stok_kontrol():
    with open("19010011077.txt", "r", encoding="utf=8") as dosya_stok:
        stok_urun = dosya_stok.readlines()
    i = 0
    for stk in stok_urun:
        if int(stk.split(",")[2].replace("]", ""))<5:
            i = i + 1
            print(str(i) + ")" + " ÜRÜN BARKOD NO : " + stk.split(":")[0] + "\t" + "|", end="")
            print(" ÜRÜN ADI : " + stk.split("'")[1] + "\t" + "|", end="")
            print(" ÜRÜN FİYATI :" + stk.split(",")[1] + "TL" + "\t" + "|", end="")
            print(" ÜRÜN ADEDİ :" + stk.split(",")[2].replace("]", ""), end="")
            time.sleep(0.5)
    input("Menüye dönmek için bir tuşa basınız : ")

while True:
    try:
        secim = ana()
        if secim == 9:
            break
        if secim > 9 or secim < 1:
            print("HATA! Lütfen seçim sınırlarına uygun bir sayı giriniz!")
            continue
    except ValueError:
        print("HATA! sayısal değer girilmelidir.")
print("OTOMASYON SONLANDIRILIYOR",end="")
for i in range(3):
    print(".",end="")
    time.sleep(0.2)




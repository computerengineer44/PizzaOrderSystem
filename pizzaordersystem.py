from datetime import datetime  # siparis zamanını verilere eklemek için kitaplık içi aktarıldı
import csv  # siparişlerin kaydı için kitaplık içi aktarıldı


# menu.txt dosyasını cagirma
def menu_sec():
    with open('Menu.txt', 'r') as f:
        print(f.read())


# Menu dosyasindaki secenekleri yazdir
menu = open("Menu.txt", "w")
menu.write(
    "* Lütfen Bir Pizza Tabanı Seçiniz:\n 1: Klasik\n 2: Margarita\n 3: TürkPizza\n 4: Sade Pizza\n\n* Ve Seçeceğiniz Sos:\n 11: Zeytin\n 12: Mantarlar\n 13: Keçi Peyniri\n 14: Et\n 15: Soğan\n 16: Mısır\n\n* Teşekkür ederiz!\"\n")
menu.close()


########################################################################################################################

# Pizzaların fiyat ve açıklamaları için superclass-subclasslar olusturma.
class Pizza:
    def __init__(self, fiyat, aciklama):
        self.fiyat = fiyat
        self.aciklama = aciklama

    def get_cost(self):
        return self.fiyat

    def get_description(self):
        return self.aciklama


class Klasik(Pizza):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Margarita(Pizza):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Turk_Pizza(Pizza):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Sade_Pizza(Pizza):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


########################################################################################################################

# Sosların fiyat ve aciklamaları icin superclass-subclasslar olusturma.
class Sos:
    def __init__(self, fiyat, aciklama):
        self.fiyat = fiyat
        self.aciklama = aciklama

    def get_cost(self):
        return self.fiyat

    def get_description(self):
        return self.aciklama


class Zeytin(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Mantarlar(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Keci_peyniri(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Et(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Sogan(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)


class Misir(Sos):
    def __init__(self, fiyat, aciklama):
        super().__init__(fiyat, aciklama)

########################################################################################################################

class Decorator:
    def __init__(self, pizza: Pizza, sos: Sos):
        self.pizza = pizza
        self.sos = sos

    def get_cost(self):
        return self.pizza.get_cost() + self.sos.get_cost()

    def get_description(self):
        return self.pizza.get_description() + self.sos.get_description()


########################################################################################################################
# pizza ve sosların içerikleri

Klasik_pizza = Klasik(75, "Sosis ve salam icerir")
Margarita_pizza = Margarita(80, "Domates, mozzarella peyniri, fesleğen ve zeytinyağı icermekte")
Turkiye_pizza = Turk_Pizza(95, "Sucuk ve pastirma bulunmakta")
SadePizza = Sade_Pizza(70, "Sadece domates sosu ve peynir bulunmakta")

zeytinsos = Zeytin(4, "  ekstra zeytin ezmeli içerir")
mantarsos = Mantarlar(6, "  ekstra 2 cesit mantarli içerir")
kecisos = Keci_peyniri(5, "  ekstra keci peynirli içerir")
etsos = Et(9, "  ekstra kavurmali içerir")
sogansos = Sogan(4, "  ekstra karamelize soganli içerir")
misirsos = Misir(4, "  ekstra sut misirli içerir")


########################################################################################################################

# pizza ve sos seçimi kısmı

def pizza_secimi(Pizza_cesidi):
    if Pizza_cesidi == "Klasik" or Pizza_cesidi == "1":
        return Klasik_pizza

    elif Pizza_cesidi == "Margarita" or Pizza_cesidi == "2":
        return Margarita_pizza

    elif Pizza_cesidi == "TürkPizza" or Pizza_cesidi == "3":
        return Turkiye_pizza

    elif Pizza_cesidi == "Sade Pizza" or Pizza_cesidi == "4":
        return SadePizza


def sos_secimi(sos_cesidi):
    if sos_cesidi == "Zeytin" or sos_cesidi == "11":
        return zeytinsos

    elif sos_cesidi == "Mantarlar" or sos_cesidi == "12":
        return mantarsos

    elif sos_cesidi == "Keçi Peyniri" or sos_cesidi == "13":
        return kecisos

    elif sos_cesidi == "Et" or sos_cesidi == "14":
        return etsos

    elif sos_cesidi == "Soğan" or sos_cesidi == "15":
        return sogansos

    elif sos_cesidi == "Mısır" or sos_cesidi == "16":
        return misirsos


########################################################################################################################

while True:
    menu_sec()  # menünün seçim fonksiyonu çağırıldı.

    # sorgulama
    while True:
        Pizza_cesidi = input("Listeden istediginiz pizzanin kodunu veya adini tam olarak giriniz")
        Pizzalist = ["1", "Klasik", "2", "Margarita", "3", "TürkPizza", "4", "Sade Pizza"]
        if Pizza_cesidi in Pizzalist:
            Pizza_cesidi = Pizza_cesidi
            break
        elif Pizza_cesidi not in Pizzalist:
            print("Tekrar deneyiniz!")
            continue
    print(f"Pizza seciminiz:{Pizza_cesidi}. Sos secimine devam ediniz.")
    while True:
        sos_cesidi = input("Listeden istediginiz sosun kodunu veya adini tam olarak giriniz")
        Soslist = ["11", "Zeytin", "12", "Mantarlar", "13", "Keçi Peyniri", "14", "Et", "15", "Soğan", "16", "Mısır"]
        if sos_cesidi in Soslist:
            sos_cesidi = sos_cesidi
            break
        elif sos_cesidi not in Soslist:
            print("Tekrar deneyiniz!")
            continue
    print(f"Sos seciminiz:{sos_cesidi}. Sos secimine devam ediniz.")

    # seçim sonucunu ve tutarını ekrana yazdırma.

    siparis = Decorator(pizza_secimi(Pizza_cesidi), sos_secimi(sos_cesidi))
    mus_siparisi = str(siparis.get_description()) + " " + str(siparis.get_cost())
    print(mus_siparisi + "TL hesaplandi.")

    # müşteri bilgilerini almak için gereken kısım

    print("Sipariş bilgilerinizin tamamlanması için gereken bilgileri giriniz.")
    ad_soyad = input("Adinizi ve soyadinizi giriniz... ")
    tc_no = input("TC Kimlik numaranizi giriniz...")
    kart_no = input("Kredi Kartı numarası giriniz... ")
    kart_sifresi = input("Kredi Kartı şifresini giriniz...")
    siparis_tarihi = datetime.now()


    # (Order_Database ile csv dosyası) sıparıs detaylarını dosyaya yazdıran kısımı içerir.
    def siparisi_verileri():
        with open('Orders_Database.csv', mode='a', newline='', encoding='utf-8') as siparis_dosyasi:
            yazici = csv.writer(siparis_dosyasi, delimiter=',')
            yazici.writerow([
                                f"Ad Soyad  ,  Tc No  ,  Kart No  ,  Kart Sifresi  ,  Siparis Tarihi  , Pizza adi-kodu  , Sos adi-kodu , Mus Siparisi"])
            yazici.writerow([ad_soyad, tc_no, kart_no, kart_sifresi, siparis_tarihi, Pizza_cesidi, sos_cesidi,
                             (mus_siparisi + "TL")])
siparisi_verileri()

while True:
    ekstra_siparis = input("Siparisi onayliyor musunuz? E/H ")
    if ekstra_siparis == "H":
        continue
    elif ekstra_siparis == "E":
        break

print("Siparişleriniz için teşekkür ederiz. Afiyet olsun!")


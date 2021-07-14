
## ara fonksiyonunda ilk parametre girilen cümle, ikincisi ise girilen harfdir.
# İşlevi: Cümlede girilen harfi bulup bir sonraki harfi bir listeye kaydeder.
def ara(cumle,harf):

    liste=[]
    sayac=0

    # Cümle içerisindeki tüm harflere for döngüsü ile bakılır,
    for indis in cumle:
        # Aranan harf cümlede bulunursa, bir sonraki indisteki harf "eklenecekHarf" adlı değişkene gönderilir.
        # Bu değişkendeki harf ise listeye eklenir.
        if (indis==harf):
            eklenecekHarf=cumle[sayac+1]
            liste.append(eklenecekHarf)
        sayac+=1
    print(liste)


# Kullanıcıdan Cümle ve Harf alma
cumle=(input("Bir cümle giriniz: "))
harf=(input("Bir cümle giriniz: "))

# Fonksiyona kullanıcının verilerinin gönderilmesi
ara(cumle,harf)
    

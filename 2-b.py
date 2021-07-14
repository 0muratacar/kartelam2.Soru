liste=[False,1,0,2,3,0,4,5,"a"]

# Listenin ilk hali
print(liste)
indis=0

for i in liste:
    # False ve 0 değerlerinin karışmaması için iki adet if bloğu açıldı
    # 0 Değerler tespit edilip silindi ve tekrardan listenin sonuna eklendi.
    if (i is not False):
        if(i==0):            
            liste.pop(indis)
            liste.append(0)
    indis=indis+1
# Listenin son hali
print(liste)


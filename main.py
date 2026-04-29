sarkilar = []

def get_total_duration(songs):
    toplam = 0
    for sarki in songs:
        toplam = toplam + sarki["sure"]
    return toplam


def get_most_played_song(songs):
    en_cok =songs[0]
    for sarki in songs:
        if sarki["dinlenme"] > en_cok["dinlenme"]:
            en_cok = sarki
    return en_cok

def get_average_duration(songs):
    toplam = get_total_duration(songs)
    ortalama = toplam / len(songs)
    return ortalama

def print_playlist(songs):
    print("-----Playlist-----")
    for i in range(len(songs)):
        sarki = songs[i]
        print(str(i+1) + ". " + sarki["sarki_adi"] +" - "+ sarki["sanatci"])

        print("-----------------")


def get_longest_song(songs):
    en_uzun = songs[0]
    for sarki in songs:
        if sarki["sure"] > en_uzun["sure"]:
            en_uzun = sarki
    return en_uzun

def filter_by_artist(songs, sanatci_adi):
    sonuc =[]
    for sarki in songs:
        if sarki["sanatci"] == sanatci_adi:
            sonuc.append(sarki)
    return sonuc


def sort_by_plays(songs):
    sirali = sorted(songs, key = lambda x: x["dinlenme"], reverse = True)

    return sirali


def main():

    sarkilar.append({"sarki_adi": "Mevsimler Geçerken", "sanatci": "Umut Kaya" ,"sure": 319, "dinlenme": 381000})
    sarkilar.append({"sarki_adi": "Rain Dance", "sanatci": "Dave", "sure": 341 , "dinlenme": 133778733})
    sarkilar.append({"sarki_adi" : "Beni Al", "sanatci" : "Ankara Echoes", "sure" : 246, "dinlenme" : 2490000})
    sarkilar.append({"sarki_adi" : "Son Arzum", "sanatci" : "Nilüfer", "sure" : 325, "dinlenme" : 18253698 })
    sarkilar.append({"sarki_adi": "Cinnamon Girl", "sanatci" : "Lana Del Rey", "sure": 333, "dinlenme": 197000000})
    sarkilar.append({"sarki_adi": "Summertime Sadness", "sanatci": "Lana Del Rey", "sure": 426, "dinlenme": 844000000})

    print_playlist(sarkilar)

    toplam = get_total_duration(sarkilar)
    print("Toplam süre: " + str(toplam) + " saniye\n")

    ortalama = get_average_duration(sarkilar)
    print("Ortalama süre: " + str(int(ortalama)) +" saniye\n")

    en_cok = get_most_played_song(sarkilar)
    print("En çok dinlenen: " + en_cok ["sarki_adi"] +" - " + str(en_cok["dinlenme"]) +" dinlenme\n")


    en_uzun = get_longest_song(sarkilar)
    print("En uzun şarkı: " + en_uzun["sarki_adi"] + " - " + str(en_uzun["sure"]) +  " saniye\n")


    sanatci_adi = "Lana Del Rey"
    filtre = filter_by_artist(sarkilar, sanatci_adi)

    print(sanatci_adi + " Şarkıları:")
    for sarki in filtre:
        print("- " + str(sarki["sarki_adi"]))

    print("")
    sirali = sort_by_plays(sarkilar)
    print("Dinlenme sirasina göre:")
    for sarki in sirali:
        print(sarki["sarki_adi"] + " - " + str(sarki["dinlenme"]))


main()




# music-playlist-analysis-idil-findikli
Music Playlist Analysis System
Proje Amacı:
Bu projenin amacı, bir müzik listesindeki şarkıları süre, dinlenme sayısı ve sanatçı gibi kriterlere göre analiz ederek liste istatistiklerini raporlayan ve verileri düzenleyen bir sistem geliştirmektir. Kullanıcının çalma listesini yönetmesini, filtrelemesini ve en popüler veya en uzun parçaları kolayca tespit etmesini sağlar.

Method Açıklamaları:
get_total_duration(songs): Tüm şarkıların toplam sürsini hesaplar.
get_most_played_song(songs): En çok dinlenen şarkıyı bulur.
get_average_duration(songs): Ortalama şarkı sürsini hesaplar.
print_playlist(songs): Playlisti düzenli şekilde yazdırır.
get_longest_song(songs): Playlistteki en uzun şarkıyı yazdırır.
filter_by_artist(songs, sanatci_adi): Playlistteki sanatçının şarkılarını döndürür.
sort_by_plays(songs): Şarkıları dinlenmelerine göre sıralar
main(): En az 5 şarkı oluşturur ve tüm methodları çalıştırır.

Çalıştırma Bilgisi:
Terminal üzerinden dosya dizinine gidip alttaki komutu çalıştırın.
python main.py

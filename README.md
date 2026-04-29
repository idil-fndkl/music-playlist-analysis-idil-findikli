# Proje Amacı: <br>
Bu projenin amacı, bir müzik listesindeki şarkıları süre, dinlenme sayısı ve sanatçı gibi kriterlere göre analiz ederek liste istatistiklerini raporlayan ve verileri düzenleyen bir sistem geliştirmektir. Kullanıcının çalma listesini yönetmesini, filtrelemesini ve en popüler veya en uzun parçaları kolayca tespit etmesini sağlar.

# Method Açıklamaları:<br>
get_total_duration(songs): Tüm şarkıların toplam süresini hesaplar. <br>
get_most_played_song(songs): En çok dinlenen şarkıyı bulur. <br>
get_average_duration(songs): Ortalama şarkı sürsini hesaplar. <br>
print_playlist(songs): Playlisti düzenli şekilde yazdırır. <br>
get_longest_song(songs): Playlistteki en uzun şarkıyı yazdırır. <br>
filter_by_artist(songs, sanatci_adi): Playlistteki sanatçının şarkılarını döndürür. <br>
sort_by_plays(songs): Şarkıları dinlenmelerine göre sıralar. <br>
main(): En az 5 şarkı oluşturur ve tüm methodları çalıştırır. <br>

# Çalıştırma Bilgisi: <br>
Terminal üzerinden dosya dizinine gidip aşağıdaki komutu çalıştırın; <br>
python main.py

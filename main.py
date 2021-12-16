"""
semua sintaksis dasar bahasa pemrograman dari :
1. Sekuensial :  langkah Berurutan
2. Percabangan : langkah Melompat jika Kondisi terpenuhi
3. Perulangan : Mengulang langkash yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('ibu berkata, "pergi ke toko"')
print('budi menjawab,"baik apa yang harus saya lakukan di toko?"')
print('ibu menjawab,"belikan satu botol susu, dan jika ada telor beli 6"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173

if jumlah_botol_susu > 0:
    print("budi mengecek harganya, dan ternyata uangnya cukup")
    print("budi membeli 1 botol susu")
else:
    print("budi tidak jadi membeli 1 botol susu")
    print("memerikan susu kepada ibu")
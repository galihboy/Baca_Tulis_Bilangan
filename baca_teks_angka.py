# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:31:32 2021

@author: galih-hermawan
"""

# inisialisasi label untuk angka 0 s/d 11
labelAngka = ('nol', 'satu', 'dua', 'tiga', 'empat', 'lima', \
         'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas')

kamusSatuanLama = {
           'puluh': '1',
           'ratus': '2',
           'ribu': '3',
           'puluh ribu': '4',
           'ratus ribu': '5',
           'juta': '6',
           'puluh juta': '7',
           'ratus juta': '8',
           'milyar': '9'
       }

kamusSatuan = {
           'puluh': '1',
           'ratus': '2',
           'ribu': '3',
           'juta': '6',
           'milyar': '9'
       }

kamusAngka = {
            'nol': '0',
            'satu': '1',
            'dua': '2',
            'tiga': '3',
            'empat': '4',
            'lima': '5',
            'enam': '6',
            'tujuh': '7',
            'delapan': '8',
            'sembilan': '9',
            'sepuluh': '10',
            'sebelas': '11',
            'seratus': '100',
            'seribu': '1000'
    }
    
kata = "seratus enam puluh dua ribu"    
lstKata = kata.split()

teks = ""
for idx, kata in enumerate(lstKata):
    print("teks: ", teks)
    if kata in kamusAngka:
        teks += "+" + kamusAngka[kata]
    elif kata in kamusSatuan:
        angka = 10**int(kamusSatuan[kata])
        teks += "*" + str(angka)
    elif kata == "belas":
        angka = teks[-1:]
        angkaBelas = teks[idx-1] 
        print("belas:",angka,"-", angkaBelas)
        teks = teks[:-1:]
        teks += "1"+ angka

# kata = "seratus enam puluh dua ribu"    
# lstKata = kata.split()

# teks = ""

# lstKata.reverse()
# nilaiSatuan = 1
# ukuran = len(lstKata)
# lstSatuan = []
# idxSatuan = 0
# for idx, kata in enumerate(lstKata):
#     print("teks:", teks)
#     print("kata:",kata)
#     if kata == "belas":
#         pass
#     elif kata in kamusAngka:
#         if lstKata[idx-1] == "belas":
#             print("belas")
#             teks += "1" + kamusAngka[kata] + "+"
#         else:
#             teks += kamusAngka[kata] + "+"
#     elif kata in kamusSatuan:
#         lstSatuan.append(kata)
#         print("lstSatuan: ",lstSatuan)
#         if len(lstSatuan)>1:
#             print(kamusSatuan[kata], ">" , kamusSatuan[lstSatuan[idxSatuan-1]])
#             #nilaiSatuan = 10**int(kamusSatuan[kata])
#             if kamusSatuan[kata] > kamusSatuan[lstSatuan[idxSatuan-1]]:
#                 nilaiSatuan = 10**int(kamusSatuan[kata]) * 10**int(kamusSatuan[lstSatuan[0]])
#                 print("OK")
#             else:
#                 nilaiSatuan = 10**int(kamusSatuan[kata]) #* 10**int(kamusSatuan[lstSatuan[idxSatuan-1]])
#                 print("OK 2", 10**int(kamusSatuan[kata]))#, " * ", 10**int(kamusSatuan[lstSatuan[idxSatuan-1]]))
            
#             #print("nilai satuan:", nilaiSatuan)
#         else:
#             nilaiSatuan = 10**int(kamusSatuan[kata])
#         teks += str(nilaiSatuan) + "*"
#         idxSatuan += 1
#     else:
#         pass
    
        
print("Teks asli = ",teks)
print("Angka = ", eval(teks[:-1]))
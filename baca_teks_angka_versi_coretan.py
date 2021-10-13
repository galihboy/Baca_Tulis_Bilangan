# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:11:24 2021

@author: galih-hermawan
"""

kamusSatuan = {
           'puluh': 1,
           'ratus': 2,
           'belas': 2.5,
           'ribu': 3,
           'juta': 6,
           'milyar': 9,
           'triliun': 12
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
            'sembilan': '9'
    }

kamusAlias = {
            'sepuluh' : 'satu puluh',
            'sebelas' : 'satu belas',
            'seratus' : 'satu ratus',
            'seribu' : 'satu ribu'
    }




def KalimatBaru(kalimat):
    lstKalimat = kalimat.split()
    lstKalimat = [kamusAlias[x] if x in kamusAlias else x for x in lstKalimat]
    kalimatBaru = " ".join(lstKalimat)
    #lstKalimatBaru = kalimatBaru.split()
    return kalimatBaru

def PengelompokanKalimat(kalimat):
    lstKata = kalimat.split()
    lstSatuan = []
    
    # mengambil komponen (kata) terakhir dari teks
    kataTerakhir = lstKata[-1]
    
    # cari satuan dan tampung di list
    lstSatuan = [[kamusSatuan[i], no, i] for no, i in enumerate(lstKata) if i in kamusSatuan]
    
    lstSatuanProses = []
    lstCek = lstSatuan.copy()
    idxAwal = 0
    
    if len(lstSatuan) == 0:
        # jika kalimat tidak mengandung satuan, langsung keluarkan
        lstSatuanProses = [kalimat]
    else:
        while len(lstCek) != 0:
            # cari satuan paling besar, temukan indeksnya, 
            # dan ambil semua kata dari kiri hingga indeks tersebut
            maks = max(lstCek)
            idx = maks[1]
            lstAmbil = lstKata[idxAwal:idx+1]
            teks = " ".join(lstAmbil)
            lstSatuanProses.append(teks)
            
            # indeks awal pindah ke sebelah kanannya
            idxAwal = idx+1
            idCek = lstCek.index(maks)
            # hapus isi list yang sudah dibaca, dan isinya dipindahkan
            del lstCek[0:idCek+1]
            
        # jika terdapat angka (bukan satuan) di bagian terakhir kalimat
        if kataTerakhir in kamusAngka:
            lstSatuanProses.append(kataTerakhir)
        
    return lstSatuanProses

#----------------------------------------------------
kalimat = "seratus ribu lima ratus dua puluh satu"
#kalimat = "dua ratus lima puluh"
kalimat = KalimatBaru(kalimat)
#lstKalimat = kalimat.split()
#ukuran = len(lstKalimat)

print(PengelompokanKalimat(kalimat))


# teks = ""

# for i, sat in enumerate(lstKalimat):
#     if sat in kamusAngka:
#         teks += "+" + kamusAngka[sat]
#     elif sat == "belas":
#         teks = teks[:-1] + "1" + teks[-1:]
#     elif sat in kamusSatuan:
#         pengali = 10**kamusSatuan[sat]
#         if i == ukuran-1:
#             teks = "(" + teks[:] + ")" + "*" + str(pengali)
#         else:
#             teks += "*" + str(pengali)
        
# print("Ekspresi: ", teks)
# print("Hasil evaluasi: ", eval(teks))

#if CekSintaks(teks):
#    nilai = eval(teks)
#    print("Nilai: ", nilai)
#    total += nilai
#else:
#    print(f"Format teks '{teks}' tidak valid.")
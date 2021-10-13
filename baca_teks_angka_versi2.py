# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:31:28 2021

@author: galih-hermawan
"""
import locale
locale.setlocale(locale.LC_ALL, '') 

def CekSintaks(ekspresi):
    try:
        eval(ekspresi)
    except SyntaxError:
        return False
    else:
        return True
    
    
def Koleksi(kalimat):
    lstKata = kalimat.split()
    lstSatuan = []
    
    # merapikan list berdasarkan data alias
    lstKata = [kamusAlias[x] if x in kamusAlias else x for x in lstKata]
    kataBaru = " ".join(lstKata)
    lstKata = kataBaru.split()
    
    kataTerakhir = lstKata[-1]
    
    #print("List rapi: ",lstKata)
    
    # cari satuan dan tampung di list
    lstSatuan = [[kamusSatuan[i], no, i] for no, i in enumerate(lstKata) if i in kamusSatuan]
    #print("List satuan: ",lstSatuan)
    
    lstSatuanProses = []
    lstCek = lstSatuan.copy()
    idxAwal = 0
    c=0
    
    if len(lstSatuan) == 0:
        lstSatuanProses = [kalimat]
    else:
        while len(lstCek) != 0:
            #print("lstCek: ",lstCek)
            maks = max(lstCek)
            #print("Maks: ", maks)
            idx = maks[1]
            lstAmbil = lstKata[idxAwal:idx+1]
            #print("Teks: ", lstAmbil)
            teks = " ".join(lstAmbil)
            lstSatuanProses.append(teks)
            
            idxAwal = idx+1
            idCek = lstCek.index(maks)
            del lstCek[0:idCek+1]

            c+=1
            if c>=10:
                print("C:",c)
                break
            
        # jika terdapat angka (bukan satuan) di bagian terakhir kalimat
        if kataTerakhir in kamusAngka:
            lstSatuanProses.append(kataTerakhir)
        
    #print("lst satuan proses: ", lstSatuanProses)
    return lstSatuanProses
    
    
    #-----------------




kamusSatuan = {
           'puluh': '1',
           'ratus': '2',
           'belas': '2.5',
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
            'sembilan': '9'
            #'sepuluh': '10',
            #'sebelas': '11',
            #'seratus': '100',
            #'seribu': '1000'
    }

kamusAlias = {
            'sepuluh' : 'satu puluh',
            'sebelas' : 'satu belas',
            'seratus' : 'satu ratus',
            'seribu' : 'satu ribu'
    }

kalimat = "dua belas juta seratus lima puluh empat ribu lima belas"
#kalimat = "sebelas ribu sebelas"
#kalimat = "seratus enam puluh dua ribu tiga ratus dua belas"    
#kalimat = "tiga ratus dua belas"
#kalimat = "seribu lima ratus lima"
#kalimat = "dua puluh satu"
print("Kalimat asli: ", kalimat)
koleksiKalimat = Koleksi(kalimat)
#kalimat_bagian = koleksiKalimat[1]
#lstKalimat = kalimat_bagian.split()
jmlKalimat = len(koleksiKalimat)

total = 0
for k in range(jmlKalimat):
    teks = ""
    #if jmlKalimat > 1
    kalimat_bagian = koleksiKalimat[k]
    lstKalimat = kalimat_bagian.split()
    ukuran = len(lstKalimat)
    for i, sat in enumerate(lstKalimat):
        if sat in kamusAngka:
            #print("angka: ", kamusAngka[sat])
            if i == 0: 
                if ukuran == 1:
                    teks += kamusAngka[sat]
                else:
                    teks += "(" + kamusAngka[sat]
            else:
                if i == ukuran-2 :
                    teks += "+" + kamusAngka[sat] + ")"
                elif i == ukuran-1:
                    teks += "+" + kamusAngka[sat] + ")"
                else:
                    teks += "+" + kamusAngka[sat]
                #if lstTeksBaca[i-1] in kamusSatuan:
                #    teks += "+" + sat
        elif sat in kamusSatuan:
            #print("idx: ", i, " satuan: ",kamusSatuan[sat])
            
            if sat ==  'belas':
                #print("belas")
                #print("teks belas 1: ", teks )
                
                #p = teks[:-1] #+ "1" + teks[-1:]
                akhirTeks = teks[-1]
                if akhirTeks == ")":
                    teks = teks[:-2] + "1" + teks[-2:]
                else:
                    teks = teks[:-1] + "1" + teks[-1:]
                #print("teks belas 2: ", teks )
                if not CekSintaks(teks):
                        teks += ")"
            else:
                pengali = 10**int(kamusSatuan[sat])
                if i == ukuran-1 :
                    print("\nsatuan terakhir - ")
                    if len(teks.strip()) == 0:
                        teks += str(pengali) #+ ")"
                    elif not CekSintaks(teks):
                        teks += ")*" + str(pengali) #+ ")"
                    else:
                        teks += "*" + str(pengali) #+ ")"
                else:
                    teks += "*" + str(pengali) 
            
    print(f"\nKalimat {k+1}: {kalimat_bagian}")
    print("Ekspresi: ",teks)
    if CekSintaks(teks):
        nilai = eval(teks)
        print("Nilai: ", nilai)
        total += nilai
    else:
        print(f"Format teks '{teks}' tidak valid.")
    
print("\nTotal nilai: ", total)
# menggunakan pemisah ribuan - tergantung regional settings
print(f"Total nilai (lokal): {total:n}")

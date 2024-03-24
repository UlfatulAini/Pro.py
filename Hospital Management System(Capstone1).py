from tabulate import tabulate

pasien = [
    {'id_pasien': 'Bae-001','nama': 'Erika Karlina','jenis_kelamin': 'Perempuan','usia': 28,'poli': 'Poli Umum'},
    {'id_pasien': 'Bae-002','nama': 'Jesika Roja','jenis_kelamin': 'Perempuan','usia': 45,'poli': 'Poli Gigi'},
    {'id_pasien': 'Bae-003','nama': 'Halim Kusuma','jenis_kelamin': 'Laki-laki','usia': 25,'poli': 'Poli Penyakit Dalam'},
    {'id_pasien': 'Bae-004','nama': 'Pino Perabi','jenis_kelamin': 'Laki-laki','usia': 31,'poli': 'Poli Penyakit Dalam'},
    {'id_pasien': 'Bae-005','nama': 'Sari Adem','jenis_kelamin': 'Perempuan','usia': 39,'poli': 'Poli Kandungan'},
    {'id_pasien': 'Bae-006','nama': 'Budi setiawan','jenis_kelamin': 'Laki-laki','usia': 19,'poli': 'Poli Umum'},
    {'id_pasien': 'Bae-007','nama': 'Ani Labo','jenis_kelamin': 'Perempuan','usia': 41,'poli': 'Poli Orthopedi'},
    {'id_pasien': 'Bae-008','nama': 'Andi Widodo','jenis_kelamin': 'Laki-laki','usia': 27,'poli': 'Poli Tht'},
    {'id_pasien': 'Bae-009','nama': 'Rina Seraya','jenis_kelamin': 'Perempuan','usia': 17,'poli': 'Poli Umum'},
    {'id_pasien': 'Bae-010','nama': 'Toni Handoko','jenis_kelamin': 'Laki-laki','usia': 49,'poli': 'Poli Penyakit Dalam'},
    {'id_pasien': 'Bae-011','nama': 'Pino Sebastian','jenis_kelamin': 'Laki-laki','usia': 27,'poli': 'Poli Umum'}
]

#Loop Utama

def tampilkan_menu_utama():
    print("\nBaeduri's Hospital - Management System")
    print('==============Menu Utama==============')
    print('1. Lihat Daftar Pasien')
    print('2. Tambah Pasien Baru')
    print('3. Perbarui Data Pasien')
    print('4. Hapus Pasien')
    print('5. Cari Pasien')
    print('6. Keluar')

def menu_utama():
    tampilkan_menu_utama()
    pilihan = input('\nMasukan menu plihan Anda (1-6): ')

    if pilihan == '1':
        submenu_daftar_pasien()
    elif pilihan == '2':
        submenu_tambah_pasien()
    elif pilihan == '3':
        submenu_perbarui_pasien()
    elif pilihan == '4':
        submenu_hapus_pasien()
    elif pilihan == '5':
        submenu_cari_pasien()
    elif pilihan == '6':
        print('\nTerima Kasih telah menggunakan Aplikasi ini.')
        exit()
    else:
        print('Menu yang anda pilih tidak valid. silahkan coba lagi.')
        menu_utama()        

#Untuk Pilihan Menu 1
        
def seluruh_pasien():
    if not pasien:
        print('Tidak ada pasien yang terdaftar.')
    else:
        print('\nDaftar Pasien:')
        print('==============')
        headers_data = ['No', 'ID Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli']
        data = []
        nomor = 1
        for p in pasien:
            data.append([nomor, p['id_pasien'], p['nama'], p['jenis_kelamin'], p['usia'], p['poli']])
            nomor += 1
        print(tabulate(data, headers=headers_data, tablefmt='grid'))
        
    submenu_daftar_pasien()

def pasien_dicari():
    print('\nCari Pasien: ')
    print('=============')
    kriteria = input('Masukkan id pasien: ').strip().lower()
    pasien_ditemukan = []
    for p in pasien:
       if kriteria in p['id_pasien'].lower():
           pasien_ditemukan.append(p)

    if not pasien_ditemukan:
       print(f"\nTidak ada pasien yang ditemukan dengan id '{kriteria}'.")
    else:
        print(f"Pasien yang ditemukan dengan id pasien '{kriteria}':") 
        headers = ['ID Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli']
        data = []
        for p in pasien_ditemukan:
            data.append([p['id_pasien'], p['nama'], p['jenis_kelamin'], p['usia'], p['poli']])
        print(tabulate(data, headers=headers, tablefmt='grid'))

    submenu_daftar_pasien()

def submenu_daftar_pasien():
    print('\nPilihan: ')
    print('1. Tampilkan data seluruh pasien.')
    print('2. Cari pasien.')
    print('3. Kembali ke menu utama.')
    pilihan = input('Masukkan pilihan Anda (1-3): ')

    if pilihan == '1':
        seluruh_pasien()
    elif pilihan == '2':
        pasien_dicari()
    elif pilihan == '3':
        menu_utama()
    else:
        print('Pilihan Anda tidak valid. Silahkan coba lagi.')
        submenu_daftar_pasien()

#Untuk Pilihan Menu 2
        
def tambah_pasien():
    print('\nTambah Pasien Baru')
    print('====================')
    id_pasien = input('Masukkan ID Pasien: ').strip().title()
    while len(id_pasien) != 7:
        print('ID Pasien harus terdiri dari 7 karakter.')
        id_pasien = input('Masukkan ID Pasien: ').strip().title()

    if any(p['id_pasien'] == id_pasien for p in pasien):
        print(f'ID Pasien {id_pasien} sudah ada. Silahkan gunakan ID yang berbeda.')
        submenu_tambah_pasien()
        return

    nama = input('Masukkan nama pasien: ').strip().title()
    while len(nama) > 55:
        print('Nama pasien tidak boleh lebih dari 55 karakter.')
        nama = input('Masukkan nama pasien: ').strip().title()

    jenis_kelamin = input('Masukkan jenis kelamin pasien L/P ("L" untuk Laki-laki dan "P" untuk Perempuan): ').strip().upper()
    while jenis_kelamin not in ['L', 'P']:
        print('Jenis kelamin harus "L" (laki-laki) atau "P" (Perempuan).')
        jenis_kelamin = input('Masukkan jenis kelamin pasien L/P ("L" untuk Laki-laki dan "P" untuk Perempuan): ').strip().upper()

    usia = input('Masukkan usia pasien: ')
    while not usia.isdigit() or len(usia) > 3 or int(usia) < 0:
        print('Usia harus berupa angka maksimal 3 digit dan tidak boleh negatif.')
        usia = input('Masukkan usia pasien: ')

    poli = input('Masukkan poli untuk pasien: ').strip().title()
    while len(poli) > 25:
        print('Nama poli tidak boleh lebih dari 25 karakter.')
        poli = input('Masukkan poli untuk pasien: ').strip().title()

    #menunjukkan data pasien yang akan disimpan
    print('\nData pasien yang akan disimpan: ')
    print('==================================')
    print(f'ID Pasien: {id_pasien}')
    print(f'Nama : {nama}')
    print(f"Jenis Kelamin: {'Laki-laki' if jenis_kelamin == 'L' else 'Perempuan'}")
    print(f'usia: {usia}')
    print(f'Poli: {poli}')

    #validasi apakah data sudah sesuai dan ingin disimpan
    konfirmasi = input('\nApakah data diatas sudah sesuai dan ingin disimpan? (ya/tidak): ').strip().lower()
    while konfirmasi not in ['ya','tidak']:
        konfirmasi = input('\nApakah data diatas sudah sesuai dan ingin disimpan? (ya/tidak): ').strip().lower()
    
    if konfirmasi == 'ya':
        pasien_baru = {'id_pasien': id_pasien, 'nama': nama, 'jenis_kelamin': 'Laki-laki' if jenis_kelamin == "L" else 'Perempuan', 'usia': usia, 'poli': poli}
        pasien.append(pasien_baru)
        print(f'Pasien {nama} dengan ID {id_pasien} telah ditambahkan.')
    else:
        print('\nData pasien batal ditambahkan.')
    
    submenu_tambah_pasien()

def submenu_tambah_pasien():
    print('\nPilihan: ')
    print('1. Tambah Pasien baru.')
    print('2. Kembali ke menu utama.')
    pilihan = input('Masukkan pilihan Anda (1-2): ')

    if pilihan == '1':
        tambah_pasien()
    elif pilihan == '2':
        menu_utama()
    else:
        print('Pilihan Anda tidak valid. Silahkan coba lagi.')
        submenu_tambah_pasien()

#Untuk Pilihan Menu 3
        
def perbarui_pasien():
    print('\nPerbarui Data Pasien')
    print('=====================')
    id_pasien = input('Masukkan ID Pasien yang ingin diperbarui: ').strip().title()
    pasien_ditemukan = None
    for p in pasien:
        if p['id_pasien'].lower() == id_pasien.lower():
            pasien_ditemukan = p
            break

    if pasien_ditemukan:
        print('\nData pasien yang akan diperbarui: ')
        data_pasien = [['Id Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli'],
                       [pasien_ditemukan['id_pasien'], pasien_ditemukan['nama'], pasien_ditemukan['jenis_kelamin'], pasien_ditemukan['usia'], pasien_ditemukan['poli']]]
        print(tabulate(data_pasien, headers='firstrow', tablefmt='grid'))

        #validasi apakah data akan diperbarui
        konfirmasi = input('Apakah data pasien diatas ingin diperbarui? (ya/tidak): ').strip().lower()
        while konfirmasi not in ['ya','tidak']:
            konfirmasi = input('Masukkan "ya" untuk memperbarui atau "tidak" untuk membatalkan: ').strip().lower()

        if konfirmasi == 'ya':
            kolom_diubah = False
            while not kolom_diubah:
                pilihan = input('\nPilihan kolom yang ingin diubah (ID Pasien, Nama, Jenis Kelamin, Usia, Poli) dan "selesai" untuk selesai: ').strip().lower()
                
                if pilihan == 'id pasien':
                    id_pasien_baru = input(f'Masukkan ID pasien baru untuk {id_pasien}: ').strip().title()
                    pasien_ditemukan['id_pasien'] = id_pasien_baru
                    kolom_diubah = True
                elif pilihan == 'nama':
                    nama_baru = input(f"Masukkan Nama baru untuk {pasien_ditemukan['nama']}: ").strip().title()
                    pasien_ditemukan['nama'] = nama_baru
                    kolom_diubah = True
                elif pilihan == 'jenis kelamin':
                    jenis_kelamin_baru = input(f'Masukkan Jenis Kelamin baru untuk {pasien_ditemukan["nama"]} L\P ("L" untuk Laki-laki dan "P" untuk Perempuan): ').strip().upper()
                    while jenis_kelamin_baru not in ['L','P']:
                        print('Jenis kelamin harus "L" untuk Laki-laki dan "P" untuk Perempuan')
                        jenis_kelamin_baru = input(f'Masukkan Jenis Kelamin baru untuk {pasien_ditemukan["nama"]} L\P ("L" untuk Laki-laki dan "P" untuk Perempuan): ').strip().upper()
                    pasien_ditemukan['jenis_kelamin'] = jenis_kelamin_baru
                    kolom_diubah = True
                elif pilihan == 'usia':
                    usia_baru = input(f"Masukkan Usia baru untuk {pasien_ditemukan['nama']}: ")
                    while not usia_baru.isdigit():
                        print('Usia harus berupa angka.')
                        usia_baru = input(f"Masukkan Usia baru untuk {pasien_ditemukan['nama']}: ")
                    pasien_ditemukan['usia'] = usia_baru
                    kolom_diubah = True
                elif pilihan == 'poli':
                    poli_baru = input(f"Masukkan Poli bau untuk {pasien_ditemukan['nama']}: ").strip().title()
                    pasien_ditemukan['poli'] = poli_baru
                    kolom_diubah = True
                elif pilihan == 'selesai':
                    break
                else:
                    print('Pilihan tidak valid. Silahkan coba lagi.')

            if kolom_diubah:
                print('\nData pasien telah diperbarui:')
                data_pasien = [['Id Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli'],
                               [pasien_ditemukan['id_pasien'], pasien_ditemukan['nama'], pasien_ditemukan['jenis_kelamin'], pasien_ditemukan['usia'], pasien_ditemukan['poli']]]
                print(tabulate(data_pasien, headers='firstrow', tablefmt='grid'))

                konfirmasi_simpan = input('\nApakah data pasien yang telah diperbarui ingin disimpan? (ya/tidak): ').strip().lower()
                while konfirmasi_simpan not in ['ya','tidak']:
                    konfirmasi_simpan = input('Masukkan "ya" untuk menyimpan dan "tidak" untuk membatalkan: ').strip().lower()

                if konfirmasi_simpan == 'ya':
                    print(f"\nData pasien {pasien_ditemukan['nama']} dengan ID Pasien {pasien_ditemukan['id_pasien']} telah diperbarui.")
                else:
                    print('Data pasien tidak diperbarui.')
            else:
                print('\nTidak ada perubahan pada data pasien.')
        else:
            print('Data pasien tidak diperbarui.')
    else:
        print(f'Pasien dengan ID {id_pasien} tidak ditemukan.')
    
    submenu_perbarui_pasien()

def submenu_perbarui_pasien():
    print('\nPilihan: ')
    print('1. Perbarui data pasien.')
    print('2. Kembali ke menu utama.')
    pilihan = input('Masukkan pilihan Anda (1-2): ')

    if pilihan == '1':
        perbarui_pasien()
    elif pilihan == '2':
        menu_utama()
    else:
        print('Pilihan Anda tidak valid. Silahkan coba lagi.')
        submenu_perbarui_pasien()

#Untuk Pilihan Menu 4

def hapus_pasien():
    print('\nHapus Pasien')
    print('================')
    id_pasien = input('Masukkan ID Pasien yang ingin dihapus: ').strip().title()
    pasien_ditemukan = None
    for p in pasien:
        if p['id_pasien'].lower() == id_pasien.lower():
            pasien_ditemukan = p
            break
    
    if pasien_ditemukan:
        print('\nData pasien yang akan dihapus:')
        data_pasien = [['Id Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli'],
                       [pasien_ditemukan['id_pasien'], pasien_ditemukan['nama'], pasien_ditemukan['jenis_kelamin'], pasien_ditemukan['usia'], pasien_ditemukan['poli']]]
        print(tabulate(data_pasien, headers='firstrow', tablefmt='grid'))

        konfirmasi = input('Apakah data pasien diatas ingin dihapus? (ya/tidak): ').strip().lower()
        while konfirmasi not in ['ya','tidak']:
            konfirmasi = input('Masukkan "ya" untuk menghapus atau "tidak" untuk membatalkan: ').strip().lower()
        
        if konfirmasi == 'ya':
            pasien.remove(pasien_ditemukan)
            print(f'Pasien dengan id {id_pasien} telah dihapus dari daftar.')
        else:
            print('Penghapusan pasien dibatalkan.')
    else:
        print(f'Pasien dengan ID {id_pasien} tidak ditemukan.')

    submenu_hapus_pasien()

def submenu_hapus_pasien():
    print('\nPilihan: ')
    print('1. Hapus pasien.')
    print('2. Kembali ke menu utama.')
    pilihan = input('Masukkan pilihan Anda (1-2): ')

    if pilihan == '1':
        hapus_pasien()
    elif pilihan == '2':
        menu_utama()
    else:
        print('Pilihan Anda tidak valid. Silahkan coba lagi.')
        submenu_hapus_pasien()
            

#Untuk Pilihan Menu 5
        
def cari_pasien():
    print('\nCari Pasien')
    print('==============')
    kriteria = input('Masukkan nama pasien yang ingin dicari: ').strip().lower()
    pasien_ditemukan = []
    for p in pasien:
        if kriteria in p['nama'].lower():
            pasien_ditemukan.append(p)

    if not pasien_ditemukan:
        print(f'Tidak ada pasien yang ditemukan dengan nama {kriteria}.')
    else:
        print(f"Pasien yang ditemukan dengan nama '{kriteria}':")
        headers_data = ['No', 'Id Pasien', 'Nama', 'Jenis Kelamin', 'Usia', 'Poli']
        data = []
        nomor = 1
        for p in pasien_ditemukan:
            data.append([nomor, p['id_pasien'], p['nama'], p['jenis_kelamin'], p['usia'], p['poli']])
            nomor += 1
        print(tabulate(data, headers=headers_data, tablefmt='grid'))
    
    submenu_cari_pasien()

def submenu_cari_pasien():
    print('\nPilihan: ')
    print('1. Cari pasien.')
    print('2. Kembali ke menu utama.')
    pilihan = input('Masukkan pilihan Anda (1-2): ')

    if pilihan == '1':
        cari_pasien()
    elif pilihan == '2':
        menu_utama()
    else:
        print('Pilihan Anda tidak valid. Silahkan coba lagi.')
        submenu_cari_pasien()


#Loop for all

while True:
    menu_utama()
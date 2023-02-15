x = 'Y'
while x == 'Y':
#---------------------------------Batas Pembuka--------------------------
    print('\n')
    print('Cafe Dipamkara')
    print('Tangerang')
    print('-------------------------')
    print('US PRAKTEK TIK \n')

    print('**ATISA**')
    n = 5
    for i in range(n-1):
        for j in range(i):
            print(' ', end='')
        for k in range(2*(n-i)-1):
            print('*', end='')
        print()
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()

    print('**ATISA**\n')
#---------------------------------Batas Pembuka--------------------------
    print('Nama Pegawai: Satya')
    customer = input('Nama Pelanggan: ')
    print('\n\n---Pilih Jenis Produk---')
    print('1    Roti        2.500 |')
    print('2    Mie         4,000 |')
    print('3    Nasi        5.000 |')
    print('4    Es Teh      3.000 |')
    print('5    Teh Tawar   2.000 |')
    print('6    Kerupuk     5.000 |')
    print('------------------------')

    def roti(x):
        return x * 2500
    def mie(x):
        return x * 4000
    def nasi(x):
        return x * 5000
    def esteh(x):
        return x * 3000
    def tehtawar(x):
        return x * 2000
    def kerupuk(x):
        return x * 5000

    o=1
    banyakbelanja = int(input("\nMasukan jumlah jenis pesanan yang anda ingin beli: "))
    hargabarang = []
    namabarang = []
    jumlah = []
    subtotal = []

    while o <= banyakbelanja:
        pilihan = int(input("\nMasukan kode barang yang anda mau beli: "))
        jumlahbarang = int(input('Berapa banyak? '))

        if pilihan == 1:
            p = roti(jumlahbarang)
            q = "Roti"
        elif pilihan == 2 :
            p = mie(jumlahbarang)
            q = "Mie"
        elif pilihan == 3:
            p = nasi(jumlahbarang)
            q = "Nasi"
        elif pilihan == 4:
            p = esteh(jumlahbarang)
            q = "Es Teh"
        elif pilihan == 5:
            p = tehtawar(jumlahbarang)
            q = "Teh Tawar"
        elif pilihan == 6:
            p = kerupuk(jumlahbarang)
            q = "Kerupuk"
        else:
            print("Tidak ada produknya...")

        hargabarang.append(p)
        jumlah.append(jumlahbarang)
        namabarang.append(q)

        o+=1
    print("\n----------------")
    print("Pelanggan pilih: ")
    print(namabarang)
    print("----------------")
    pajak = sum(hargabarang)*(7.27/100)
    subjumlahjumlah =(sum(hargabarang)+pajak)
    print("\nTotal\t\t:",sum(hargabarang))
    print("Pajak\t\t: %.0f" % pajak)
    print("Jumlah\t\t: %.0f" % subjumlahjumlah)
    duitcustomer = float(input("Pembayaran\t: "))
    print("Kembalian\t: %.0f" % (duitcustomer - subjumlahjumlah))

    print('\n\n')
    print("\tVILLA TGR REGENCY 0215535545")
    print("  VILLA TANGERANG REGENCY BLOK EE 03, PERIUK")
    print("      KEC. PERIUK KOTA TANGERANG, 15131")
    print("------------------------------------------------")
    print('''
Jmlh.   Nama Barang                        Harga
''')

    for n in range(banyakbelanja):
        namab = namabarang[n]
        hargab = hargabarang[n]
        juml = jumlah[n]
        print(f' {juml}x     {namab}                                {hargab}')
    print("\n\t\t--------------------------------")
    print("\t\tJUMLAH BARANG\t: ",sum(jumlah))
    print("\t\tHARGA JUAL\t:  %.0f" % (subjumlahjumlah))
    print("\t\tKEMBALIAN\t:  %.0f" % (duitcustomer - subjumlahjumlah))
    print("\n\t\t--------------------------------")
    x = input("Apakah mau pesan lagi?: [Y/N] ").upper()
    print("\nTerimakasih!\n")





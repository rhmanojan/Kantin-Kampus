# Source Code Aplikasi Impian
print("================================")
print("SELAMAT DATANG DI TOKO RAHMAN")
print("================================")
print("Berikut daftar barang")
print("1. Pensil - Rp 2.000")
print("2. Buku Tulis - Rp 5.000")
print("3. Penghapus - Rp 1.000")
barang = ["Pensil", "Buku Tulis", "Penghapus"]
masukan = input("Masukan angka: ")
if masukan == "1":
    print("anda memilih " + barang[0])
    jumlah = int(input("Masukkan jumlah: "))
    total = jumlah * 2000
    print("Total harga adalah Rp " , total)

elif masukan == "2":
    print("anda memilih "+ barang[1])
    jumlah = int(input("Masukkan jumlah: "))
    total = jumlah * 5000
    print("Total harga adalah Rp " , total)
elif masukan == "3":
    print("anda memilih "+ barang[2])
    jumlah = int(input("Masukkan jumlah: "))
    total = jumlah * 1000
    print("Total harga adalah Rp " , total)
    
else:
    print("barang tidak tersedia")

#!/usr/bin/env python3

import sys
import random
import string

def buat_password(panjang, besar, kecil, simbol, angka):
    karakter = ''
    if besar:
        karakter += string.ascii_uppercase
    if kecil:
        karakter += string.ascii_lowercase
    if simbol:
        karakter += string.punctuation
    if angka:
        karakter += string.digits

    if not karakter:
        print(f"Error: Anda perlu memilih setidaknya satu jenis karakter untuk password. \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
        return None

    password = ''.join(random.choice(karakter) for _ in range(panjang))
    return password

def bantuan():
    print(f"""
Penggunaan: python3 {sys.argv[0]} <PILIHAN>

Program python sederhana membuat password random.

Pilihan:

--panjang         : Menentukan panjang password yang ingin dibuat.
--simbol          : Menggunakan simbol.
--angka           : Gunakan angka.
--huruf-besar     : Gunakan huruf besar.
--huruf-kecil     : Gunakan huruf kecil.
--bantuan         : Menampilkan informasi bantuan.

Contoh: python3 {sys.argv[0]} --panjang 12 --simbol --angka --huruf-besar --huruf-kecil
""")

def utama():
    args = sys.argv[1:]
    panjang = None
    besar = False
    kecil = False
    simbol = False
    angka = False

    if not args or sys.argv[1] == "--bantuan":
        bantuan()
        return

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--panjang":
            i += 1
            if i < len(args):
                panjang = int(args[i])
                if panjang <= 0:
                    print(f"Error: Panjang password harus lebih besar dari 0. \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
                    return
            else:
                print(f"Error: Panjang password tidak valid. \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
                return
        elif arg == "--huruf-besar":
            besar = True
        elif arg == "--huruf-kecil":
            kecil = True
        elif arg == "--simbol":
            simbol = True
        elif arg == "--angka":
            angka = True
        else:
            print(f"Error: Argumen tidak valid: {arg} \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
            return
        i += 1

    if panjang is None:
        print(f"Error: Anda perlu menyertakan panjang password. \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
        return

    if not any([besar, kecil, simbol, angka]):
        print(f"Error: Anda perlu memilih setidaknya satu jenis karakter untuk password. \nKetik 'python3 {sys.argv[0]} --bantuan' untuk menampilkan informasi bantuan.")
        return

    password_custom = buat_password(panjang, besar, kecil, simbol, angka)
    if password_custom:
        print(password_custom)

if __name__ == "__main__":
    utama()

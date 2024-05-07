# Fungsi utama
def main():
    todo_list = []
    nomor_terakhir = 0  # Variabel untuk menyimpan nomor terakhir dari to-do list
    file_terbuka = None  # Menyimpan nama file yang telah dibuka sebelumnya, jika ada
    data_disimpan = False  # Menyimpan status apakah data sudah disimpan atau belum
    temp_file = "temp.txt"  # Nama file sementara

    while True:
        print()
        print("Pilih operasi:")
        print("1. Tambahkan item ke to-do list")
        print("2. Hapus beberapa data yang diinginkan")
        print("3. Tampilkan semua data yang sudah dimasukkan sebelumnya")
        print("4. Simpan data sebagai file .txt")
        print("5. Buka file yang sudah dibuat sebelumnya")
        print("6. Hapus file .txt atau todo list yang sudah tidak digunakan")
        print("7. Baca data dari file .txt")
        print("8. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8): ")
        
        if pilihan == "1":
            nomor_terakhir = tambahkan_item(todo_list, nomor_terakhir)
            data_disimpan = False
        elif pilihan == "2":
            hapus_data(todo_list)
            data_disimpan = False
        elif pilihan == "3":
            if not data_disimpan:
                print("Peringatan: Data belum disimpan. Harap simpan data terlebih dahulu sebelum melanjutkan.")
                simpan_ke_txt(todo_list, temp_file)  # Simpan data ke file sementara
            tampilkan_data(todo_list)
            tanya_keluar()
        elif pilihan == "4":
            nama_file = input("Masukkan nama file untuk disimpan (.txt akan ditambahkan secara otomatis): ")
            simpan_ke_txt(todo_list, f"{nama_file}.txt")
            data_disimpan = True
        elif pilihan == "5":
            nama_file = input("Masukkan nama file yang ingin dibuka: ")
            file_terbuka = f"{nama_file}.txt"
            print(f"File {nama_file}.txt berhasil dibuka.")
        elif pilihan == "6":
            nama_file = input("Masukkan nama file yang ingin dihapus: ")
            hapus_file(f"{nama_file}.txt")
        elif pilihan == "7":
            if file_terbuka:
                baca_dari_txt(file_terbuka)
                tanya_keluar()
            else:
                print("Tidak ada file yang dibuka. Harap buka file terlebih dahulu.")
        elif pilihan == "8":
            if not data_disimpan:
                print("Peringatan: Data belum disimpan. Harap simpan data terlebih dahulu sebelum keluar.")
                simpan_ke_txt(todo_list, temp_file)  # Simpan data ke file sementara
                continue  # Kembali ke awal loop
            print("Terima kasih telah menggunakan program ini.")
            hapus_file(temp_file)  # Hapus file sementara sebelum keluar
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    # Hapus file sementara jika program keluar
    if not data_disimpan:
        hapus_file(temp_file)


# Fungsi untuk menambahkan item ke to-do list
def tambahkan_item(todo_list, nomor_terakhir):
    nomor = nomor_terakhir + 1
    nama = input("Nama: ")
    matkul = input("Mata Kuliah: ")
    deadline = input("Deadline (format: DD/MM/YYYY): ")
    todo_list.append({"to-do-list": f"to-do-list-{nomor}", "nama": nama, "matakuliah": matkul, "deadline": deadline})
    print(f"Data berhasil ditambahkan dengan nomor to-do-list: to-do-list-{nomor}")
    return nomor

# Fungsi untuk menghapus beberapa data yang diinginkan
def hapus_data(todo_list):
    print("Data yang sudah dimasukkan sebelumnya:")
    for idx, item in enumerate(todo_list, start=1):
        print(f"{idx}. Nama : {item['nama']}\nMata Kuliah : {item['matakuliah']}\nDeadline : {item['deadline']}")

    indices = input("Masukkan nomor data yang ingin dihapus (pisahkan dengan koma): ")
    indices = [int(idx.strip()) for idx in indices.split(',')]

    for idx in sorted(indices, reverse=True):
        try:
            del todo_list[idx - 1]
            print(f"Data dengan nomor {idx} berhasil dihapus.")
        except IndexError:
            print(f"Data dengan nomor {idx} tidak ditemukan.")

    # Perbarui nomor to-do-list
    for idx, item in enumerate(todo_list, start=1):
        item["to-do-list"] = f"to-do-list-{idx}"

# Fungsi untuk menampilkan semua data yang sudah dimasukkan sebelumnya
def tampilkan_data(todo_list):
    print("Data yang sudah dimasukkan sebelumnya:")
    for item in todo_list:
        print(f"To-do List: {item['to-do-list']}\nNama : {item['nama']}\nMata Kuliah : {item['matakuliah']}\nDeadline : {item['deadline']}\n")

# Fungsi untuk menyimpan data sebagai file .txt
def simpan_ke_txt(todo_list, filename):
    with open(filename, "w") as file:
        for item in todo_list:
            file.write(f"To-do List: {item['to-do-list']}\nNama : {item['nama']}\nMata Kuliah : {item['matakuliah']}\nDeadline : {item['deadline']}\n\n")
    print(f"Data telah disimpan dalam file {filename}.")

# Fungsi untuk membaca data dari file .txt
def baca_dari_txt(filename):
    try:
        with open(filename, "r") as file:
            print(f"Data yang terdapat dalam file {filename}:")
            print(file.read())
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Fungsi untuk menghapus file .txt atau todo list yang sudah tidak digunakan
def hapus_file(filename):
    import os
    try:
        os.remove(filename)
        print(f"File {filename} telah dihapus.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def tanya_keluar():
    while True:
        jawaban = input("Apakah Anda ingin keluar (k) atau kembali ke menu (m)?: ")
        if jawaban.lower() == 'k':
            print("Terima kasih telah menggunakan program ini.")
            break
        elif jawaban.lower() == 'm':
            return
        else:
            print("Pilihan tidak valid. Harap masukkan 'k' untuk keluar atau 'm' untuk kembali ke menu.")


if __name__ == "__main__":
    main()

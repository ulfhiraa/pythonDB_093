import tkinter as tk
import sqlite3
from tkinter import messagebox

#Fungsi untuk menyimpan data ke sqlite
def simpan_data_ke_sqlite(nama_Siswa, nilai_Biologi, nilai_Fisika, nilai_Inggris, prediksi_Fakultas):
# membuka atau membuat database SQLite
    conn = sqlite3.connect("MULTIPLATFORM.db")
    cursor = conn.cursor()
    
# membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_Siswa 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_Siswa TEXT,
                    nilai_Biologi INTEGER,
                    nilai_Fisika INTEGER,
                    nilai_Inggris INTEGER,
                    prediksi_Fakultas TEXT)''')

# Insert Data kedalam Table hasil_prediksi
    cursor.execute('''INSERT INTO nilai_Siswa(nama_Siswa, nilai_Biologi, nilai_Fisika, nilai_Inggris, prediksi_Fakultas) 
                    VALUES(?, ?, ?, ?, ?)''', (nama_Siswa, nilai_Biologi, nilai_Fisika, nilai_Inggris, prediksi_Fakultas))

# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

#membuat aplikasi di jendela utama
top = tk.Tk()
top.title("MULTIPLATFORM") #untuk memberi nama Judul
top.geometry("500x500") #untuk mengatur ukuran awal jendela
top.resizable(False, False) #untuk mencegah jendela agar tidak dapat diubah ukurannya

#Fungsi untuk prediksi fakultas
def prediksi_Fakultas(Biologi, Fisika, Inggris):
#kondisi untuk prediksi fakultas
    if Fisika < Biologi > Inggris:
        return "Kedokteran"
    elif Biologi < Fisika > Inggris:
        return "Teknik"
    elif Biologi < Inggris > Fisika:
        return "Bahasa"
    else :
        return "Fakultas lain"
    
    
# Fungsi untuk menampilkan
def show():
    nama_Siswa = entry_Siswa.get()
    nilai_Biologi = entry_Biologi.get()
    nilai_Fisika = entry_Fisika.get()
    nilai_Inggris = entry_BahasaInggris.get()

    hasilSiswa = f"Nama Siswa: {nama_Siswa}"
    hasilBiologi= f"Nilai Biologi: {nilai_Biologi}"
    hasilFisika = f"Nilai Fisika: {nilai_Fisika}"
    hasilInggris = f"Nilai Bahasa Inggris: {nilai_Inggris}"

    prediksi = prediksi_Fakultas(nilai_Biologi, nilai_Fisika, nilai_Inggris)

    hasilprediksi_Fakultas = f"Prediksi Fakultas: {prediksi}"

    label_hasilSiswa.config(text=hasilSiswa)
    label_hasilBiologi.config(text=hasilBiologi)
    label_hasilFisika.config(text=hasilFisika)
    label_hasilInggris.config(text=hasilInggris)
    label_hasilprediksiFakultas.config(text=hasilprediksi_Fakultas)

    if not nilai_Biologi and not nilai_Fisika and not nilai_Inggris and not nama_Siswa:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlite(nama_Siswa, nilai_Biologi, nilai_Fisika, nilai_Inggris, prediksi)
        messagebox.showinfo("Info","Data Tersimpan")

    
# Label Judul
label_judul = tk.Label(top, text="Prediksi Fakultas Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat frame inputan
frame_input = tk.LabelFrame(top, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# Label Nama Siswa
label_nama_Siswa = tk.Label(frame_input, text="Masukkan Nama Siswa: ")
label_nama_Siswa.grid(row=0, column=0, pady=10)
entry_Siswa = tk.Entry(frame_input)
entry_Siswa.grid(row=0,column=1)

# Label Nilai Biologi
label_nilai_Biologi = tk.Label(frame_input, text="Masukkan Nilai Biologi: ")
label_nilai_Biologi.grid(row=1, column=0, pady=10)
entry_Biologi = tk.Entry(frame_input)
entry_Biologi.grid(row=1,column=1)

# Label Nilai Fisika
label_nilai_Fisika = tk.Label(frame_input, text="Masukkan Nilai Fisika: ")
label_nilai_Fisika.grid(row=2, column=0, pady=10)
entry_Fisika = tk.Entry(frame_input)
entry_Fisika.grid(row=2,column=1)

# Label Nilai Bahasa Inggris
label_nilai_Inggris = tk.Label(frame_input, text="Masukkan Nilai Bahasa Inggris: ")
label_nilai_Inggris.grid(row=3, column=0, pady=10)
entry_BahasaInggris = tk.Entry(frame_input)
entry_BahasaInggris.grid(row=3,column=1)

# Tombol Submit
btn_hasil = tk.Button(top, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(top,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_hasilSiswa = tk.Label(frame_hasil, text="")
label_hasilSiswa.pack()

label_hasilBiologi =  tk.Label(frame_hasil,text="")
label_hasilBiologi.pack()

label_hasilFisika =  tk.Label(frame_hasil,text="")
label_hasilFisika.pack()

label_hasilInggris =  tk.Label(frame_hasil,text="")
label_hasilInggris.pack()

label_hasilprediksiFakultas =  tk.Label(frame_hasil,text="")
label_hasilprediksiFakultas.pack()

# Jalankan Aplikasi
top.mainloop()
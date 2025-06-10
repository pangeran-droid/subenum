# 🔗 Scraping Link Tool

Alat sederhana berbasis Python untuk mengekstrak semua link dari sebuah halaman website dan menyimpannya ke dalam file `.txt`. Cocok digunakan untuk scraping ringan, analisis SEO, atau sekadar eksplorasi web.

---

## ✨ Fitur

- Menampilkan semua link dari halaman HTML.
- Menyaring hanya link valid (`http`/`https`).
- Opsi filter berdasarkan domain tertentu.
- Menyimpan hasil ke file `hasil_links.txt`.

---

## 🛠️ Instalasi

### 1. Pastikan Python sudah terpasang:

Cek versi Python:

```bash
python --version
# atau
python3 --version
```

Jika belum ada, instal Python terlebih dahulu dari https://www.python.org/downloads/

---

### 2. Clone repositori ini

```bash
git clone https://github.com/pangeran-droid/Scraping-Link.git
cd Scraping-Link
```

---

### 3. Install dependensi

Untuk **Linux**, **Windows**, dan **macOS**:

```bash
pip install -r requirements.txt
```

Jika menggunakan Python 3:

```bash
pip3 install -r requirements.txt
```

---

## 🚀 Menjalankan Program

```bash
python scraping_link.py
```

Atau:

```bash
python3 scraping_link.py
```

### Contoh:

```
Masukan URL (contoh: https://example.com) : https://example.com
Masukkan nama domain untuk filter (kosongkan jika tidak ingin filter domain, contoh: example.com) : example.com
```

Hasil akan ditampilkan dan disimpan ke file `hasil_links.txt`.

---

## 📁 Output

- Semua link valid disimpan di:
  ```
  hasil_links.txt
  ```

---

## 📌 Catatan

- Hanya link dengan protokol `http://` atau `https://` yang akan diambil.
- Jika ingin mendeteksi link internal, ubah ke absolute URL (bisa dikembangkan lebih lanjut).
- Hati-hati scraping situs yang memiliki larangan di `robots.txt`.

---

## 📄 Lisensi

MIT License – bebas digunakan untuk keperluan pribadi maupun komersial.

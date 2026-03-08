
# 🚀 Snippet Manager (Granular-Modular Edition)

Snippet Manager adalah tool CLI (Command Line Interface) berbasis Python yang dirancang untuk menyimpan, mencari, dan menyalin kode snippet favorit kamu secara cepat. Menggunakan arsitektur modular dengan pemisahan antara **Data Master** dan **User Stats**.

---

## 🛠️ Persyaratan Sistem
* Python 3.10 atau lebih tinggi
* Clipboard Manager (Linux: `xclip` atau `xsel`)

---

## 📥 Cara Instalasi

### 1. Persiapan Lingkungan (Linux/macOS)
Karena Python modern menggunakan sistem *externally-managed-environment*, wajib menggunakan virtual environment:

```bash
# Clone repository ini
git clone [https://github.com/abduljohar11/kamus-python.git](https://github.com/abduljohar11/kamus-python.git)
cd "kamus python"

# Buat dan aktifkan Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Instal dependencies
pip install rich pyperclip

```

### 2. Instalasi Tool Clipboard (Wajib untuk Linux)

```bash
sudo apt update && sudo apt install xclip

```

---

## 📁 Struktur Folder

Proyek ini menggunakan struktur **Granular Folder** untuk mempermudah manajemen data:

```text
kamus-python/
├── data/               # Penyimpanan Data Master (Read-Only)
│   └── laravel-react/  # Nama Bahasa/Framework (Sesuai setting __init__)
│       ├── migration/  # Sub-Kategori
│       └── eloquent/   # Sub-Kategori
├── src/                # Logic Core (Database & Search Engine)
├── storage/            # Data Personal (User Stats & Favorites)
└── main.py             # Entry Point Aplikasi

```

---

## ➕ Cara Menambah Data & Bahasa

### 1. Menambah Snippet Baru

Cukup buat file `data_kode.json` di dalam sub-folder kategori yang diinginkan (atau tambahkan ke file yang sudah ada):

```json
[
  {
    "id": "LV-MIG-003",
    "title": "Add Foreign Key",
    "description": "Menambahkan relasi antar tabel.",
    "categories": ["migration", "database"],
    "code": "$table->foreignId('user_id')->constrained();",
    "link": "[https://laravel.com/docs/migrations#foreign-key-constraints](https://laravel.com/docs/migrations#foreign-key-constraints)"
  }
]

```

### 2. Menambah Bahasa Pemrograman Baru

Jika kamu ingin menambahkan bahasa baru (misal: `nodejs`):

1. Buat folder baru: `data/nodejs/`.
2. Buat sub-folder kategori di dalamnya: `data/nodejs/auth/`.
3. Letakkan file `data_kode.json` di sana.
4. Ubah inisialisasi di `main.py`:
```python
db = DBHandler(lang="nodejs")

```



---

## 🖥️ Cara Penggunaan

1. Aktifkan venv: `source venv/bin/activate`
2. Jalankan aplikasi: `python main.py`
3. Masukkan kata kunci (Contoh: `migration table`)
4. Pilih nomor snippet untuk melihat detail.
5. Ketik `c` untuk menyalin kode ke clipboard.

---

## 🔒 Catatan Keamanan (Security)

* Folder `storage/` sudah masuk dalam `.gitignore` agar data statistik dan favorit personal kamu tidak ter-push ke GitHub.
* Folder `venv/` juga diabaikan agar repositori tetap ringan.

```

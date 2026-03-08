# 🏫 Snippet Manager (School Management Edition)

Snippet Manager adalah asisten digital berbasis CLI yang diibaratkan sebagai **Perpustakaan Digital Sekolah**. Tool ini membantu Anda menyimpan "buku panduan" (kode snippet) agar mudah dicari saat sedang membangun infrastruktur aplikasi (Gedung Sekolah).

---

## 🛠️ Persyaratan Sistem

* **Python 3.10+** (Kepala Sekolah/Mesin Utama)
* **Clipboard Manager:** (Kurir pesan antar ruangan)
* Linux: `xclip` atau `xsel`
* Android: `termux-api`



---

## 📥 Cara Instalasi (Membangun Pondasi Sekolah)

### 1. Persiapan Lingkungan (Linux / Termux)

Gunakan virtual environment agar "kurikulum" proyek ini tidak bentrok dengan program lain:

```bash
# Clone repository (Pendaftaran Siswa Baru)
git clone https://github.com/abduljohar11/kamus-python.git
cd "kamus python"

# Buat dan masuki Virtual Environment (Masuk Ruang Kelas)
python3 -m venv venv
source venv/bin/activate

# Instal alat tulis (Dependencies)
pip install rich pyperclip

```

### 2. Konfigurasi Clipboard (Jalur Komunikasi)

#### **A. Untuk Linux Desktop**

```bash
sudo apt update && sudo apt install xclip

```

#### **B. Untuk Android (Termux)**

1. Instal aplikasi **Termux:API** di HP Anda.
2. Di dalam Termux, jalankan perintah:

```bash
pkg install termux-api

```

---

## 📁 Struktur Folder (Denah Sekolah)

Proyek ini menggunakan struktur **Granular Folder** agar data tidak menumpuk di satu tempat:

```text
kamus-python/
├── data/               # 📚 Perpustakaan (Data Master - Read Only)
│   └── laravel-react/  # 🏷️ Nama Jurusan (Namespace)
│       ├── migration/  # 📂 Rak Buku: Struktur Bangunan (Migration)
│       └── eloquent/   # 📂 Rak Buku: Manajemen Data (Eloquent)
├── src/                # ⚙️ Ruang Guru (Logika Pencarian & Database)
├── storage/            # 📝 Buku Saku Siswa (Statistik & Favorit Pribadi)
└── main.py             # 🚪 Gerbang Utama (Entry Point)

```

---

## ➕ Cara Menambah Koleksi (Menambah Buku Panduan)

### 1. Menambah Snippet dengan Analogi

Tambahkan data ke file `data_kode.json`. Gunakan deskripsi berbasis analogi sekolah agar mudah dipahami:

```json
{
  "id": "SCH-MIG-011",
  "title": "Modern Teacher Relation",
  "description": "Analogi: Menugaskan Wali Kelas ke sebuah Ruang Kelas. Database otomatis merujuk ID Guru ke tabel Kelas.",
  "categories": ["migration", "relationship", "school"],
  "code": "$table->foreignId('teacher_id')->constrained()->onDelete('cascade');",
  "link": "https://laravel.com/docs/migrations#foreign-key-constraints"
}

```

### 2. Menambah Jurusan Baru (Bahasa Pemrograman)

1. Buat folder baru: `data/nodejs/auth/`.
2. Isi dengan file `data_kode.json`.
3. Di `main.py`, ganti: `db = DBHandler(lang="nodejs")`.

---

## 🖥️ Cara Penggunaan (KBM - Kegiatan Belajar Mengajar)

1. **Masuk Kelas:** `source venv/bin/activate`
2. **Buka Buku Induk:** `python main.py`
3. **Cari Materi:** Masukkan kata kunci ganda (Contoh: `migration student`).
4. **Pelajari Detail:** Pilih nomor urut untuk melihat **Analogi & Kode**.
5. **Salin Jawaban:** Ketik `c` untuk menyalin kode ke clipboard Anda.

---

## 🔒 Catatan Keamanan & Privasi (Tata Tertib)

* **Privasi:** Folder `storage/` (Buku Saku) bersifat pribadi dan tidak akan dibagikan ke orang lain melalui Git.
* **Integritas:** Data di dalam folder `data/` (Perpustakaan) harus dijaga agar tetap valid sesuai standar JSON.
* **Termux:** Pastikan izin `termux-setup-storage` sudah diberikan agar kurir clipboard bisa bekerja.
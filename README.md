# Nusantara Tech - Development Environment in a Box

> Tugas Case Based 2: Containerization  
> Mata Kuliah: Administrasi Sistem

## 📌 Tentang Proyek Ini

Proyek ini adalah implementasi **"Development Environment in a Box"** menggunakan Docker dan Docker Compose untuk mensimulasikan lingkungan development terpadu milik software house **Nusantara Tech**.

Tujuannya sederhana: siapapun bisa clone repo ini, jalankan satu perintah, dan seluruh environment langsung berjalan - tanpa perlu install manual satu per satu. Tidak ada lagi sindrom _"it works on my machine"_.

### Stack yang Digunakan

| Komponen | Teknologi |
|---|---|
| App / Backend | Python (FastAPI) |
| Database | MySQL |
| Object Storage | MinIO |
| Gateway | Nginx (Reverse Proxy) |
| Orkestrasi | Docker & Docker Compose |

---

## 🗂️ Struktur Proyek

```
nusantara-tech/
├── docker-compose.yml       # Orkestrasi semua service
├── .env.example             # Template konfigurasi environment
├── nginx/
│   └── nginx.conf           # Konfigurasi reverse proxy
├── app/
│   ├── Dockerfile           # Build image FastAPI
│   ├── main.py              # Source code aplikasi CRUD
│   └── requirements.txt     # Dependency Python
└── README.md
```

---

## ⚙️ Cara Menjalankan

### Prasyarat
Pastikan sudah terinstall:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Langkah-langkah

**1. Clone repositori ini**
```bash
git clone https://github.com/abiabdillax/adsis-case-2.git
cd adsis-case-2
```

**2. Buat file `.env` dari template**
```bash
cp .env.example .env
```
Lalu edit file `.env` sesuai kebutuhan (lihat bagian Konfigurasi di bawah).

**3. Jalankan semua service**
```bash
docker-compose up -d
```

**4. Cek semua container berjalan**
```bash
docker-compose ps
```

Semua service (`app`, `mysql`, `minio`, `nginx`) harus berstatus `Up`.

---

## 🌐 Akses Layanan

| Layanan | URL | Keterangan |
|---|---|---|
| Aplikasi Web | http://localhost | Via Nginx (port 80) |
| API Docs (Swagger) | http://localhost/docs | Auto-generated FastAPI docs |
| MinIO Dashboard | http://localhost:9001 | Login dengan kredensial di `.env` |

---

## 🪣 MinIO - Object Storage

MinIO digunakan sebagai penyimpanan file upload (simulasi AWS S3).

- **Dashboard:** http://localhost:9001
- **Default bucket:** `uploads` (dibuat otomatis saat pertama kali jalan)
- **Lokasi file:** Tersimpan di Docker volume `minio_data`, tidak akan hilang meski container di-restart

---

## 🔐 Konfigurasi Environment

Salin `.env.example` menjadi `.env` dan isi nilainya:

```env
# Database
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=nusantara_db
MYSQL_USER=nusantara_user
MYSQL_PASSWORD=your_password

# MinIO
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=your_minio_password
MINIO_BUCKET=uploads

# App
DATABASE_URL=mysql+pymysql://nusantara_user:your_password@mysql/nusantara_db
MINIO_ENDPOINT=minio:9000
```

> ⚠️ Jangan pernah commit file `.env` ke GitHub. File `.gitignore` sudah dikonfigurasi untuk mengecualikannya.

---

## 🛑 Menghentikan Environment

```bash
# Stop tanpa menghapus data
docker-compose stop

# Stop dan hapus container (data di volume tetap aman)
docker-compose down

# Stop dan hapus SEMUA termasuk volume (data hilang!)
docker-compose down -v
```

---

## 👥 Pembagian Tugas

| Nama | NIM | Bagian |
|---|---|---|
| Lorem Ipsum | 000000001 | Infrastruktur & Docker (docker-compose, Nginx, .env) |
| Lorem Ipsum | 000000002 | Backend App (FastAPI, CRUD, koneksi MySQL) |
| Lorem Ipsum | 000000003 | MinIO Integration & Dokumentasi (README, screenshot) |

---

## 📸 Bukti Pengujian

> _(Screenshot akan ditambahkan setelah semua service berjalan)_

- [ ] Semua container berstatus `Up`
- [ ] Aplikasi CRUD dapat diakses di browser
- [ ] Data berhasil tersimpan ke MySQL
- [ ] File upload berhasil masuk ke MinIO
- [ ] Data tetap ada setelah `docker-compose down` lalu `up` kembali

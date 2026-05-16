# 🤝 Panduan Workflow

Dokumen ini berisi panduan cara berkontribusi ke repo ini menggunakan Git dan GitHub. Dibuat khusus buat yang belum terlalu familiar - ikuti step by step, pasti bisa!

---

## 🛠️ Persiapan Awal (Lakukan Sekali Saja)

### 1. Install Git
Download dan install Git di: https://git-scm.com/downloads

Setelah install, buka terminal (Command Prompt / PowerShell / Terminal) dan cek:
```bash
git --version
```
Kalau muncul versi git-nya, berarti berhasil.

### 2. Konfigurasi Identitas Git
Ini penting supaya setiap perubahan yang kamu buat tercatat atas namamu:
```bash
git config --global user.name "Nama Kamu"
git config --global user.email "email@kamu.com"
```
Gunakan email yang sama dengan akun GitHub kamu.

### 3. Clone Repo Ini
```bash
git clone https://github.com/abiabdillahx/adsis-case-2.git
cd adsis-case-2
```

---

## 🌿 Alur Kerja Harian

Kita pakai sistem **branch** supaya kerjaan masing-masing tidak saling ganggu.

### Branch yang ada:
| Branch | Pemilik | Isi |
|---|---|---|
| `main` | Semua | Branch utama, yang dikumpul ke dosen |
| `feature/infra` | Orang 1 | docker-compose, nginx, .env |
| `feature/app` | Orang 2 | Source code FastAPI, Dockerfile |
| `feature/minio-docs` | Orang 3 | MinIO integration, README, screenshot |

---

### Langkah Kerja Setiap Hari

**Step 1 - Pindah ke branch kamu**

Lakukan ini setiap kali mau mulai kerja:
```bash
# Ganti nama branch sesuai bagianmu
git checkout feature/infra
```

Kalau branch belum ada di lokal, buat dulu:
```bash
git checkout -b feature/infra
```

**Step 2 - Ambil update terbaru dari GitHub**
```bash
git pull origin feature/infra
```

**Step 3 - Kerjakan tugasmu**

Edit file-file yang jadi tanggung jawabmu. Kalau sudah selesai, lanjut ke step berikutnya.

**Step 4 - Simpan perubahanmu**
```bash
# Lihat file apa saja yang berubah
git status

# Tambahkan semua perubahan
git add .

# Atau tambahkan file tertentu saja
git add nama-file.yml
```

**Step 5 - Commit (beri catatan apa yang kamu ubah)**
```bash
git commit -m "Tambah konfigurasi docker-compose untuk service MySQL"
```

> 💡 Tips nulis pesan commit yang bagus:
> - Gunakan bahasa yang jelas dan spesifik
> - Contoh bagus: `"Tambah endpoint POST /mahasiswa"`
> - Contoh jelek: `"update"` atau `"fix"`

**Step 6 - Upload ke GitHub**
```bash
git push origin feature/infra
```

---

## 🔀 Menggabungkan Kerjaan ke `main` (Pull Request)

Kalau bagianmu sudah selesai dan siap digabung, jangan langsung push ke `main`. Buat **Pull Request** dulu:

1. Buka repo ini di GitHub
2. Klik tab **"Pull requests"**
3. Klik tombol **"New pull request"**
4. Pilih: `base: main` ← `compare: feature/namamu`
5. Tulis judul dan deskripsi singkat apa yang kamu kerjakan
6. Klik **"Create pull request"**
7. Minta salah satu anggota lain untuk review sebelum di-merge

---

## ❗ Aturan Penting

- **Jangan push langsung ke `main`** - selalu lewat Pull Request
- **Jangan commit file `.env`** - file itu sudah ada di `.gitignore`, biarkan saja
- **Selalu `git pull` dulu** sebelum mulai kerja, supaya kodenya selalu yang terbaru
- Kalau ada konflik (conflict), hubungi anggota yang pegang bagian itu dulu sebelum diselesaikan

---

## 🆘 Perintah Darurat

```bash
# Lihat status file yang berubah
git status

# Lihat riwayat commit
git log --oneline

# Batalkan perubahan di file tertentu (HATI-HATI: tidak bisa di-undo)
git checkout -- nama-file.py

# Lihat kamu sekarang di branch mana
git branch
```

---

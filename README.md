## 📘 Repo: Generasi Judul Berita dengan Encoder-Decoder dan Transformer

**Nama**: Ach. Nur Aqil Wahid  
**Program Studi**: Magister Kecerdasan Artifisial  
**Universitas**: Universitas Gadjah Mada  

---

### 🧾 Deskripsi Proyek

Proyek ini merupakan bagian dari **Tugas 3** dalam mata kuliah _Natural Language Processing_, yang bertujuan untuk mengeksplorasi pemodelan _sequence-to-sequence generatif_ melalui tiga pendekatan arsitektural utama:

1. **Encoder-Decoder berbasis LSTM (tanpa attention)**
2. **Encoder-Decoder dengan mekanisme Attention**
3. **Transformer model (full attention)**

Fokus utamanya adalah menghasilkan **judul berita** dari **konten artikel berita** menggunakan pendekatan NLP modern.

---

### 📊 Dataset

Dataset menggunakan **artikel berita dari NewsAPI**, terdiri dari pasangan _body_ (konten) dan _title_ (judul). Dataset ini telah diproses sebelumnya dan digunakan secara konsisten pada setiap arsitektur model.

#### Tahapan preprocessing meliputi:
- Pembersihan teks
- Tokenisasi
- Padding dan truncating
- Konversi ke format tensor

---

### 🏗️ Arsitektur Model

#### 1. **Encoder-Decoder LSTM (Basic)**
- Encoder: LSTM
- Decoder: LSTM
- Tanpa attention mechanism
- Token start/end digunakan untuk mengatur sekuens

#### 2. **Encoder-Decoder dengan Attention**
- Encoder: LSTM
- Decoder: LSTM + Bahdanau Attention
- Memungkinkan decoder fokus pada bagian tertentu dari input saat menghasilkan judul

#### 3. **Transformer**
- Encoder-Decoder stack seperti dalam arsitektur Vaswani et al.
- Self-attention, positional encoding, dan feed-forward layers

---

### 🏃 Pelatihan & Inferensi

Setiap model akan dilatih pada dataset yang sama menggunakan:
- Loss function: CrossEntropyLoss
- Optimizer: Adam
- Batch training
- Validasi model berdasarkan BLEU score atau ROUGE (opsional)

---

### 🧪 Evaluasi

#### Evaluasi Kualitatif
- Analisis manual atas hasil judul yang dihasilkan
- Penilaian subjektif terhadap keterbacaan, relevansi, dan akurasi

#### Evaluasi Efisiensi Komputasi
- Perbandingan waktu training
- Performa selama inferensi
- Ukuran model dan waktu konvergensi

---

### 📂 Struktur Folder (rencana)

```
.
├── data/
│   └── newsapi_articles.json     # Dataset berisi artikel berita dalam format JSON
├── models/
│   ├── encoder_decoder_attention.py   # Model LSTM dengan attention
│   ├── encoder_decoder_lstm.py        # Model LSTM dasar
│   └── transformer_model.py           # Model Transformer
├── notebooks/
│   └── tugas3_headline_generation.ipynb  # Notebook eksplorasi dan training model
├── outputs/
│   ├── evaluation.txt              # Hasil evaluasi model
│   └── generated_headlines.csv     # Output judul hasil prediksi model
├── utils/
│   └── preprocessing.py            # Fungsi preprocessing teks
├── README.md                       # Dokumentasi proyek
```

---

### ✍️ Catatan Penting

- Saat ini, implementasi dan pelatihan model **masih berlangsung**.
- Repository ini akan diperbarui secara berkala dengan kode, hasil pelatihan, dan evaluasi akhir.
- Mohon cek kembali setelah tanggal deadline tugas.

---

### 📌 TODO (Checklist Progress)

- [x] Persiapan struktur repo
- [ ] Implementasi Encoder-Decoder LSTM
- [ ] Implementasi LSTM dengan Attention
- [ ] Implementasi Transformer
- [ ] Pelatihan ketiga model
- [ ] Evaluasi Kualitatif dan Kuantitatif
- [ ] Penulisan laporan analisis

---
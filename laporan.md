# **Laporan Proyek Machine Learning \- Kunti Najma Jalia**

### **Domain Proyek \- Sistem Rekomendasi Destinasi Wisata di Yogyakarta**

Yogyakarta merupakan salah satu destinasi pariwisata terkemuka di Indonesia yang menawarkan berbagai jenis atraksi (Suhailah & Hartatik, 2023). Pariwisata bahkan telah menjadi salah satu kebutuhan mendasar bagi masyarakat di era modern (Pakarti & Wardani, 2022). Daya tarik Kota Yogyakarta sebagai destinasi wisata unggulan terus meningkat, yang dibuktikan dengan data kunjungan wisatawan yang mencapai 9,5 juta orang hingga akhir November 2024\. Pemerintah Kota Yogyakarta bahkan optimis angka ini akan menembus 10 juta kunjungan pada akhir tahun (Adminwarta, 2024).  
Seiring dengan kemajuan teknologi, wisatawan semakin bergantung pada internet untuk merencanakan perjalanan mereka. Mesin pencari seperti Google dan media sosial menjadi alat utama untuk mencari rekomendasi objek wisata (Pratiwi & Nada, 2022). Namun, ledakan informasi digital ini menimbulkan tantangan baru. Wisatawan seringkali dihadapkan pada daftar pilihan yang sangat banyak, kompleks, dan membutuhkan waktu untuk diseleksi (Musyrifah et al., 2022). Informasi yang disajikan seringkali acak dan tidak memuat detail yang lengkap, sehingga menyulitkan wisatawan untuk memilih destinasi yang paling sesuai dengan preferensi dan minat mereka (Sispianygala et al., 2024). Terlebih lagi, banyak aplikasi pariwisata yang ada saat ini hanya berfokus pada penyajian informasi lokasi tanpa memiliki fitur rekomendasi yang memadai (Hendrawan et al., 2022).  
Untuk mengatasi masalah kelebihan informasi (*information overload*) tersebut, diperlukan sebuah solusi cerdas yang mampu menjembatani antara banyaknya pilihan destinasi dengan preferensi unik setiap pengguna. Sistem rekomendasi menjadi komponen krusial dalam platform pariwisata modern untuk membantu pengguna mengambil keputusan. Konsep *Smart Tourism* juga menekankan pentingnya pengembangan sarana dan kemampuan informasi untuk memfasilitasi inovasi produk dan meningkatkan pengalaman wisata (Hendrawan et al., 2022). Dengan memanfaatkan *machine learning*, sistem dapat dibangun untuk memberikan rekomendasi berdasarkan data historis seperti peringkat (rating) yang diberikan pengguna (Pratiwi & Nada, 2022).  
Proyek ini bertujuan untuk mengembangkan dan membandingkan dua pendekatan utama dalam sistem rekomendasi, yaitu *Content-Based Filtering* dan *Collaborative Filtering* (Musyrifah et al., 2022). Metode *Collaborative Filtering*, khususnya varian *Item-based*, bekerja dengan menemukan pola dari item-item yang telah dinilai oleh banyak pengguna untuk merekomendasikan item serupa lainnya (Mi'roj, 2023). Sementara itu, metode *Content-Based Filtering* memberikan rekomendasi dengan menganalisis karakteristik atau konten dari item itu sendiri yang relevan dengan pilihan pengguna sebelumnya (Musyrifah et al., 2022). Dengan menerapkan kedua model ini, sistem rekomendasi tempat wisata di Yogyakarta diharapkan dapat memberikan saran yang lebih personal dan relevan, membantu pengguna membuat keputusan yang lebih baik dan cepat.

### **Referensi**

* Adminwarta. 2024\. Target Kunjungan Wisatawan ke Yogyakarta Tahun 2024 Diyakini Terlampaui. *Warta Jogja Kota*. URL: [https://warta.jogjakota.go.id/detail/index/37070](https://warta.jogjakota.go.id/detail/index/37070). Diakses pada 7 Juni 2025\.  
* Hendrawan, I.R., Indraswari, A.D., Antara, P., & Widihasani, A.F. 2022\. Elisitasi Kebutuhan Smart Tourism untuk Rekomendasi Pariwisata Yogyakarta. *JIKO (Jurnal Informatika dan Komputer)*, 6(2), 176-184.  
* Mi'roj, M.I. 2023\. Penerapan Metode Item Based Collaborative Filtering untuk Membangun Sistem Rekomendasi Pariwisata (Studi Kasus Kabupaten Sidoarjo)*.* *Skripsi*. Universitas Dinamika.  
* Musyrifah, Sulfayanti, Ap, I., Asmawati, & Zulkarnaim, N. 2022\. Sistem Rekomendasi Berbasis-Konten Untuk Pengembangan Web Smart Tourism. *Jurnal Komputer Terapan*. 8(1): 143-150.  
* Pakarti, M.B., & Wardani, A.T.F. 2022\. Sistem Informasi Pariwisata Daerah Istimewa Yogyakarta Berbasis Website Menggunakan Microsoft PowerApps. *Jurnal Informatika, Komputer dan Bisnis (JIKOBIS)*. 2(1): 12-21.  
* Pratiwi, B.M., & Nada, N.Q. 2022\. *Penerapan Model Machine Learning dalam Menentukan Rekomendasi Objek Wisata Provinsi Jawa Tengah*. Prosiding Science And Engineering National Seminar 7 (SENS 7). 15 Desember 2022\. Indonesia.  
* Sispianygala, A., Berutu, S.S., & Jatmitka. 2024\. Pengembangan Aplikasi Sistem Rekomendasi Tempat Wisata Dengan Collaborative Filtering. *Progresif: Jurnal Ilmiah Komputer*. 20(2): 828-838.  
* Suhailah, E., & Hartatik. 2023\. Pembuatan Sistem Rekomendasi Pariwisata Yogyakarta Menggunakan Triangle Multiplaying Jaccard. *JACIS: Journal Automation Computer Information System*. 3(2): 115-126.

### **Business Understanding**

Proses klarifikasi masalah dalam proyek ini berfokus pada pemahaman kebutuhan untuk memberikan rekomendasi tempat wisata yang dipersonalisasi di Yogyakarta dan bagaimana *machine learning* dapat memberikan solusi yang bernilai tambah bagi wisatawan dan pemangku kepentingan pariwisata.

#### **Problem Statements**

1. Bagaimana cara merekomendasikan tempat-tempat wisata yang memiliki karakteristik serupa kepada pengguna?  
2. Bagaimana cara memberikan rekomendasi tempat wisata yang bersifat personal kepada seorang pengguna berdasarkan pola rating dari pengguna lain yang memiliki selera serupa?  
3. Pendekatan mana antara *Content-Based Filtering* dan *Collaborative Filtering* yang lebih sesuai?

#### **Goals**

1. Mengembangkan model *Content-Based Filtering* (CBF) yang mampu merekomendasikan 5 tempat wisata teratas yang paling mirip dengan suatu tempat wisata yang dipilih sebagai referensi.  
2. Mengembangkan model *Collaborative Filtering* (CF) yang mampu memprediksi preferensi rating pengguna terhadap tempat-tempat yang belum pernah ia kunjungi dan merekomendasikan 5 tempat teratas berdasarkan prediksi tersebut.  
3. Menganalisis dan membandingkan karakteristik dari kedua model untuk memahami kelebihan dan kekurangan masing-masing dalam memberikan rekomendasi.

### **Solution Statements**

Untuk mencapai tujuan-tujuan tersebut, tahapan solusi yang akan dilakukan dalam proyek ini adalah sebagai berikut:

1. **Pengumpulan Data**: Data yang digunakan bersumber dari Kaggle yang mencakup tiga dataset terpisah: data tempat wisata (`tourism_with_id.csv`), data rating dari pengguna (`tourism_rating.csv`), dan data demografi pengguna (`user.csv`).  
2. **Pemrosesan Awal Data (*Data Preprocessing*)**:  
   * Menangani nilai duplikat pada setiap dataset untuk memastikan integritas data.  
   * Melakukan filtering untuk memfokuskan analisis dan pemodelan hanya pada destinasi di wilayah Yogyakarta.  
3. **Analisis Data Eksploratif (*Exploratory Data Analysis \- EDA*)**:  
   * Melakukan analisis statistik deskriptif untuk memahami distribusi variabel kunci seperti rating, kategori wisata, dan usia pengguna.  
   * Memvisualisasikan data untuk mengidentifikasi pola dan tren, seperti distribusi rating, sebaran destinasi per kota dan kategori, serta distribusi usia pengguna.  
4. **Persiapan Data untuk Pemodelan (*Data Preparation*)**:  
   * **Untuk Content-Based Filtering (CBF):** Melakukan rekayasa fitur dengan menggabungkan kolom teks (`Place_Name`, `Category`, `Description`) menjadi satu fitur konten. Teks tersebut kemudian dibersihkan dan diproses menggunakan teknik *stemming* dan *stopword removal* dengan library Sastrawi.  
   * **Untuk Collaborative Filtering (CF):** Melakukan *encoding* pada ID pengguna dan tempat wisata untuk mengubahnya menjadi indeks numerik. Selanjutnya, nilai rating dinormalisasi ke dalam rentang 0 hingga 1\. Terakhir, data dibagi menjadi data latih (80%) dan data validasi (20%).  
5. **Pengembangan Model (*Model Development*)**:  
   * **Content-Based Filtering (CBF):** Membangun model dengan menghitung bobot TF-IDF dari fitur konten, kemudian mengukur kemiripan antar item menggunakan metrik *Cosine Similarity*.  
   * **Collaborative Filtering (CF):** Mengembangkan model jaringan saraf tiruan (*neural network*) menggunakan TensorFlow/Keras. Model ini menggunakan lapisan *Embedding* untuk mempelajari representasi vektor (laten) dari pengguna dan tempat wisata, yang kemudian digabungkan untuk memprediksi rating.  
6. **Evaluasi Model (*Model Evaluation*)**:  
   * **Model CBF** dievaluasi secara **kualitatif** dengan menginspeksi relevansi dari 5 rekomendasi teratas yang dihasilkan untuk sebuah tempat wisata sampel.  
   * **Model CF** dievaluasi secara **kuantitatif** menggunakan metrik *Root Mean Squared Error* (RMSE) dan *Loss* pada data training dan validasi untuk memantau performa dan potensi *overfitting*.

### **Data Understanding**

Dataset yang digunakan dalam proyek ini terdiri dari tiga sumber utama yang berasal dari platform Kaggle.

* **Sumber Data:**  
  * Dataset Wisata Indonesia: Diperoleh dari Kaggle, dapat diakses melalui tautan berikut: [https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination)  
  * Dataset yang digunakan meliputi:  
    * `tourism_with_id.csv`  
    * `tourism_rating.csv`  
    * `user.csv`  
* **Informasi Dataset Utama (Sebelum Filtering):**  
  * Jumlah total destinasi wisata: **437**.  
  * Jumlah total data rating dari pengguna: **10000**.  
  * Jumlah total pengguna dalam dataset: **300**.  
  * Setelah proses filtering, data yang digunakan adalah **126** destinasi di Yogyakarta dengan **2848** data rating yang relevan.  
* **Variabel-variabel pada Dataset:**  
  * **`df_tourism`:**  
    * `Place_Id`: ID unik untuk setiap tempat wisata.  
    * `Place_Name`: Nama tempat wisata.  
    * `Description`: Deskripsi singkat mengenai tempat tersebut.  
    * `Category`: Kategori wisata (misalnya, Budaya, Cagar Alam).  
    * `City`: Kota lokasi wisata.  
    * `Price`: Harga tiket masuk (dalam Rupiah).  
    * `Rating`: Rata-rata rating publik (skala 1-5).  
    * `Time_Minutes`: Estimasi waktu kunjungan dalam menit (memiliki 232 nilai null).  
    * `Coordinate`: Koordinat geografis dalam format dictionary.  
    * `Lat`: Garis lintang.  
    * `Long`: Garis bujur.  
    * `Unnamed: 11`, `Unnamed: 12`: Kolom tambahan yang muncul saat membaca file CSV. Kolom ini tidak mengandung informasi relevan dan akan diabaikan dalam analisis.  
  * **`df_rating`:**  
    * `User_Id`: ID unik untuk setiap pengguna.  
    * `Place_Id`: ID tempat wisata yang diberi rating.  
    * `Place_Ratings`: Rating yang diberikan oleh pengguna (skala 1-5).  
  * **`df_user`:**  
    * `User_Id`: ID unik pengguna.  
    * `Location`: Lokasi (kota dan provinsi) pengguna.  
    * `Age`: Usia pengguna.

### **Exploratory Data Analysis (EDA)**

Pada tahap EDA, beberapa temuan penting meliputi:

* **Distribusi Rating Pengguna:** Rating yang paling sering diberikan oleh pengguna adalah **4**.  
* **Sebaran Destinasi Berdasarkan Kategori (di Yogyakarta):** Kategori **Cagar Alam**, **Budaya**, dan **Taman Hiburan** merupakan tiga kategori dengan jumlah destinasi terbanyak di Yogyakarta.  
* **Distribusi Usia Pengguna:** Pengguna dalam dataset ini memiliki rentang usia dari 18 hingga 40 tahun. Distribusi usia menunjukkan konsentrasi yang kuat pada rentang **24 hingga 34 tahun**, dengan median usia berada di sekitar **29 tahun** dan modus di **30 tahun**..

#### **Data Preparation**

Tahapan persiapan data merupakan fase krusial dalam pengembangan model *machine learning*. Prinsip *‘garbage in, garbage out’* sangat berlaku di sini, yang berarti kualitas model sangat bergantung pada kualitas data yang digunakan untuk melatihnya. Oleh karena itu, sebelum data dimasukkan ke dalam model, perlu dilakukan serangkaian proses untuk membersihkan, mentransformasi, dan menstrukturkan data agar menjadi format yang optimal. Tahapan ini bertujuan untuk memastikan data yang digunakan bersih dari inkonsistensi, relevan dengan masalah yang akan diselesaikan, dan siap untuk diproses oleh algoritma *machine learning*, sehingga pada akhirnya dapat menghasilkan model rekomendasi yang akurat dan andal.  
Langkah-langkah persiapan data yang dilakukan dalam proyek ini adalah sebagai berikut:

1. **Penanganan Duplikat**:  
   * **Proses**: Dilakukan pengecekan dan penghapusan data duplikat pada `df_rating`. Ditemukan dan dihapus sebanyak 79 baris data yang identik.  
   * **Alasan**: Menjamin setiap interaksi rating bersifat unik dan meningkatkan kualitas data input untuk model.  
2. **Filtering Data Yogyakarta**:  
   * **Proses**: `df_tourism` difilter untuk hanya menyisakan baris dengan `City` berisi 'Yogyakarta'. Hasilnya, diperoleh dataframe baru (`df_tourism_yogya`) dengan 126 destinasi.  
   * **Alasan**: Memfokuskan cakupan proyek agar sesuai dengan tujuan.  
3. **Penanganan *Missing Values***:  
   * **Proses**: Dilakukan penanganan nilai yang hilang pada kolom `Rating` di `df_tourism_yogya` dengan menggunakan nilai median dari kolom tersebut.  
   * **Alasan**: Memastikan tidak ada data rating yang kosong yang dapat mengganggu proses pemodelan.  
4. **Rekayasa Fitur dan TF-IDF Vectorization untuk CBF**:  
   * **Proses**: Kolom `Place_Name`, `Category`, dan `Description` dari dataframe yang telah difilter digabungkan menjadi satu fitur tunggal bernama `content_features`. Fitur ini kemudian diproses menggunakan Sastrawi untuk *stemming* dan *stopword removal*. Selanjutnya, teknik **TF-IDF Vectorization** diterapkan untuk mengubah fitur teks menjadi representasi vektor numerik.  
   * **Alasan**: Membuat representasi numerik dari konten tekstual yang dapat diukur kemiripannya oleh model *Content-Based Filtering*.  
5. **Persiapan Data untuk CF**:  
   * **Proses**: `User_Id` dan `Place_Id` pada data rating Yogyakarta diubah menjadi indeks numerik (encoding). `Place_Ratings` dinormalisasi ke skala 0-1. Dataset kemudian diacak dan dibagi menjadi 80% data latih dan 20% data validasi.  
   * **Alasan**: Menyiapkan data untuk input model *neural network*.

### **Modeling and Result**

Pada tahap ini, dikembangkan dua sistem rekomendasi dengan algoritma yang berbeda untuk menyelesaikan permasalahan yang telah diidentifikasi. Setiap model dijelaskan secara lebih rinci, mulai dari arsitektur teknis, cara kerja, hingga output yang dihasilkan berupa *top-N recommendation*.


#### **1\. Content-Based Filtering (CBF)**

Sistem *Content-Based Filtering* (CBF) bekerja dengan merekomendasikan item berdasarkan kemiripan fitur atau kontennya. Arsitektur model ini tidak melibatkan *deep learning*, melainkan serangkaian proses linguistik dan matematis sebagai berikut:

1. **Representasi Konten**: Untuk setiap tempat wisata, dibuat sebuah "dokumen" tunggal dengan menggabungkan fitur-fitur tekstualnya, yaitu `Place_Name`, `Category`, dan `Description` (laporan.md).  
2. **Vektorisasi**: Teks dari setiap dokumen diubah menjadi representasi vektor numerik menggunakan metode yang dijelaskan pada bagian *Data Preparation*. Hasilnya adalah matriks dengan dimensi `(126, 2151)`, yang merepresentasikan 126 tempat wisata dengan vocabulary sebanyak 2.151 kata unik (notebook.ipynb).  
3. **Perhitungan Kemiripan**: **Cosine Similarity** digunakan untuk menghitung skor kemiripan antara setiap pasang vektor tempat wisata (notebook.ipynb). Metrik ini mengukur kosinus sudut antara dua vektor dalam ruang multidimensi. Skor mendekati 1 menandakan kemiripan yang tinggi, sedangkan skor mendekati 0 menandakan ketidakmiripan.

**Menyajikan Top-N Recommendation**  
Ketika pengguna memilih satu tempat wisata, model akan mengambil vektor fiturnya dan menghitung *cosine similarity*\-nya dengan semua tempat lain. Hasilnya adalah daftar tempat wisata yang diurutkan berdasarkan skor kemiripan tertinggi. Berikut adalah 5 rekomendasi teratas yang dihasilkan untuk **'Taman Pintar Yogyakarta'**:

| Place\_Id | Place\_Name | Category | Rating | similarity\_score |
| :---- | :---- | :---- | :---- | :---- |
| 206 | Wisata Kaliurang | Cagar Alam | 4.4 | 0.192158 |
| 98 | Taman Pelangi Yogyakarta | Taman Hiburan | 4.3 | 0.148100 |
| 90 | Kampung Wisata Taman Sari | Taman Hiburan | 4.6 | 0.147447 |
| 203 | Galaxy Waterpark Jogja | Taman Hiburan | 4.3 | 0.147205 |
| 100 | Taman Budaya Yogyakarta | Budaya | 4.5 | 0.140009 |

**Kelebihan dan Kekurangan:**

| Kelebihan | Kekurangan |
| :---- | :---- |
| **Independensi Pengguna**: Tidak terpengaruh oleh data pengguna lain, efektif mengatasi masalah *cold start* untuk pengguna baru. | **Ketergantungan pada Rekayasa Fitur**: Kinerja sangat bergantung pada kualitas dan kelengkapan deskripsi konten. |
| **Transparansi (Interpretability)**: Hasil rekomendasi mudah dijelaskan karena didasarkan pada fitur konten yang jelas. | **Overspecialization (Serendipity Rendah)**: Cenderung merekomendasikan item yang sangat mirip dan kurang memberikan kejutan. |
| **Kemampuan Merekomendasikan Item Niche**: Mampu merekomendasikan item yang tidak populer selama fiturnya relevan. | **Masalah *New Item Cold Start***: Tidak dapat merekomendasikan item baru yang belum memiliki deskripsi konten. |

#### **2\. Collaborative Filtering (CF)**

Sistem *Collaborative Filtering* ini menggunakan pendekatan *deep learning* dengan arsitektur jaringan saraf tiruan yang disebut `RecommenderNet` (notebook.ipynb). Model ini tidak memerlukan informasi konten, melainkan belajar dari pola interaksi (rating) antara pengguna dan item.  
Arsitektur model `RecommenderNet` terdiri dari beberapa komponen utama:

1. **Embedding Layers**:  
   * **User & Place Embedding**: Lapisan ini mengubah setiap ID pengguna dan tempat wisata menjadi vektor padat (*embedding*) yang menangkap preferensi laten pengguna dan karakteristik laten item. Vektor ini memiliki dimensi 50, dan nilainya dipelajari selama proses pelatihan.  
2. **Bias Layers**:  
   * **User & Place Bias**: Lapisan ini mempelajari bias atau kecenderungan intrinsik seorang pengguna untuk memberi rating tinggi/rendah dan popularitas dasar sebuah tempat.  
3. **Proses Prediksi**:  
   * Model melakukan operasi **dot product** antara *user embedding* dan *place embedding* untuk mengukur tingkat kecocokan awal.  
   * Hasilnya kemudian disesuaikan dengan menambahkan **bias pengguna dan bias item**, menghasilkan prediksi yang lebih akurat.  
   * **Fungsi Aktivasi Sigmoid** mengubah skor akhir menjadi nilai probabilitas antara 0 dan 1, yang merepresentasikan rating yang telah dinormalisasi.

**Menyajikan Top-N Recommendation**  
Model akan memprediksi rating yang mungkin diberikan oleh seorang pengguna untuk semua tempat yang belum pernah ia kunjungi. Hasilnya diurutkan untuk menemukan 5 tempat dengan skor prediksi tertinggi. Untuk **User ID 1**, berikut adalah 5 rekomendasi teratas yang dihasilkan:

| Place\_Id | Place\_Name | Category | Rating | Predicted\_Normalized\_Rating |
| :---- | :---- | :---- | :---- | :---- |
| 139 | Puncak Gunung Api Purba \- Nglanggeran | Cagar Alam | 4.7 | 0.645483 |
| 138 | Jogja Exotarium | Taman Hiburan | 4.4 | 0.592980 |
| 132 | Air Terjun Kedung Pedut | Cagar Alam | 4.5 | 0.581932 |
| 134 | Desa Wisata Gamplong | Taman Hiburan | 4.4 | 0.575500 |
| 136 | Grojogan Watu Purbo Bangunrejo | Taman Hiburan | 4.5 | 0.568301 |

**Kelebihan dan Kekurangan:**

| Kelebihan | Kekurangan |
| :---- | :---- |
| **Tidak Memerlukan Fitur Item** Hanya belajar dari data interaksi (rating), sehingga mudah diimplementasikan pada domain di mana metadata sulit diperoleh. | **Masalah *Cold Start*** Tidak dapat memberikan rekomendasi untuk pengguna atau item baru yang belum memiliki riwayat rating. |
| **Tingkat *Serendipity* Tinggi** Mampu menemukan hubungan tak terduga antar item dan memberikan rekomendasi yang mengejutkan namun relevan. | **Masalah *Sparsity*** Kinerjanya menurun jika matriks interaksi pengguna-item sangat renggang (sedikit data rating). |
| **Tidak Memerlukan Analisis Konten** Model tidak bergantung pada pemrosesan bahasa alami, sehingga lebih sederhana secara teknis pada tahap persiapan data. | **Bias Popularitas** Cenderung lebih sering merekomendasikan item-item populer karena memiliki lebih banyak data interaksi. |

### **Evaluation**

Evaluasi performa model dilakukan dengan pendekatan yang berbeda untuk setiap jenis sistem rekomendasi, sesuai dengan sifat dan tujuan masing-masing model. Bagian ini akan menjelaskan secara eksplisit metrik yang digunakan, formula, cara kerja, dan hasil numerik yang diperoleh.


1. #### **Content-Based Filtering (CBF)**

Untuk model *Content-Based Filtering* (CBF), evaluasi performa dapat dilakukan secara kuantitatif dengan metrik klasifikasi standar seperti **Precision**, **Recall**, dan **F1-Score**. Metrik ini mengukur kemampuan model dalam merekomendasikan item yang relevan berdasarkan histori pengguna.  
**Metrik Evaluasi Kuantitatif:**

* **Precision**  
  Metrik ini menjawab pertanyaan, "Dari semua tempat yang direkomendasikan, berapa persen yang benar-benar relevan bagi pengguna?" Precision berfokus pada kualitas dari rekomendasi yang diberikan.

**Formula:**  
![][image1]

- **True Positives (TP):** Jumlah tempat yang direkomendasikan dan benar-benar disukai pengguna.  
- **False Positives (FP):** Jumlah tempat yang direkomendasikan namun tidak disukai pengguna.  
* **Recall**  
  Metrik ini menjawab pertanyaan, "Dari semua tempat yang seharusnya direkomendasikan, berapa persen yang berhasil ditemukan oleh model?" Recall berfokus pada cakupan atau kelengkapan dari rekomendasi.

**Formula:**  
![][image2]

- **True Positives (TP):** Jumlah tempat yang direkomendasikan dan benar-benar disukai pengguna.  
- **False Positives (FP):** Jumlah tempat yang direkomendasikan namun tidak disukai pengguna.  
- **False Negatives (FN):** Jumlah tempat yang disukai pengguna namun tidak berhasil direkomendasikan oleh model.  
* **F1-Score**  
  Ini adalah rata-rata harmonik dari Precision dan Recall. Metrik ini berguna untuk mencari keseimbangan antara Precision dan Recall, terutama jika terjadi kondisi di mana salah satu metrik sangat tinggi sementara yang lain sangat rendah.

**Formula:**   
![][image3]

**Hasil Metrik Kuantitatif**  
Berdasarkan hasil eksekusi pada *notebook*, diperoleh nilai metrik sebagai berikut:

* **Rata-rata Precision:** **0.0354**  
* **Rata-rata Recall:** **0.0936**  
* **F1-Score:** **0.0514**

**Analisis Kualitatif (Relevansi Hasil):**   
Karena evaluasi kuantitatif memiliki batasan, pendekatan **evaluasi kualitatif** juga penting. Perlu ditekankan bahwa **Cosine Similarity** bukanlah metrik evaluasi performa, melainkan bagian dari proses *modeling*.  
Evaluasi kualitatif dilakukan dengan menganalisis relevansi 5 item teratas yang direkomendasikan. Saat model diberi input **'Taman Pintar Yogyakarta'**, rekomendasi yang dihasilkan adalah sebagai berikut:

| Place\_Name | Category | Rating | similarity\_score |
| :---- | :---- | :---- | :---- |
| Wisata Kaliurang | Cagar Alam | 4.4 | 0.192158 |
| Taman Pelangi Yogyakarta | Taman Hiburan | 4.3 | 0.148100 |
| Kampung Wisata Taman Sari | Taman Hiburan | 4.6 | 0.147447 |
| Galaxy Waterpark Jogja | Taman Hiburan | 4.3 | 0.147205 |
| Taman Budaya Yogyakarta | Budaya | 4.5 | 0.140009 |

Hasil di atas menunjukkan model mampu memberikan rekomendasi yang relevan lintas kategori, membuktikan bahwa model berhasil menangkap nuansa dari konten tekstual.


2. #### **Collaborative Filtering**

Model *Collaborative Filtering* (CF) pada proyek ini dilatih untuk memprediksi rating, sehingga kinerjanya diukur secara kuantitatif menggunakan metrik evaluasi untuk masalah regresi.  
**Metrik yang Digunakan** yaitu **Root Mean Squared Error (RMSE)** yang digunakan untuk mengevaluasi sistem rekomendasi yang memprediksi rating karena kemampuannya memberikan bobot lebih pada kesalahan yang besar.

* **Formula RMSE:**  
  ![][image4]  
  Di mana:  
  * n adalah jumlah total data pada set validasi.  
  * ∑ adalah simbol sigma yang berarti "jumlah total dari".  
  * yi​ adalah nilai rating aktual yang diberikan pengguna untuk item ke-i.  
  * y^​i​ adalah nilai rating yang diprediksi oleh model untuk item ke-i.  
  * (yi​−y^​i​)2 adalah kuadrat dari selisih (error) antara rating aktual dan prediksi.  
* **Cara Kerja dan Interpretasi**  
  RMSE bekerja dengan cara menghitung selisih (error) untuk setiap prediksi, mengkuadratkannya, menghitung rata-ratanya, lalu meng-akarkannya kembali. Langkah **pengkuadratan** adalah kunci: ini membuat error yang lebih besar memiliki dampak yang jauh lebih signifikan terhadap skor akhir dibandingkan error kecil. Dengan kata lain, model akan "dihukum" lebih berat jika membuat satu prediksi yang sangat salah daripada membuat beberapa prediksi yang sedikit salah.  
  **Semakin rendah nilai RMSE, semakin baik kinerja model** karena ini menandakan bahwa prediksi model secara rata-rata lebih dekat dengan nilai rating yang sebenarnya.

**Hasil Metrik Evaluasi**  
Berdasarkan proses pelatihan di *notebook* (epoch ke-100), diperoleh nilai metrik pada data validasi sebagai berikut:

* **Final Validation RMSE:** **0.3836**  
* **Final Validation Loss:** **0.7558**

Nilai RMSE yang rendah ini menunjukkan performa model yang baik dalam memprediksi rating pengguna pada data yang belum pernah dilihat sebelumnya. Hasil visualisasi kurva pembelajaran pada *notebook* juga mengonfirmasi bahwa model tidak mengalami *overfitting*.

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPAAAABGCAIAAAB9pI6tAAAO90lEQVR4Xu2ceWwWxRvHK0cVilYRifGoF6JBiK0mElETBDk8UhD0D1GDoBGUiGAEIx5NkCJCQFQQwYSoEbxIRIR4BAwSFfxDQPEApAGqYAERKzft++7vw3zdcTt9W9q3Lb+ync8fm3lnn51j5zvPPLPdbUbg8cSIDDfD4zmR8YL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8IL2xAovaE+s8II+UUkmk25WA1O/NdZvaZamKOjzzjvv7rvvLigoaN68+ezZs93TVXD48OEgMgxlZWWlpaUZhszMTI6TJ0+ucEG6UJSbFeHrr79u3bp1wpAMcY3qiaFDh6qD4tChQ65Fupxyyikc6QLHZ599dtmyZa5FulR372JJeXl5Xl6edDBu3Dg07Vocy3loGCgnMOJD6KSZGCeffLJrWnuYJ5deeqmbG0LVo0aNysnJsVIWrl210FrKoaIg0tOUhbz66quFhYVYcsm8efMGDhzoWqTLSSedZNM9evTYv39/5GSdaHKCZniOHDkSmHFdtWpVs2bNHIOdO3dyu/G+doy7dOmisZSIg3D4t2/fnpubq/zi4mKuSimLlGhW1AouoSLaH/XNwjWtGkq47bbbTjvttMD0gqL++ecfWi59O5Z0nD5yu0jv3r27qqWjVg0QQ4YMCUyPKJxiK9eeNqmbGG/kojRg/fr1c08Hwd9//92iRQs0jVmHDh1+++03O2bStH6OHTv2888/V/611157/vnnk3jsscd+/vlnltERI0bs2LFj5MiRXIL9rFmzioqKDh482Lt3bzSkzIceeggbrurWrRunSLRp02bv3r3lhm+++WbdunWBiXZYAVQ1MxBL6Xjx4sVqAJNQaqNHBw4cQKC7du1Cgmefffatt96qFkbhFJpW1ES8VFmR0rqkJvr27bto0SKdXb9+PWEPrZoxYwY2Mh4/fvy2bds4O2jQoAULFpBYs2ZNu3btDhu0lOnyxx9/fPXq1YER9MKFC1MukmnT5AStwePI/c3Ozq7KN6BpQogpU6bk5+cHxq8HkWslxyuuuKKkpITlctKkSQzY1q1blf/7778TNnBKRZHz1VdftWrVSisDKyyCZiw/+ugjBBeYSSKBSkOqjsyHH3548+bN0UpJIEQJOjCRaMIQhJG3fl555ZVMJBK33377TTfdpGY4jBkzhiYhJiJjlRaFHNqgMrlRN9xwQ9u2bW1LyGceYjB37lwJmra1bNmSs+pjYDrFVEHiukorIWkMOnfurBgDm2HDhnXt2jWsth5ocoKW88OJaiSCVCumcs444wxsUGe58ejyoEEYLcgRWjWo2IQJBiZMmLBy5UrpT6AbNnOo85Zbblm6dKkUQOHffvutqksaNZOJyKwnk3RefPFFpTFYu3Ytnl6qxU3i7JWmbVKMflqvjOK//PLLfxsRogZrRyvvmHJW79u37/TTTycxw2CVunHjRgIGFMlahK8tN7Px9ddfZ7kITFHqDoofMGAAV5HDXaIlymf9sXeeU9zDDz74QLe0XqiroBNme6G2uucaKwnjCPfs2ROEYnIMyHnllVcYMNJyPBKNzkqpOF0KSVQMZzUwF198scIVWyAyleLLwyDYtiFaAlfh2qOChqysrDvvvFOFE+QQhOhyRDZ16lTNok2bNlkP/eabbyIRlYBeWQ1sMwRTkSPrz9tvv/3CCy8899xz0bknqO7jjz9midBPFS4ILZYvX667oRbSYKbQH3/8EYThHMyfP19PkGRz2WWXKcEcjgpazl4/64WaCpoqmbIZFWlhoDNaItVijD/77DOG0C2icZAwKzLtxG2Q3rJli2NAR9DQxIkTozedpVMdlAHH/v3748KVo44njeYIXjMqbZ7IkYwCs9ZryHFOuKuE8QjElCS4b7g6mSWMww5MJMpNVu324QBpWoizV/5FF12E+BJmbiAdPV/jePXVV6sotVMQQBMMaNfL5ZMnT6Z5mmnWBrhLOOPA9BcDAqTA1PvMM8+wUMiGKRGYmIS1giBNmZ988gk1FhYWvvXWW/xE+sQVTDM1g8nZp08fFWWjmsTx99C6I1TPbsBmlpm9whdffKGzHOkMU19yt2aNCvwBfivDrLYs09HnR4J569xflDFt2rQgvAnKoYSOHTvK8qiWDfycM2eO9BEtQQ90cfbt27e3xjgCMmnAihUrVDJhCTnvvvtuYFaGwYMHk2CvqSiF9LnnnisD/WTLRY3Tp0//4YcfgrAZ9s4zVzUWdhOp/JdffllpZSaNrHHkSsiGceTmbNiwQZY9e/aMPg7SrWOaIWVNSKrQoOuRIpm6RVBcXEx0RHfee+89rh0+fDhpohEVhUHlB011oaayU8eo/vLLL7eZtLugoMCGHOwbOnXqxE+aaG9rk0JuVetV5VOV0V0NdXUU/SyPoMt1SjlMuehViXD6ycbB8bs1xDamemwDbGNSImP1xem+Y1N3aio7WqNwXquMcBpkm5Wbm9tkBS2sEGtC9DYek5T2tijVazdw6ZGocQDgtqNaqr+kYsHpU1PZ0UlCC2TKMmQznQbZZhF+NU1BJ427alBBpyRalD02BG7FtaH6EirWkz5uSG6LZpZHayLRq1cvNhPlZkktKSmRZFOOXF5eXnqCHj16tIKqarBPGxot9Tg8ntriyk6RTTShI/EG2xeF+doTQFWuKG1BB+HfFKrHvaZq9u/fz97FttxzouAOZI3598qoJ7bnoumtW7dSDVFHYPb4gwYNys/PT7n7Ceom6GS4aleDe43HE5JC0DYt6ej4xBNPoFG729Af6CHlJppNYeXHYcckaZ4Nu7mpiDbS44mSQtDOUYlOnTplRB6vloWk9NBsCtMQNGq2MXTzqvnrr78SFf9S4PFY/tsUSiJKyxPrb7CkE+bvtC1bttTZsopvMEZK+5f0BB3UYDslg/Lwj3Yej8N/kW40wKgscQSNk5aO7dmqVBWN66sxa7TQ4AEDBjQzf0eE+voUpVHBPsdul3v16lWPw0SB3bt3V3r9+vVp76bS4+hrIrYnih90lGqVHj58OGs9/ZfnrmpbNnjw4FatWukeYZ+ZmZmdnb1y5UrXrtGjRYkVqaioqLS0tH379m3btnWN0uKYX7W0bt1asZx7ogFgjP788086O3HixHbt2rmn04LSsrKypkyZIlHxs0uXLsenO+Lo7FHd0QkalWzSvERiI+ZazWPs7btjJxBJ8yZWmzZt9HPXrl3N6vV9g+pJGNzcWrJ79+758+dXM1g7duygU8nw/Q180KpVq+peb2Befd6zZ48c5TvvvPPhhx+6Fg3JfzF0dHsXddV1UaTGpprb2jihwWvXrh06dKh56l2+fPlylh2tThdccMGBAwcwGDFiBC5cwwZLlizJycnp0aOH7TLoRbaePXsG4eJ74YUX2hvy9NNP4yO7du36/fffB+alU9ZAhKhrdfPJ7Nu3r15kS5pAaNGiRXiWmTNnUtrevXujzY5iBW1xDN5//32WC/vYig6WlJQkwm8Np02bxmI7ZsyYsvBFHbj33nsxoz22kGHDhiHfqVOnjh07VreFZtMpe8nAgQPZxFeuveFIHd9EZ6q6FDlZC2zH3BONGxp83333rVu3ToJGOqNGjSJz+vTpDM+4ceNGjhxZZt7Bknz1DXPSqFzhil4iVd+VOGw+Q5o3b55Wufvvv//QoUMqf+fOnQnzJ6qMyAvW7FhQlW6dwlCF8rm5uXfccQdmGzdurPx5la4NaiBo5t4111wTGLdF755//nnZbNu2zUa9Ujz5NFvv3BKidO7cWZZMP5VcWFhoW47jf/DBB4NwYVdRlWtvOCoI2lZcXy1Qh+urtOMGY4NYkSnjwcYgelveeOMNvJF0rHzC6wkTJmgdQwFJ85URF/7000/Sq7UkU29pkqPvAzZs2GAVrBxbF77chnlWYdu3bz/rrLNU+8KFC/WOslC9+gtuhcechugbOCLDvLnKsXfv3kkjPtvITZs2kaCpTB61Vg2zbcO4oKBg9erVyrzuuuseeOAB9ZSp/uuvvwamPd999120R8eH1B66iYN/1WPHcrPuJ8P3OUnceOON+sxEQkyY9/RRTL9+/WzMiqWct+SokQaC8qSRjn6ygjPe+DwVNX78+EsuuUQlEFc89dRTEjTVqTGcogq97Zg0b8o7X/+rtUIeOlF1TEzVW7ZsSRixfvrpp0HoxTIMxDb6PCwwbz3k5eWVRTZ26rXmQNJ8drB06VL9JEayN+3JJ5+86qqr7FXHBy/oFKAtPXS3gkiEwaWcpSRoFSAbnLRyOCLxhIki7EwggGGAlWlPBWYLpaIoZ/bs2Sph0qRJy5Ytk6AfeeSRc845J2kmVYcOHWSgC5VISfWCptjm5mtCDPr06UMUoUYG5nGe7Vpg+sJSM3r0aOduZJi/suk+2M2lehFWcvQbhblz56oQm9nQeEGngKW2W7duGjDlSIJBKkEzbFrQUQn7yMB4SplhkJ+fzwpOAs/Klj8wS/nNN9+sQjhmZWWpHC5ZsWLFggULKAcPjXFZGG+sWbMmKhcu/OWXX1AkBsXFxWqhgxV0MtW7McyWu+66KzAtnDVrFi7Wbv1tyw8ePLh48WKM9+3bZ7/qOPXUU/XpGiImnwbQQX12+dJLLyF9pYnKAjPlfvzxR32octzwgnZZsmSJll0GzLoWyYJRx0dKE1Gv079//+uvvx7ZyRI2b97csWNH9ojWBs4880xsuBZxd+/enSqGDBliRYYgcnJybOGvvfYaklUJyiSRmZmpKjjec889aMWecigtLWUnF22kRf9MA4hqkuGnoihV9RYVFSFffbBtL6Go7OzsOXPmBGa6HjEwDRA9P4krHn30UdWFv2cqKs2mVv+r5HjiBV07JCCNvXuu9kQnTDJ0pUpXJmFWiWSN67UhgUO0/Tqmhy1KuKf/T3hB1xqrEvdE3YhI7ti4F1ciGQa1lY1TZsYGL+hac6Ko4URpZ/3iBe2JFV7QnljhBe2JFV7QnljhBe2JFV7QnljhBe2JFV7QnljhBe2JFV7QnljhBe2JFV7QnljhBe2JFV7QnljxP7JFH1vTq+X6AAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,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>
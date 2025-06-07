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
   * **Proses**: Dilakukan pengecekan dan penghapusan data duplikat pada:
      - `df_tourism`: Dilakukan pengecekan duplikat pada data destinasi wisata. Hasilnya, tidak ditemukan adanya baris data yang identik.
      - `df_rating`: Ditemukan dan dihapus sebanyak 79 baris data rating yang duplikat.
      - `df_user`: Dilakukan pengecekan duplikat berdasarkan kolom User_Id untuk memastikan setiap pengguna terdaftar hanya satu kali. Hasilnya, tidak ditemukan adanya User_Id yang duplikat.  
   * **Alasan**: Menjamin setiap interaksi setiap data bersifat unik dan meningkatkan kualitas data input untuk model.  
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

#### **1\. Content-Based Filtering (CBF)**

Untuk model *Content-Based Filtering* (CBF), evaluasi performa dapat dilakukan secara kuantitatif dengan metrik klasifikasi standar seperti **Precision**, **Recall**, dan **F1-Score**. Metrik ini mengukur kemampuan model dalam merekomendasikan item yang relevan berdasarkan histori pengguna. 

##### **Metrik Evaluasi Kuantitatif:**

* **Precision**  
  Metrik ini menjawab pertanyaan, "Dari semua tempat yang direkomendasikan, berapa persen yang benar-benar relevan bagi pengguna?" Precision berfokus pada kualitas dari rekomendasi yang diberikan.

  **Formula**  
  ![Formula Precision](https://images.prismic.io/encord/ccd903d0-3d97-4d9a-b6b7-7c31773e4676_Precision+-+Mathematical+Formula+-+Encord.png?auto=compress,format)

  **True Positives (TP):** Jumlah tempat yang direkomendasikan dan benar-benar disukai pengguna.  
  **False Positives (FP):** Jumlah tempat yang direkomendasikan namun tidak disukai pengguna.  

* **Recall**  
  Metrik ini menjawab pertanyaan, "Dari semua tempat yang seharusnya direkomendasikan, berapa persen yang berhasil ditemukan oleh model?" Recall berfokus pada cakupan atau kelengkapan dari rekomendasi.

  **Formula**  
  ![Formula Recall](https://images.prismic.io/encord/3c0173c9-409e-4f84-a53f-7073ea00bca9_Recall+-+Mathematical+Formula+-+Encord.png?auto=compress,format)

  **True Positives (TP):** Jumlah tempat yang direkomendasikan dan benar-benar disukai pengguna.  
  **False Positives (FP):** Jumlah tempat yang direkomendasikan namun tidak disukai pengguna.  
  **False Negatives (FN):** Jumlah tempat yang disukai pengguna namun tidak berhasil direkomendasikan oleh model. 

* **F1-Score**  
  Ini adalah rata-rata harmonik dari Precision dan Recall. Metrik ini berguna untuk mencari keseimbangan antara Precision dan Recall, terutama jika terjadi kondisi di mana salah satu metrik sangat tinggi sementara yang lain sangat rendah.

  **Formula**   
  ![Formula F1](https://images.prismic.io/encord/0ef9c82f-2857-446e-918d-5f654b9d9133_Screenshot+%2849%29.png?auto=compress,format)

##### **Hasil Metrik Kuantitatif**  
Berdasarkan hasil eksekusi pada *notebook*, diperoleh nilai metrik sebagai berikut:

* **Rata-rata Precision:** **0.0354**  
* **Rata-rata Recall:** **0.0936**  
* **F1-Score:** **0.0514**

##### **Analisis Kualitatif (Relevansi Hasil):**   
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

#### **2\. Collaborative Filtering (CF)**

Model *Collaborative Filtering* (CF) pada proyek ini dilatih untuk memprediksi rating, sehingga kinerjanya diukur secara kuantitatif menggunakan metrik evaluasi untuk masalah regresi.  

**Metrik yang Digunakan** yaitu **Root Mean Squared Error (RMSE)** yang digunakan untuk mengevaluasi sistem rekomendasi yang memprediksi rating karena kemampuannya memberikan bobot lebih pada kesalahan yang besar.

  **Formula RMSE**  
  ![Formula RMSE](https://miro.medium.com/v2/resize:fit:966/1*lqDsPkfXPGen32Uem1PTNg.png)
  
  **n** adalah jumlah total data pada set validasi.  
  **∑** adalah simbol sigma yang berarti "jumlah total dari".  
  **yi**​ adalah nilai rating aktual yang diberikan pengguna untuk item ke-i.  
  **y^​i**​ adalah nilai rating yang diprediksi oleh model untuk item ke-i.  
  **(yi​−y^​i​)2** adalah kuadrat dari selisih (error) antara rating aktual dan prediksi.  

  **Cara Kerja dan Interpretasi**  
  RMSE bekerja dengan cara menghitung selisih (error) untuk setiap prediksi, mengkuadratkannya, menghitung rata-ratanya, lalu meng-akarkannya kembali. Langkah **pengkuadratan** adalah kunci: ini membuat error yang lebih besar memiliki dampak yang jauh lebih signifikan terhadap skor akhir dibandingkan error kecil. Dengan kata lain, model akan "dihukum" lebih berat jika membuat satu prediksi yang sangat salah daripada membuat beberapa prediksi yang sedikit salah.  
  **Semakin rendah nilai RMSE, semakin baik kinerja model** karena ini menandakan bahwa prediksi model secara rata-rata lebih dekat dengan nilai rating yang sebenarnya.

##### **Hasil Metrik Evaluasi**  
Berdasarkan proses pelatihan di *notebook* (epoch ke-100), diperoleh nilai metrik pada data validasi sebagai berikut:

* **Final Validation RMSE:** **0.3836**  
* **Final Validation Loss:** **0.7558**

Nilai RMSE yang rendah ini menunjukkan performa model yang baik dalam memprediksi rating pengguna pada data yang belum pernah dilihat sebelumnya. Hasil visualisasi kurva pembelajaran pada *notebook* juga mengonfirmasi bahwa model tidak mengalami *overfitting*.
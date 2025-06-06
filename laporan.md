# **Laporan Proyek Machine Learning \- Kunti Najma Jalia**

### **Domain Proyek \- Sistem Rekomendasi Destinasi Wisata di Yogyakarta**

Yogyakarta merupakan salah satu destinasi pariwisata terkemuka di Indonesia yang menawarkan berbagai jenis atraksi (Suhailah & Hartatik, 2023). Pariwisata bahkan telah menjadi salah satu kebutuhan mendasar bagi masyarakat di era modern (Pakarti & Wardani, 2022). Daya tarik Kota Yogyakarta sebagai destinasi wisata unggulan terus meningkat, yang dibuktikan dengan data kunjungan wisatawan yang mencapai 9,5 juta orang hingga akhir November 2024\. Pemerintah Kota Yogyakarta bahkan optimis angka ini akan menembus 10 juta kunjungan pada akhir tahun (Adminwarta, 2024).

Seiring dengan kemajuan teknologi, wisatawan semakin bergantung pada internet untuk merencanakan perjalanan mereka. Mesin pencari seperti Google dan media sosial menjadi alat utama untuk mencari rekomendasi objek wisata (Pratiwi & Nada, 2022). Namun, ledakan informasi digital ini menimbulkan tantangan baru. Wisatawan seringkali dihadapkan pada daftar pilihan yang sangat banyak, kompleks, dan membutuhkan waktu untuk diseleksi (Musyrifah et al., 2022). Informasi yang disajikan seringkali acak dan tidak memuat detail yang lengkap, sehingga menyulitkan wisatawan untuk memilih destinasi yang paling sesuai dengan preferensi dan minat mereka (Sispianygala et al., 2024). Terlebih lagi, banyak aplikasi pariwisata yang ada saat ini hanya berfokus pada penyajian informasi lokasi tanpa memiliki fitur rekomendasi yang memadai (Hendrawan et al., 2022).

Untuk mengatasi masalah kelebihan informasi (*information overload*) tersebut, diperlukan sebuah solusi cerdas yang mampu menjembatani antara banyaknya pilihan destinasi dengan preferensi unik setiap pengguna. Sistem rekomendasi menjadi komponen krusial dalam platform pariwisata modern untuk membantu pengguna mengambil keputusan. Konsep *Smart Tourism* juga menekankan pentingnya pengembangan sarana dan kemampuan informasi untuk memfasilitasi inovasi produk dan meningkatkan pengalaman wisata (Hendrawan et al., 2022). Dengan memanfaatkan *machine learning*, sistem dapat dibangun untuk memberikan rekomendasi berdasarkan data historis seperti peringkat (rating) yang diberikan pengguna (Pratiwi & Nada, 2022).

Proyek ini bertujuan untuk mengembangkan dan membandingkan dua pendekatan utama dalam sistem rekomendasi, yaitu *Content-Based Filtering* dan *Collaborative Filtering* (Musyrifah et al., 2022). Metode *Collaborative Filtering*, khususnya varian *Item-based*, bekerja dengan menemukan pola dari item-item yang telah dinilai oleh banyak pengguna untuk merekomendasikan item serupa lainnya (Mi'roj, 2023). Sementara itu, metode *Content-Based Filtering* memberikan rekomendasi dengan menganalisis karakteristik atau konten dari item itu sendiri yang relevan dengan pilihan pengguna sebelumnya (Musyrifah et al., 2022). Dengan menerapkan kedua model ini, sistem rekomendasi tempat wisata di Yogyakarta diharapkan dapat memberikan saran yang lebih personal dan relevan, membantu pengguna membuat keputusan yang lebih baik dan cepat.

### **Referensi**

* Adminwarta. 2024\. *Target Kunjungan Wisatawan ke Yogyakarta Tahun 2024 Diyakini Terlampaui*. URL: [https://warta.jogjakota.go.id/detail/index/37070](https://warta.jogjakota.go.id/detail/index/37070). Diakses pada 7 Juni 2025\.  
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

### **Data Preparation**

Tahapan persiapan data merupakan fase krusial dalam pengembangan model *machine learning*. Prinsip *‘garbage in, garbage out’* sangat berlaku di sini, yang berarti kualitas model sangat bergantung pada kualitas data yang digunakan untuk melatihnya. Oleh karena itu, sebelum data dimasukkan ke dalam model, perlu dilakukan serangkaian proses untuk membersihkan, mentransformasi, dan menstrukturkan data agar menjadi format yang optimal. Tahapan ini bertujuan untuk memastikan data yang digunakan bersih dari inkonsistensi, relevan dengan masalah yang akan diselesaikan, dan siap untuk diproses oleh algoritma *machine learning*, sehingga pada akhirnya dapat menghasilkan model rekomendasi yang akurat dan andal.

Langkah-langkah persiapan data yang dilakukan dalam proyek ini adalah sebagai berikut:

1. **Penanganan Duplikat**:  
   * **Proses:** Dilakukan pengecekan dan penghapusan data duplikat pada `df_rating`. Ditemukan dan dihapus sebanyak 79 baris data yang identik.  
   * **Alasan:** Menjamin setiap interaksi rating bersifat unik dan meningkatkan kualitas data input untuk model.  
2. **Filtering Data Yogyakarta**:  
   * **Proses:** `df_tourism` difilter untuk hanya menyisakan baris dengan `City` berisi 'Yogyakarta'. Hasilnya, diperoleh dataframe baru (`df_tourism_yogya`) dengan 126 destinasi.  
   * **Alasan:** Memfokuskan cakupan proyek agar sesuai dengan tujuan.  
3. **Rekayasa Fitur untuk CBF**:  
   * **Proses:** Kolom `Place_Name`, `Category`, dan `Description` dari dataframe yang telah difilter digabungkan menjadi satu fitur tunggal bernama `content_features`. Fitur ini kemudian diproses menggunakan Sastrawi.  
   * **Alasan:** Membuat sebuah representasi teks yang komprehensif untuk setiap item wisata.  
4. **Persiapan Data untuk CF**:  
   * **Proses:** `User_Id` dan `Place_Id` pada data rating Yogyakarta diubah menjadi indeks numerik (encoding). `Place_Ratings` dinormalisasi ke skala 0-1. Dataset kemudian diacak dan dibagi menjadi 80% data latih dan 20% data validasi.  
   * **Alasan:** Menyiapkan data untuk input model *neural network*.

### **Modeling and Result**

Pada tahap ini, dikembangkan dua sistem rekomendasi dengan algoritma yang berbeda untuk menyelesaikan permasalahan yang telah diidentifikasi. Setiap model dijelaskan dari cara kerja, kelebihan, kekurangan, hingga output yang dihasilkan berupa top-N recommendation.

#### **1\. Solusi dengan Content-Based Filtering (CBF)**

Pendekatan ini dibuat untuk menjawab **pernyataan masalah pertama**: *Bagaimana cara merekomendasikan tempat-tempat wisata yang memiliki karakteristik serupa kepada pengguna?*

**Penjelasan Sistem Rekomendasi:** Sistem *Content-Based Filtering* bekerja dengan cara menemukan kemiripan antar item (tempat wisata) berdasarkan atribut atau kontennya. Dalam proyek ini, konten yang digunakan adalah gabungan dari nama, kategori, dan deskripsi tempat wisata. Prosesnya adalah sebagai berikut:

1. **Ekstraksi Fitur Teks:** Setiap tempat wisata direpresentasikan sebagai gabungan teks dari fitur-fiturnya.  
2. **Vektorisasi TF-IDF:** Teks tersebut diubah menjadi vektor numerik menggunakan **Term Frequency-Inverse Document Frequency (TF-IDF)**. Teknik ini memberi bobot tinggi pada kata-kata yang penting untuk sebuah tempat wisata tetapi jarang muncul di tempat lain.  
3. **Perhitungan Kemiripan:** **Cosine Similarity** digunakan untuk mengukur kemiripan antara vektor-vektor tempat wisata. Skor kemiripan berkisar antara 0 (tidak mirip) hingga 1 (sangat mirip).

**Menyajikan Top-N Recommendation:** Setelah matriks kemiripan dibuat, sistem dapat memberikan rekomendasi. Ketika pengguna memilih satu tempat wisata sebagai referensi, model akan mencari N tempat lain dengan skor *cosine similarity* tertinggi terhadap tempat tersebut. Outputnya adalah daftar **Top-5 tempat wisata** yang paling mirip, diurutkan dari yang paling relevan.

**Kelebihan dan Kekurangan:**

* **Kelebihan:**  
  * Tidak memerlukan data rating dari pengguna lain, sehingga tidak mengalami masalah *cold start* untuk item baru.  
  * Rekomendasi bersifat transparan karena didasarkan pada fitur item yang jelas.  
  * Mampu merekomendasikan item yang kurang populer selama fiturnya relevan.  
* **Kekurangan:**  
  * Rekomendasi cenderung kurang beragam (*serendipity* rendah) karena hanya menyarankan item yang mirip.  
  * Kualitas rekomendasi sangat bergantung pada kelengkapan dan kualitas deskripsi fitur item.

#### **2\. Solusi dengan Collaborative Filtering (CF)**

Pendekatan ini dirancang untuk menjawab **pernyataan masalah kedua**: *Bagaimana cara memberikan rekomendasi tempat wisata yang bersifat personal berdasarkan pola rating pengguna lain?*

**Penjelasan Sistem Rekomendasi:** Sistem *Collaborative Filtering* bekerja dengan mengidentifikasi pola dari data interaksi pengguna-item (dalam hal ini, rating). Model ini mengasumsikan bahwa jika seorang pengguna memiliki selera yang sama dengan pengguna lain (misalnya, sama-sama menyukai Candi Prambanan dan Malioboro), maka ia juga kemungkinan akan menyukai tempat lain yang disukai oleh pengguna tersebut. Dalam proyek ini, digunakan pendekatan *deep learning*:

1. **Embedding Layer:** Pengguna dan tempat wisata masing-masing dipetakan ke dalam vektor berdimensi rendah yang disebut *embedding*. Vektor ini menangkap preferensi laten pengguna dan karakteristik laten item.  
2. **Prediksi Rating:** Model dilatih untuk mempelajari vektor *embedding* ini. Untuk memprediksi rating, model akan mengambil vektor pengguna dan vektor tempat wisata, lalu menghitung *dot product* di antara keduanya.  
3. **Pelatihan:** Model dilatih dengan data rating yang ada untuk meminimalkan *error* (diukur dengan RMSE), sehingga prediksi ratingnya semakin akurat.

**Menyajikan Top-N Recommendation:** Untuk seorang pengguna, model akan memprediksi rating untuk semua tempat wisata yang belum pernah ia kunjungi. Berdasarkan prediksi rating tersebut, sistem akan mengurutkannya dari yang tertinggi ke terendah dan menyajikan **Top-5 tempat wisata** sebagai rekomendasi personal.

**Kelebihan dan Kekurangan:**

* **Kelebihan:**  
  * Mampu menemukan fitur-fitur yang kompleks dan tak terduga (*serendipity* tinggi) karena tidak bergantung pada konten item.  
  * Rekomendasi bersifat sangat personal dan dapat beradaptasi dengan perubahan selera pengguna.  
* **Kekurangan:**  
  * Mengalami masalah *cold start*: tidak bisa memberikan rekomendasi untuk pengguna atau item baru yang belum memiliki data rating.  
  * Membutuhkan data historis interaksi pengguna-item dalam jumlah yang cukup besar untuk bisa bekerja dengan baik.

### **Evaluation**

Evaluasi performa model dilakukan dengan pendekatan yang berbeda untuk setiap jenis sistem rekomendasi, sesuai dengan sifat dan tujuan masing-masing model.

#### **1\. Content-Based Filtering**

Model *Content-Based Filtering* dievaluasi menggunakan dua pendekatan, yaitu kualitatif dan kuantitatif, untuk memberikan gambaran yang komprehensif mengenai kinerjanya.

1. **Pendekatan Kualitatif (Analisis Relevansi):**  
   **Cara Kerja:** Evaluasi ini dilakukan dengan memberikan satu item referensi kepada model dan mengamati 5 item teratas yang direkomendasikan. Kualitas rekomendasi dinilai berdasarkan **relevansi** antara item referensi dengan item yang direkomendasikan. Relevansi diukur secara subjektif dengan memeriksa apakah item-item yang disarankan memiliki kategori atau tema yang serupa dan masuk akal.  
2. **Pendekatan Kuantitatif (Analisis Skor Kemiripan):**  
   **Metrik yang Digunakan yaitu** **Cosine Similarity Score**. Metrik ini secara inheren merupakan bagian dari model, namun skor yang dihasilkannya dapat dianalisis untuk evaluasi.  
   **Cara Kerja dan Interpretasi:** Skor *Cosine Similarity* mengukur kosinus sudut antara dua vektor TF-IDF, yang merepresentasikan kemiripan konten antara dua tempat wisata. Nilai skor ini berkisar dari 0 (tidak ada kemiripan) hingga 1 (sangat mirip). Dalam konteks evaluasi, skor ini berfungsi sebagai ukuran kuantitatif dari seberapa “yakin” model terhadap rekomendasinya. Skor kemiripan yang tinggi (misalnya, di atas 0.15 dalam proyek ini) pada rekomendasi teratas menunjukkan bahwa model berhasil menemukan item-item dengan karakteristik tekstual yang sangat relevan.

#### **2\. Collaborative Filtering (Evaluasi Kuantitatif)**

Model *Collaborative Filtering* pada proyek ini dilatih untuk memprediksi rating yang akan diberikan pengguna. Oleh karena itu, kinerjanya dapat diukur secara kuantitatif menggunakan metrik evaluasi untuk masalah regresi. Metrik utama yang digunakan adalah **Root Mean Squared Error (RMSE)**.

* **Formula RMSE:** `RMSE=n1​∑i=1n​(yi​−y^​i​)2​Di` mana:  
  * adalah jumlah total data.  
  * yi​ adalah nilai rating aktual.  
  * y^​i​ adalah nilai rating yang diprediksi oleh model.  
* **Cara Kerja dan Interpretasi:**  
  * RMSE mengukur rata-rata magnitudo dari kesalahan prediksi (selisih antara rating aktual dan prediksi).  
  * Dengan mengkuadratkan selisih (yi​−y^​i​), metrik ini memberikan bobot yang lebih besar pada kesalahan yang besar. Ini berarti model akan "dihukum" lebih berat jika melakukan prediksi yang sangat jauh dari nilai sebenarnya.  
  * Karena diakarkan, nilai RMSE memiliki satuan yang sama dengan variabel target (dalam kasus ini, rating yang telah dinormalisasi), sehingga lebih mudah untuk diinterpretasikan.  
  * **Semakin rendah nilai RMSE, semakin baik kinerja model** karena ini menandakan bahwa prediksi model secara rata-rata lebih dekat dengan nilai rating yang sebenarnya. Dalam proyek ini, RMSE pada data training dan validasi dipantau di setiap epoch untuk melihat sejauh mana model belajar dan untuk mendeteksi *overfitting*.

### **Hasil Proyek**

#### **Hasil Model Content-Based Filtering**

Saat model diberi input **'Taman Pintar Yogyakarta'**, 5 rekomendasi teratas yang dihasilkan adalah:

| **Place\_Id** | **Place\_Name** | **Category** | **Rating** | **similarity\_score** |
| ----- | ----- | ----- | ----- | ----- |
| 206 | Wisata Kaliurang | Cagar Alam | 4.4 | 0.192158 |
| 98 | Taman Pelangi Yogyakarta | Taman Hiburan | 4.3 | 0.148100 |
| 90 | Kampung Wisata Taman Sari | Taman Hiburan | 4.6 | 0.147447 |
| 203 | Galaxy Waterpark Jogja | Taman Hiburan | 4.3 | 0.147205 |
| 100 | Taman Budaya Yogyakarta | Budaya | 4.5 | 0.140009 |

**Analisis:** Rekomendasi yang diberikan cukup relevan, sebagian besar adalah "Taman Hiburan" atau "Cagar Alam," yang sesuai dengan karakteristik 'Taman Pintar'.

#### **Hasil Model Collaborative Filtering**

Metrik evaluasi pada data validasi di akhir pelatihan adalah:

* **Final Validation RMSE:** **0.3674**  
* **Final Validation Loss:** **0.7276**

Visualisasi proses pelatihan menunjukkan bahwa model berhasil belajar dengan baik. Untuk **User ID 1**, 5 rekomendasi teratas yang dihasilkan adalah:

| **Place\_Id** | **Place\_Name** | **Category** | **Rating** | **Predicted\_Normalized\_Rating** |
| ----- | ----- | ----- | ----- | ----- |
| 139 | Puncak Gunung Api Purba \- Nglanggeran | Cagar Alam | 4.7 | 0.769608 |
| 138 | Jogja Exotarium | Taman Hiburan | 4.4 | 0.730769 |
| 132 | Air Terjun Kedung Pedut | Cagar Alam | 4.5 | 0.723506 |
| 134 | Desa Wisata Gamplong | Taman Hiburan | 4.4 | 0.712936 |
| 136 | Grojogan Watu Purbo Bangunrejo | Taman Hiburan | 4.5 | 0.710067 |

**Analisis:** Model ini merekomendasikan tempat-tempat populer yang mungkin disukai oleh User ID 1 berdasarkan selera pengguna lain, menunjukkan kemampuannya memberikan rekomendasi personal.
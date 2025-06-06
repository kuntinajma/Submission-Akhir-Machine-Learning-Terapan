# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from IPython.display import display
import pickle
import os
import warnings

# Membuat direktori untuk menyimpan plot
plot_dir = 'plot'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)
    print(f"Folder '{plot_dir}' berhasil dibuat.")

warnings.filterwarnings('ignore')

print("=================== Import Library ==============")
print("Semua library yang dibutuhkan telah di-import.")

print("\n=================== Definisi Fungsi dan Kelas ==============")
print("=================== Inisialisasi Variabel Global ==============")
results = {}
MODEL_CF_SUCCESS = False
MODEL_CBF_SUCCESS = False
top_5_recs_cbf = pd.DataFrame()
top_5_recs_cf_keras = pd.DataFrame()
print("Variabel global telah diinisialisasi.")

print("\n=================== Fungsi untuk Preprocessing Teks (Sastrawi) ==============")
def preprocess_text_sastrawi(text, stemmer, stopword_remover):
    if pd.isna(text) or text.strip() == '': return ''
    text = text.lower()
    text_stemmed = stemmer.stem(text)
    text_cleaned = stopword_remover.remove(text_stemmed)
    return text_cleaned
print("Fungsi untuk Preprocessing telah berhasil didefinisikan")

print("\n=================== Kelas Model Collaborative Filtering (RecommenderNet) ==============")
class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_places, embedding_size=50, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.user_embedding = layers.Embedding(num_users, embedding_size, embeddings_initializer='he_normal', embeddings_regularizer=keras.regularizers.l2(1e-6))
        self.user_bias = layers.Embedding(num_users, 1)
        self.place_embedding = layers.Embedding(num_places, embedding_size, embeddings_initializer='he_normal', embeddings_regularizer=keras.regularizers.l2(1e-6))
        self.place_bias = layers.Embedding(num_places, 1)
    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:, 0])
        user_bias_vec = self.user_bias(inputs[:, 0])
        place_vector = self.place_embedding(inputs[:, 1])
        place_bias_vec = self.place_bias(inputs[:, 1])
        dot_user_place = tf.tensordot(user_vector, place_vector, 2)
        x = dot_user_place + user_bias_vec + place_bias_vec
        return tf.nn.sigmoid(x)
print("Kelas RecommenderNet telah berhasil didefinisikan")

print("\n=================== Fungsi untuk Mendapatkan Rekomendasi ==============")
def get_content_based_recommendations(place_id_ref, n=5, cosine_sim_matrix_param=None, tourism_df_param=None, id_to_idx_map_param=None):
    if cosine_sim_matrix_param is None or tourism_df_param is None or id_to_idx_map_param is None:
        return "Model CBF belum siap."
    if place_id_ref not in id_to_idx_map_param:
        place_name_matches = tourism_df_param[tourism_df_param['Place_Name'] == place_id_ref]
        if not place_name_matches.empty:
            place_id_ref_from_name = place_name_matches['Place_Id'].iloc[0]
            if place_id_ref_from_name in id_to_idx_map_param: idx = id_to_idx_map_param[place_id_ref_from_name]
            else: return f"ID Tempat (dari nama) '{place_id_ref_from_name}' tidak ditemukan di map."
        else: return f"ID Tempat atau Nama '{place_id_ref}' tidak ditemukan."
    else: idx = id_to_idx_map_param[place_id_ref]
    sim_scores = list(enumerate(cosine_sim_matrix_param[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    place_indices = [i[0] for i in sim_scores]
    recommendations_df = tourism_df_param.iloc[place_indices][['Place_Id', 'Place_Name', 'Category', 'Rating']].copy()
    recommendations_df['similarity_score'] = [s[1] for s in sim_scores]
    return recommendations_df

def get_top_n_recommendations_keras_cf(user_real_id, n=5, model=None, tourism_df_all_yogya=None, rating_df_yogya_cf=None, mappings=None):
    if model is None or mappings is None:
        return "Model CF belum siap."
    user_to_user_encoded_cf = mappings['user_to_user_encoded']
    place_to_place_encoded_cf = mappings['place_to_place_encoded']
    place_encoded_to_place_cf = mappings['place_encoded_to_place']
    user_enc = user_to_user_encoded_cf.get(user_real_id)
    if user_enc is None: return "User ID tidak ditemukan dalam data training CF."
    all_place_ids_yogya = tourism_df_all_yogya['Place_Id'].unique()
    place_ids_in_cf_model_list = list(place_to_place_encoded_cf.keys())
    rated_items_by_user = rating_df_yogya_cf[rating_df_yogya_cf['User_Id'] == user_real_id]['Place_Id'].unique()
    candidate_items_for_prediction = [pid for pid in all_place_ids_yogya if pid in place_ids_in_cf_model_list and pid not in rated_items_by_user]
    if not candidate_items_for_prediction: return pd.DataFrame(columns=['Place_Id', 'Place_Name', 'Category', 'Rating', 'Predicted_Normalized_Rating'])
    place_encoded_candidates = [place_to_place_encoded_cf[pid] for pid in candidate_items_for_prediction]
    user_place_array = np.array([[user_enc, place_enc] for place_enc in place_encoded_candidates])
    predictions_normalized = model.predict(user_place_array, verbose=0).flatten()
    top_indices = predictions_normalized.argsort()[-n:][::-1]
    recommended_original_place_ids = [place_encoded_to_place_cf[place_encoded_candidates[i]] for i in top_indices]
    recommendations_df = tourism_df_all_yogya[tourism_df_all_yogya['Place_Id'].isin(recommended_original_place_ids)][['Place_Id', 'Place_Name', 'Category', 'Rating']].copy()
    pred_map = {place_encoded_to_place_cf[place_encoded_candidates[i]]: predictions_normalized[i] for i in top_indices}
    recommendations_df['Predicted_Normalized_Rating'] = recommendations_df['Place_Id'].map(pred_map)
    return recommendations_df.sort_values('Predicted_Normalized_Rating', ascending=False)
print("Fungsi untuk Mendapatkan Rekomendasi telah berhasil didefinisikan.")

print("\n=================== Data Understanding ==============")
print("=================== Memuat Dataset ==============")
df_tourism_raw = pd.read_csv('dataset/tourism_with_id.csv')
df_rating_raw = pd.read_csv('dataset/tourism_rating.csv')
df_user_raw = pd.read_csv('dataset/user.csv')
print("File CSV berhasil dimuat dari folder 'dataset/'.")

print("\n=================== Membuat Salinan ==============")
df_tourism = df_tourism_raw.copy()
df_rating = df_rating_raw.copy()
df_user = df_user_raw.copy()
print("DataFrame berhasil dicopy untuk mengantisipasi data oroginal masih tersimpan rapi.")

print("\n=================== Informasi Umum dan Variabel Dataset ==============")
print("=================== df_tourism (Tempat Wisata) ==============")
print("Info Detail Variabel (df_tourism):")
df_tourism.info()
print("\nContoh Data Awal (df_tourism):")
print(df_tourism.head(3))
print("\nContoh Data Akhir (df_tourism):")
print(df_tourism.tail(3))
print("\nStatistik Deskriptif Harga (Price) dan Rating Publik (Rating) pada df_tourism:")
print(df_tourism[['Price', 'Rating']].describe())
print("\nCek nilai null di df_tourism:")
print(df_tourism.isnull().sum().to_frame(name='jumlah_null'))

print("\n=================== df_rating (Rating Pengguna) ==============")
print("Info Detail Variabel (df_rating):")
df_rating.info()
print("\nContoh Data Awal (df_rating):")
print(df_rating.head(3))
print("\nContoh Data Akhir (df_rating):")
print(df_rating.tail(3))
print("\nStatistik Deskriptif Rating Pengguna (Place_Ratings) pada df_rating:")
print(df_rating['Place_Ratings'].describe().to_frame(name='statistik_place_ratings'))
print("\nCek nilai null di df_rating:")
print(df_rating.isnull().sum().to_frame(name='jumlah_null'))

print("\n=================== df_user (Pengguna) ==============")
print("Info Detail Variabel (df_user):")
df_user.info()
print("\nContoh Data Awal (df_user):")
print(df_user.head(3))
print("\nContoh Data Akhir (df_user):")
print(df_user.tail(3))
print("\nStatistik Deskriptif Usia (Age) pada df_user:")
print(df_user['Age'].describe().to_frame(name='statistik_usia'))
print("\nCek nilai null di df_user:")
print(df_user.isnull().sum().to_frame(name='jumlah_null'))

print("\n=================== Univariate Exploratory Data Analysis (EDA) ==============")
print("=================== Distribusi Sebaran Rating Pengguna ==============")
most_frequent_rating = df_rating['Place_Ratings'].mode()[0]
rating_counts = df_rating['Place_Ratings'].value_counts().reset_index()
rating_counts.columns = ['Rating', 'Jumlah']
print(rating_counts.sort_values(by='Rating').to_string(index=False))
plt.figure(figsize=(8, 5))
sns.countplot(x='Place_Ratings', data=df_rating, palette='viridis', order=sorted(df_rating['Place_Ratings'].unique()))
plt.title('Distribusi Rating Pengguna (Keseluruhan Dataset)')
plt.savefig(os.path.join(plot_dir, 'distribusi_rating_pengguna.png'))
print(f"Insight: Visualisasi menunjukkan rating yang paling sering diberikan oleh pengguna adalah {most_frequent_rating}.")
print(f"Visualisasi 'Distribusi Rating Pengguna' disimpan di folder '{plot_dir}'.")


print("\n=================== Distribusi Sebaran Destinasi Berdasarkan Kota ==============")
top_cities = df_tourism['City'].value_counts().nlargest(5).reset_index()
top_cities.columns = ['Kota', 'Jumlah Tempat Wisata']
print(top_cities.to_string(index=False))
plt.figure(figsize=(10, 5))
sns.barplot(x='Kota', y='Jumlah Tempat Wisata', data=top_cities, palette='mako')
plt.title('Top 5 Kota dengan Jumlah Tempat Wisata Terbanyak')
plt.savefig(os.path.join(plot_dir, 'distribusi_destinasi_kota.png'))
print(f"Insight: Berdasarkan data, 5 kota dengan destinasi wisata terbanyak adalah {top_cities['Kota'].tolist()}. Ini menegaskan bahwa fokus dataset adalah pada pusat-pusat pariwisata utama di Indonesia, dengan {top_cities['Kota'].iloc[0]} memiliki jumlah terbanyak yaitu {top_cities['Jumlah Tempat Wisata'].iloc[0]} destinasi.")
print(f"Visualisasi 'Top 5 Kota' disimpan di folder '{plot_dir}'.")

print("\n=================== Distribusi Sebaran Destinasi Berdasarkan Kategori ==============")
top_categories_all = df_tourism['Category'].value_counts().nlargest(5).reset_index()
top_categories_all.columns = ['Kategori', 'Jumlah Tempat Wisata']
print(top_categories_all.to_string(index=False))
plt.figure(figsize=(10, 5))
sns.barplot(x='Kategori', y='Jumlah Tempat Wisata', data=top_categories_all, palette='crest')
plt.title('Top 5 Kategori Tempat Wisata (Keseluruhan Dataset)')
plt.savefig(os.path.join(plot_dir, 'distribusi_destinasi_kategori.png'))
print(f"Insight: Kategori wisata paling populer di seluruh dataset adalah '{top_categories_all['Kategori'].iloc[0]}' dengan jumlah {top_categories_all['Jumlah Tempat Wisata'].iloc[0]} tempat.")
print(f"Visualisasi 'Top 5 Kategori' disimpan di folder '{plot_dir}'.")


print("\n=================== Distribusi Sebaran Usia Pengguna ==============")
age_counts = df_user['Age'].value_counts().reset_index()
age_counts.columns = ['Usia', 'Jumlah Pengguna']
print(age_counts.sort_values(by='Usia').to_string(index=False))
age_stats = df_user['Age'].describe()
age_median = int(age_stats['50%'])
age_q1 = int(age_stats['25%'])
age_q3 = int(age_stats['75%'])
plt.figure(figsize=(10, 6))
sns.histplot(data=df_user, x='Age', bins=20, kde=True, color='salmon')
plt.title('Distribusi Usia Pengguna')
plt.savefig(os.path.join(plot_dir, 'distribusi_usia_pengguna.png'))
print(f"Insight: Distribusi usia pengguna menunjukkan konsentrasi yang kuat antara usia {age_q1} hingga {age_q3} tahun, dengan median usia di sekitar {age_median} tahun.")
print(f"Visualisasi 'Distribusi Usia Pengguna' disimpan di folder '{plot_dir}'.")

print("\n=================== Data Preprocessing ==============")
print("=================== Pegecekan dan Penanganan Nilai Duplikat ==============")
jumlah_data_awal_tourism = len(df_tourism)
jumlah_duplikat_tourism = df_tourism.duplicated().sum()
print(f"df_tourism - Jumlah data awal: {jumlah_data_awal_tourism}")
print(f"df_tourism - Jumlah data duplikat ditemukan: {jumlah_duplikat_tourism}")
df_tourism.drop_duplicates(inplace=True)
print(f"df_tourism - Jumlah data setelah hapus duplikat: {len(df_tourism)}")
jumlah_data_awal_rating = len(df_rating)
jumlah_duplikat_rating = df_rating.duplicated().sum()
print(f"\ndf_rating - Jumlah data awal: {jumlah_data_awal_rating}")
print(f"df_rating - Jumlah data duplikat ditemukan: {jumlah_duplikat_rating}")
df_rating.drop_duplicates(inplace=True)
print(f"df_rating - Jumlah data setelah hapus duplikat: {len(df_rating)}")
jumlah_data_awal_user = len(df_user)
jumlah_duplikat_user_id = df_user.duplicated(subset=['User_Id']).sum()
print(f"\ndf_user - Jumlah data awal: {jumlah_data_awal_user}")
print(f"df_user - Jumlah data duplikat ditemukan: {jumlah_duplikat_user_id}")
df_user.drop_duplicates(subset=['User_Id'], inplace=True, keep='first')
print(f"df_user - Jumlah data setelah hapus duplikat: {len(df_user)}")
print("\nPenanganan duplikat selesai.")

print("\n=================== Data Preparation ==============")
print("=================== Filtering Data untuk Yogyakarta ==============")
target_keyword = 'yogyakarta'
df_tourism_yogya = df_tourism[df_tourism['City'].str.contains(target_keyword, case=False, na=False)].copy()
if df_tourism_yogya.empty:
    print("Tidak ada destinasi Yogyakarta ditemukan. Program berhenti.")
    exit()
print(f"Jumlah destinasi di area Yogyakarta: {len(df_tourism_yogya)}")

print("\n=================== Membersihkan Data Rating Yogyakarta untuk Collaborative Filtering (CF) ==============")
place_ids_yogya = df_tourism_yogya['Place_Id'].unique()
df_rating_yogya_cf = df_rating[df_rating['Place_Id'].isin(place_ids_yogya)].copy()
df_rating_yogya_cf.dropna(subset=['Place_Ratings'], inplace=True)
df_rating_yogya_cf['Place_Ratings'] = pd.to_numeric(df_rating_yogya_cf['Place_Ratings'], errors='coerce')
df_rating_yogya_cf.dropna(subset=['Place_Ratings'], inplace=True)
print(f"Jumlah rating Yogyakarta untuk CF setelah cleaning: {len(df_rating_yogya_cf)}")

print("\n=================== Rekayasa Fitur untuk Content-Based Filtering (CBF) ==============")
df_tourism_yogya['Rating'] = pd.to_numeric(df_tourism_yogya['Rating'], errors='coerce').fillna(df_tourism_yogya['Rating'].median())
print("Memproses teks menggunakan Sastrawi...")
stemmer = StemmerFactory().create_stemmer()
stopword_remover = StopWordRemoverFactory().create_stop_word_remover()
df_tourism_yogya['content_features'] = (df_tourism_yogya['Place_Name'].fillna('') + ' ' +
                                      df_tourism_yogya['Category'].fillna('') + ' ' +
                                      df_tourism_yogya['Description'].fillna('')).apply(lambda x: preprocess_text_sastrawi(x, stemmer, stopword_remover))
print("Kolom 'content_features' untuk CBF telah dibuat.")
print(df_tourism_yogya[['Place_Name', 'content_features']].head(2))

print("\n=================== Model Development Dengan Content Based Filtering (CBF) ==============")
print("=================== Perhitungan TF-IDF dan Cosine Similarity ==============")
tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix_cbf = tfidf_vectorizer.fit_transform(df_tourism_yogya['content_features'])
cosine_sim_cbf = cosine_similarity(tfidf_matrix_cbf)
results['CBF_tfidf_matrix_shape'] = tfidf_matrix_cbf.shape
print(f"[CBF] Matriks TF-IDF berhasil dibuat dengan dimensi: {results['CBF_tfidf_matrix_shape']}")
MODEL_CBF_SUCCESS = True

print("\n=================== Visualisasi Matriks Kesamaan (Cosine Similarity) ==============")
sample_size = 20
df_tourism_yogya_cbf_display = df_tourism_yogya.reset_index(drop=True)
sample_indices = df_tourism_yogya_cbf_display.head(sample_size).index
sample_cosine_sim = cosine_sim_cbf[sample_indices, :][:, sample_indices]
sample_place_names = df_tourism_yogya_cbf_display.head(sample_size)['Place_Name']
plt.figure(figsize=(12, 10))
sns.heatmap(sample_cosine_sim, annot=False, cmap='YlGnBu', xticklabels=sample_place_names, yticklabels=sample_place_names)
plt.title('Heatmap Cosine Similarity (Sampel 20 Tempat Pertama)')
plt.xticks(rotation=90, size=8); plt.yticks(size=8)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'heatmap_cosine_similarity.png'))
print(f"Visualisasi 'Heatmap Cosine Similarity' disimpan di folder '{plot_dir}'.")


print("\n=================== Uji Coba Model CBF ==============")
placeid_to_idx_map_cbf = pd.Series(df_tourism_yogya_cbf_display.index, index=df_tourism_yogya_cbf_display['Place_Id'])
sample_place_id_cbf = df_tourism_yogya_cbf_display['Place_Id'].iloc[0]
sample_place_name_cbf = df_tourism_yogya_cbf_display.loc[df_tourism_yogya_cbf_display['Place_Id'] == sample_place_id_cbf, 'Place_Name'].iloc[0]
results['CBF_sample_place_name'] = sample_place_name_cbf
print(f"[CBF] Contoh Top-5 Rekomendasi berdasarkan kemiripan dengan '{sample_place_name_cbf}':")
top_5_recs_cbf = get_content_based_recommendations(sample_place_id_cbf, cosine_sim_matrix_param=cosine_sim_cbf, tourism_df_param=df_tourism_yogya_cbf_display, id_to_idx_map_param=placeid_to_idx_map_cbf)
results['CBF_example_recommendations'] = top_5_recs_cbf
print(top_5_recs_cbf.to_string(index=False))

print("\n=================== Model Development Dengan Collaborative Filtering (CF) ==============")
print("=================== Persiapan Data untuk Model CF ==============")
if not df_rating_yogya_cf.empty and df_rating_yogya_cf['User_Id'].nunique() > 1 and df_rating_yogya_cf['Place_Id'].nunique() > 1:
    print("Memulai persiapan data: Encoding User_Id dan Place_Id, normalisasi rating, dan split data...")
    user_ids_cf = df_rating_yogya_cf['User_Id'].unique().tolist()
    user_to_user_encoded_cf = {x: i for i, x in enumerate(user_ids_cf)}
    user_encoded_to_user_cf = {i: x for i, x in enumerate(user_ids_cf)}
    df_rating_yogya_cf['user_encoded'] = df_rating_yogya_cf['User_Id'].map(user_to_user_encoded_cf)
    place_ids_cf_model = df_rating_yogya_cf['Place_Id'].unique().tolist()
    place_to_place_encoded_cf = {x: i for i, x in enumerate(place_ids_cf_model)}
    place_encoded_to_place_cf = {i: x for i, x in enumerate(place_ids_cf_model)}
    df_rating_yogya_cf['place_encoded'] = df_rating_yogya_cf['Place_Id'].map(place_to_place_encoded_cf)
    num_users_cf = len(user_to_user_encoded_cf)
    num_places_cf_model = len(place_to_place_encoded_cf)
    min_rating_cf = df_rating_yogya_cf['Place_Ratings'].min()
    max_rating_cf = df_rating_yogya_cf['Place_Ratings'].max()
    if max_rating_cf > min_rating_cf:
        df_rating_yogya_cf['rating_normalized'] = df_rating_yogya_cf['Place_Ratings'].apply(lambda x: (x - min_rating_cf) / (max_rating_cf - min_rating_cf)).values
    else:
        df_rating_yogya_cf['rating_normalized'] = 0.5
    df_cf_shuffled = df_rating_yogya_cf.sample(frac=1, random_state=42)
    x_cf = df_cf_shuffled[['user_encoded', 'place_encoded']].values
    y_cf = df_cf_shuffled['rating_normalized'].values
    train_indices_cf = int(0.8 * df_cf_shuffled.shape[0])
    x_train_cf, x_val_cf, y_train_cf, y_val_cf = (
        x_cf[:train_indices_cf],
        x_cf[train_indices_cf:],
        y_cf[:train_indices_cf],
        y_cf[train_indices_cf:]
    )
    validation_data_keras = (x_val_cf, y_val_cf)
    print("Persiapan Data CF Selesai.")
    print("Pembagian Data:")
    print(f"Data Train   : {len(x_train_cf)}")
    print(f"Data Validasi: {len(x_val_cf)}")
    MODEL_CF_PREPARED = True
else:
    print("Data rating Yogyakarta tidak cukup untuk memulai Collaborative Filtering.")
    MODEL_CF_PREPARED = False

print("\n=================== Training Model CF ==============")
if MODEL_CF_PREPARED:
    model_keras_cf = RecommenderNet(num_users_cf, num_places_cf_model, embedding_size=50)
    model_keras_cf.compile(
        loss=tf.keras.losses.BinaryCrossentropy(),
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        metrics=[tf.keras.metrics.RootMeanSquaredError()]
    )
    print("Melatih model Keras RecommenderNet...")
    history_cf = model_keras_cf.fit(
        x=x_train_cf,
        y=y_train_cf,
        batch_size=64,
        epochs=100,
        validation_data=validation_data_keras,
        verbose=1
    )
    MODEL_CF_SUCCESS = True
    results['CF_history'] = history_cf.history
    print("Training Model CF Selesai.")
else:
    print("Model CF tidak dilatih karena persiapan data gagal atau data tidak memadai.")


print("\n=================== Uji Coba Model CF ==============")
if MODEL_CF_SUCCESS:
    cf_mappings = {
        'user_to_user_encoded': user_to_user_encoded_cf,
        'place_to_place_encoded': place_to_place_encoded_cf,
        'place_encoded_to_place': place_encoded_to_place_cf
    }
    sample_user_id_cf_keras = df_rating_yogya_cf['User_Id'].unique()[0]
    results['CF_Keras_sample_user_id'] = sample_user_id_cf_keras
    print(f"[CF Keras] Contoh Top-5 Rekomendasi untuk User ID: {sample_user_id_cf_keras}")
    top_5_recs_cf_keras = get_top_n_recommendations_keras_cf(
        user_real_id=sample_user_id_cf_keras,
        model=model_keras_cf,
        tourism_df_all_yogya=df_tourism_yogya,
        rating_df_yogya_cf=df_rating_yogya_cf,
        mappings=cf_mappings
    )
    results['CF_Keras_example_recommendations'] = top_5_recs_cf_keras
    if isinstance(top_5_recs_cf_keras, pd.DataFrame) and not top_5_recs_cf_keras.empty:
        print(top_5_recs_cf_keras.to_string(index=False))
    else:
        print(f"Tidak ada rekomendasi baru untuk User ID {sample_user_id_cf_keras}.")
else:
    print("Uji Coba Model CF tidak dapat dilakukan karena model tidak berhasil dilatih.")


print("\n=================== Evaluation ==============")
print("=================== Evaluasi Model Collaborative Filtering ==============")
if MODEL_CF_SUCCESS:
    history_data = results.get('CF_history', {})
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history_data.get('root_mean_squared_error', []), label='Training RMSE')
    plt.plot(history_data.get('val_root_mean_squared_error', []), label='Validation RMSE')
    plt.title('Training and Validation RMSE'); plt.xlabel('Epoch'); plt.ylabel('RMSE'); plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(history_data.get('loss', []), label='Training Loss')
    plt.plot(history_data.get('val_loss', []), label='Validation Loss')
    plt.title('Training and Validation Loss'); plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, 'evaluasi_cf_metrics.png'))
    final_val_rmse = history_data.get('val_root_mean_squared_error', [None])[-1]
    results['CF_Keras_Val_RMSE'] = final_val_rmse
    print(f"  Metrik Evaluasi (Final Validation RMSE): {final_val_rmse:.4f}" if final_val_rmse else "N/A")
    print(f"  Visualisasi metrik evaluasi CF disimpan di folder '{plot_dir}'.")
else:
    print("  Model CF (Keras) tidak dievaluasi.")

print("\n=================== Evaluasi Model Content-Based Filtering ==============")
if MODEL_CBF_SUCCESS:
    print(f"  Evaluasi Kualitatif: Model ini dievaluasi secara kualitatif berdasarkan relevansi item yang direkomendasikan.")
    print(f"  Dimensi Matriks TF-IDF: {results.get('CBF_tfidf_matrix_shape', 'N/A')}")
    recs_cbf_df = results.get('CBF_example_recommendations', pd.DataFrame())
    if isinstance(recs_cbf_df, pd.DataFrame) and not recs_cbf_df.empty:
        print(f"\n  Visualisasi Similarity Score untuk rekomendasi '{results.get('CBF_sample_place_name', 'N/A')}':")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='similarity_score', y='Place_Name', data=recs_cbf_df, palette='magma')
        plt.title(f"Visualisasi Similarity Score"); plt.xlabel('Similarity Score'); plt.ylabel('Nama Tempat Wisata'); plt.xlim(0, 1)
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, 'evaluasi_cbf_similarity.png'))
        print(f"  Visualisasi 'Similarity Score' disimpan di folder '{plot_dir}'.")
    else:
        print(f"  Contoh Rekomendasi CBF: Tidak ada atau gagal.")
else:
    print("  Model CBF tidak berhasil dilatih atau dievaluasi.")


print("\n=================== Penyimpanan Model ==============")
print("=================== Membuat folder saved_model ==============")
save_dir = 'saved_model'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"Folder '{save_dir}' berhasil dibuat.")
else:
    print(f"Folder '{save_dir}' sudah ada.")

print("\n=================== Menyimpan Model Content-Based Filtering ==============")
if MODEL_CBF_SUCCESS:
    print("Menyimpan Model Content-Based Filtering ---")
    pickle.dump(tfidf_vectorizer, open(os.path.join(save_dir, 'cbf_tfidf_vectorizer.pkl'), 'wb'))
    np.save(os.path.join(save_dir, 'cbf_cosine_similarity_matrix.npy'), cosine_sim_cbf)
    df_tourism_yogya_cbf_display.to_csv(os.path.join(save_dir, 'cbf_tourism_data.csv'), index=False)
    print(f"Artefak CBF berhasil disimpan di folder '{save_dir}'.")
else:
    print("Model CBF tidak berhasil, tidak ada yang disimpan.")

print("\n=================== Menyimpan Model Collaborative Filtering ==============")
if MODEL_CF_SUCCESS:
    print("Menyimpan Model Collaborative Filtering ---")
    model_keras_cf.save(os.path.join(save_dir, 'cf_recommender_keras_model.keras'))
    cf_mappings = {'user_to_user_encoded': user_to_user_encoded_cf, 'place_to_place_encoded': place_to_place_encoded_cf, 'place_encoded_to_place': place_encoded_to_place_cf}
    with open(os.path.join(save_dir, 'cf_mappings.pkl'), 'wb') as f:
        pickle.dump(cf_mappings, f)
    print(f"Model CF (Keras) dan data mapping berhasil disimpan di folder '{save_dir}'.")
else:
    print("Model CF tidak berhasil, tidak ada yang disimpan.")

print("\n========================================================")
print("============== SEMUA PROSES TELAH SELESAI ==============")
print("================================================================================================================")
print("============== SEMUA PROSES TELAH SELESAI ==============")
print("========================================================")
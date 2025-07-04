
---

### 🇬🇧 English

```markdown
# IMDb Movie Review Sentiment Analysis (Positive/Negative)

This project performs sentiment analysis on IMDb movie reviews, classifying each review as **positive** or **negative** using a **Logistic Regression** model.

---

## 🔍 Dataset Used

- **IMDb Movie Reviews** (Loaded via TensorFlow)
- 50,000 reviews total (25K training, 25K test)
- Each review is labeled as either 1 (positive) or 0 (negative)

---

## 🛠 Technologies Used

- Python 3.x
- TensorFlow (for dataset)
- Scikit-learn (for model)
- Matplotlib & Seaborn (visualization)
- Joblib (model saving)

---

## 🚀 Project Workflow

1. **Data Loading & Preprocessing**  
   - Used top 10,000 most frequent words  
   - All reviews padded/truncated to length 200

2. **Model Training**  
   - Logistic Regression model trained for binary classification

3. **Evaluation**  
   - Accuracy, classification report, confusion matrix used  
   - Results visualized

4. **Model Saving**  
   - Trained model saved as `imdb_sentiment_model.pkl`

---

## 📁 Output Files

| File Name                    | Description                                   |
|-----------------------------|-----------------------------------------------|
| `sentiment_analysis_imdb.py`| Main Python script                            |
| `imdb_sentiment_model.pkl`  | Trained model                                 |
| `imdb_confusion_matrix.png` | Confusion matrix plot showing model accuracy  |

---

## 💻 Run the Project

```bash
python sentiment_analysis_imdb.py
```

```markdown
# IMDb Film Yorumları ile Duygu Analizi (Pozitif/Negatif)

Bu projede, IMDb film yorumları veri seti kullanılarak bir yorumun **olumlu (pozitif)** veya **olumsuz (negatif)** olup olmadığını tahmin eden bir **Lojistik Regresyon** modeli geliştirildi.

---

## 🔍 Kullanılan Veri Seti

- **IMDb Movie Reviews** (TensorFlow üzerinden otomatik yüklenir)
- 50.000 adet yorum (25K eğitim, 25K test)
- Her yorum ya 1 (pozitif) ya da 0 (negatif) olarak etiketlenmiştir

---

## 🛠 Kullanılan Teknolojiler

- Python 3.x
- TensorFlow (veri yükleme)
- Scikit-learn (modelleme)
- Matplotlib & Seaborn (grafik)
- Joblib (model kaydı)

---

## 🚀 Proje Akışı

1. **Veri yükleme ve ön işleme**  
   - En sık geçen 10.000 kelime kullanıldı  
   - Yorumlar 200 kelimeye sabitlendi (padding)

2. **Model Eğitimi**  
   - Lojistik regresyon ile metin sınıflandırması yapıldı  
   - Eğitim ve test verileri ayrı tutuldu

3. **Değerlendirme**  
   - Doğruluk oranı, sınıflandırma raporu ve karışıklık matrisi kullanıldı  
   - Başarı görselleştirildi

4. **Model Kaydı**  
   - Eğitim sonrası model `imdb_sentiment_model.pkl` olarak kaydedildi

---

## 📁 Oluşan Dosyalar

| Dosya Adı                     | Açıklama                                      |
|------------------------------|-----------------------------------------------|
| `sentiment_analysis_imdb.py` | Ana Python dosyası                            |
| `imdb_sentiment_model.pkl`   | Eğitilmiş model                               |
| `imdb_confusion_matrix.png`  | Karışıklık matrisi grafiği (başarı görseli)   |

---

## 💻 Çalıştırmak için

```bash
python sentiment_analysis_imdb.py


import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.datasets import imdb
from keras.preprocessing.sequence import pad_sequences
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import joblib

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import joblib

def main():
    # 1. Veri setini yükle
    num_words = 10000  # En sık geçen 10.000 kelime
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=num_words)

    print("Eğitim verisi boyutu:", len(X_train))
    print("Test verisi boyutu:", len(X_test))

    # 2. Her yorumu aynı uzunlukta hale getir (padding)
    max_len = 200
    X_train = pad_sequences(X_train, maxlen=max_len)
    X_test = pad_sequences(X_test, maxlen=max_len)

    # 3. sklearn için 2D matris haline getir
    X_train_2d = X_train.reshape(len(X_train), -1)
    X_test_2d = X_test.reshape(len(X_test), -1)

    # 4. Lojistik Regresyon Modeli
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_2d, y_train)

    # 5. Test verisi ile tahmin
    y_pred = model.predict(X_test_2d)

    # 6. Başarı ölçümü
    acc = accuracy_score(y_test, y_pred)
    print("Doğruluk Oranı: {:.4f}".format(acc))
    print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred))

    # 7. Karışıklık Matrisi
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Negatif', 'Pozitif'], yticklabels=['Negatif', 'Pozitif'])
    plt.xlabel("Tahmin")
    plt.ylabel("Gerçek")
    plt.title("Karışıklık Matrisi - IMDb Yorumları")
    plt.tight_layout()
    plt.savefig("imdb_confusion_matrix.png")
    plt.show()

    # 8. Modeli kaydet
    joblib.dump(model, "imdb_sentiment_model.pkl")
    print("Model başarıyla 'imdb_sentiment_model.pkl' olarak kaydedildi.")

if __name__ == "__main__":
    main()

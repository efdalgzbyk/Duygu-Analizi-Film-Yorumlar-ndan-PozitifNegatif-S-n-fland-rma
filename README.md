
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

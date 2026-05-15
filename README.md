# 🛡️ SMS Spam Classifier

A Machine Learning powered Streamlit web application that classifies SMS messages as **Spam** or **Ham (Safe Message)**.

---

# 🌐 Live App

🔗 https://sms-spam-classifier-xc9nttah6fe2k9xspzzfhu.streamlit.app/

---

# 📌 Overview

This project uses Machine Learning and NLP techniques to automatically detect spam SMS messages. The application processes text messages, transforms them into numerical vectors using TF-IDF Vectorization, and predicts whether the message is spam or safe using a trained Multinomial Naive Bayes model.

The project is deployed using Streamlit Cloud and hosted publicly through GitHub.

---

# 🚀 Key Features

- Real-time SMS spam prediction
- Interactive Streamlit web interface
- NLP-based text preprocessing
- TF-IDF Vectorization
- Machine Learning classification
- Lightweight and fast deployment
- User-friendly design
- Cloud deployment support

---

# 🧠 Model Details

| Component | Description |
|---|---|
| Algorithm | Multinomial Naive Bayes |
| Vectorizer | TF-IDF Vectorizer |
| NLP Library | NLTK |
| Language | Python |
| Frontend | Streamlit |

### Text Preprocessing Includes:
- Lowercasing
- Tokenization
- Removing punctuation
- Removing stopwords
- Stemming using PorterStemmer

---

# ⚙️ How It Works

1. User enters an SMS message.
2. The text is preprocessed using NLP techniques.
3. TF-IDF converts text into numerical vectors.
4. The trained machine learning model predicts:
   - Spam
   - Ham (Safe Message)
5. Result is displayed instantly on the web interface.

---

# 📩 Example Messages

## ✅ Ham (Safe Message)

```text
Hey, are we meeting tomorrow at the library?
```

Prediction:
```text
SAFE MESSAGE (HAM)
```
## 🚨 Spam Message

```text
Congratulations! You won a FREE iPhone. Click here now!!!
```

Prediction:
```text
SPAM MESSAGE
```
# 📸 Application Screenshot

![SMS Spam Classifier](https://raw.githubusercontent.com/SujithVarma-ai/SMS-spam-classifier/main/screenshot.png)

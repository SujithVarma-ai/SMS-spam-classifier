
# 🛡️ SMS Spam Classifier

A professional, lightweight, and deployment-ready Streamlit web application that uses Machine Learning (Multinomial Naive Bayes) and Natural Language Processing (NLTK) to classify SMS messages as either **Spam** or **Ham (Safe)**.

## 📁 Project Structure

```
sms_spam_classifier_project/
│
├── app.py               # The main Streamlit application script
├── requirements.txt     # Python dependencies
├── nltk.txt             # NLTK resources required for Streamlit Cloud deployment
├── model.pkl            # Trained MultinomialNB machine learning model
├── vectorizer.pkl       # Trained TF-IDF vectorizer
└── README.md            # Setup and deployment instructions
```

## 🚀 How to Run Locally

1. **Prerequisites**: Ensure you have Python installed (preferably Python 3.8+).
2. **Open Terminal**: Navigate to this project directory:
   ```bash
   cd path/to/sms_spam_classifier_project
   ```
3. **Install Dependencies**:
   It's recommended to create a virtual environment, but you can also install directly:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App**:
   Execute the following command to start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
5. **View in Browser**: The application will automatically open in your default web browser at `http://localhost:8501`.

## 🌐 How to Deploy on Streamlit Community Cloud (Free)

Deploying this app to the public web is incredibly easy using Streamlit Community Cloud.

1. **Upload to GitHub**:
   - Create a new public or private repository on GitHub.
   - Upload all the files in this directory (`app.py`, `requirements.txt`, `nltk.txt`, `model.pkl`, `vectorizer.pkl`) to the repository.

2. **Connect to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
   - Click on the **"New app"** button.
   - Select the GitHub repository you just created.
   - Set the branch to `main` (or `master`).
   - In the **"Main file path"** field, ensure it says `app.py`.

3. **Deploy**:
   - Click the **"Deploy!"** button.
   - Streamlit Cloud will automatically read the `requirements.txt` to install the Python libraries, read `nltk.txt` to install the NLP language files, and launch your application globally!

## 🧠 Model details
- **Preprocessing**: Lowercasing, Tokenization, Special Character Removal, Stop Word Removal, Stemming (PorterStemmer).
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency).
- **Algorithm**: Multinomial Naive Bayes (Optimized for high precision to prevent false positives).

# SMS-spam-classifier

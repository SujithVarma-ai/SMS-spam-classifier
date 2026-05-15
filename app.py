import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Configure the Streamlit page
st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- NLTK Resource Management ---
@st.cache_resource
def download_nltk_dependencies():
    """Download required NLTK resources silently."""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

download_nltk_dependencies()

ps = PorterStemmer()

# --- Core Logic ---
def transform_text(text):
    """Clean and preprocess the input text."""
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)

@st.cache_resource
def load_models():
    """Load the ML model and TF-IDF vectorizer."""
    try:
        tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
        model = pickle.load(open('model.pkl', 'rb'))
        return tfidf, model
    except FileNotFoundError:
        st.error("Model files not found! Ensure 'vectorizer.pkl' and 'model.pkl' exist in the directory.")
        st.stop()

tfidf, model = load_models()

# --- UI Styling ---
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        font-size: 1.1rem !important;
        border-radius: 10px;
        border: 1px solid #D1D5DB;
    }
    .result-box-spam {
        background-color: #FEE2E2;
        border-left: 5px solid #EF4444;
        padding: 20px;
        border-radius: 5px;
        color: #991B1B;
        font-weight: bold;
        font-size: 1.2rem;
        text-align: center;
        margin-top: 20px;
    }
    .result-box-ham {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
        padding: 20px;
        border-radius: 5px;
        color: #065F46;
        font-weight: bold;
        font-size: 1.2rem;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Layout ---
st.markdown("<div class='main-header'>🛡️ SMS Spam Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Powered by Machine Learning to keep your inbox clean</div>", unsafe_allow_html=True)

input_sms = st.text_area(
    "Enter your message below:", 
    height=150, 
    placeholder="e.g., Congratulations! You've won a $1000 Walmart gift card. Click here to claim..."
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("Predict Message Status", use_container_width=True, type="primary")

if predict_button:
    if not input_sms.strip():
        st.warning("⚠️ Please enter a message to classify.")
    else:
        with st.spinner("Analyzing message..."):
            # 1. Preprocess
            transformed_sms = transform_text(input_sms)
            
            # 2. Vectorize
            vector_input = tfidf.transform([transformed_sms]).toarray()
            
            # 3. Predict
            result = model.predict(vector_input)[0]
            
            # 4. Display professional result
            if result == 1:
                st.markdown("<div class='result-box-spam'>🚨 SPAM DETECTED<br><span style='font-size:0.9rem; font-weight:normal;'>This message looks suspicious and could be a scam or unsolicited advertisement.</span></div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-box-ham'>✅ SAFE MESSAGE (HAM)<br><span style='font-size:0.9rem; font-weight:normal;'>This message appears to be legitimate and safe.</span></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #6B7280; font-size: 0.8rem;'>Built with Streamlit • Multinomial Naive Bayes Model</p>", unsafe_allow_html=True)

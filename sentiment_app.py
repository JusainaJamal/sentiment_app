import streamlit as st
import os
import pandas as pd
from textblob import TextBlob
import pickle
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, AdamW


def load_model():

    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


def add_bg_fromm_url(url):
    try:
        st.markdown(
            f"""
            <style>
            .stApp{{
                background-image: url({url});
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html= True
        )
    except:
        pass
# calls the function to fetch the background
add_bg_fromm_url("https://img.freepik.com/free-photo/black-friday-elements-assortment_23-2149074076.jpg?w=826&t=st=1711609767~exp=1711610367~hmac=621c0ea0ca4a27fc57113bad9e6e3790b628eed8b49307904719e6b0a9b7d45d")



def main2():
    #st.title("")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state.logged_in:
        show_login_page()
    else:
        main()

def show_login_page():
    st.subheader("Login")
    
    # Apply CSS styling to change text color to white and make it bold
    st.markdown("""
        <style>
            /* Target the input fields */
            .stTextInput>div>div>div>input {
                color: white; /* Set text color to white */
                font-weight: bold; /* Make text bold */
            }
            /* Target the input labels */
            .stTextInput>label {
                color: white; /* Set label color to white */
            }
        </style>
    """, unsafe_allow_html=True)


    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        
        if username == "your_username" and password == "your_password":
            st.session_state.logged_in = True
            st.experimental_rerun()  # Rerun the app to redirect to welcome page
        else:
            st.error("Invalid username or password")
def logout():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()    

def save_review(product_name, review):
    file_name = f"{product_name}_reviews.txt"
    with open(file_name, 'a') as file:
        file.write(review + '\n')

# Function to get past reviews and calculate overall sentiment
def get_past_reviews(product_name):
    file_name = f"{product_name}_reviews.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            reviews = file.readlines()
        sentiments = [TextBlob(review).sentiment.polarity for review in reviews]
        overall_sentiment = sum(sentiments) / len(sentiments)
        return reviews, overall_sentiment
    else:
        return [], None
    
# Function to classify sentiment
def classify_sentiment(sentiment):
    if sentiment > 0.2:
        return "Good"
    elif sentiment < -0.2:
        return "Bad"
    else:
        return "Neutral"
    

# Main Streamlit app
def main():
    st.title("Product Review Sentiment Analysis")

    # Sidebar for user input
    product_name = st.sidebar.text_input("Enter Product Name:")
    review = st.sidebar.text_area("Type your review here:")

    if st.sidebar.button("Submit Review"):
        save_review(product_name, review)

    # Display past reviews and overall sentiment
    past_reviews, overall_sentiment = get_past_reviews(product_name)
    if past_reviews:
        st.subheader(f"Past Reviews for {product_name}:")
        for past_review in past_reviews:
            st.write(past_review)
        
        overall_sentiment_classification = classify_sentiment(overall_sentiment)
        st.write(f"     OVERALL SENTIMENT : {overall_sentiment_classification} ({overall_sentiment:.2f})")

    # Predict sentiment of new review
    if review:
        new_sentiment = TextBlob(review).sentiment.polarity
        new_sentiment_classification = classify_sentiment(new_sentiment)
        st.subheader("Sentiment Analysis:")
        st.write(f"New Review Sentiment: {new_sentiment_classification} ({new_sentiment:.2f})")
    logout()
  # Rerun the app to redirect to login page
    
if __name__ == "__main__":
    main2()


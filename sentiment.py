# from transformers import pipeline
# sentiment = pipeline("sentiment-analysis")


# import streamlit as st
# import os
# import pandas as pd
# from textblob import TextBlob

# # Function to save review to a text file
# def save_review(product_name, review):
#     file_name = f"{product_name}_reviews.txt"
#     with open(file_name, 'a') as file:
#         file.write(review + '\n')

# # Function to get past reviews and calculate overall sentiment
# def get_past_reviews(product_name):
#     file_name = f"{product_name}_reviews.txt"
#     if os.path.exists(file_name):
#         with open(file_name, 'r') as file:
#             reviews = file.readlines()
#         sentiments = [TextBlob(review).sentiment.polarity for review in reviews]
#         overall_sentiment = sum(sentiments) / len(sentiments)
#         return reviews, overall_sentiment
#     else:
#         return [], None

# # Main Streamlit app
# def main():
#     st.title("Amazon Product Review Sentiment Analysis")

#     # Sidebar for user input
#     product_name = st.sidebar.text_input("Enter Product Name:")
#     review = st.sidebar.text_area("Type your review here:")

#     if st.sidebar.button("Submit Review"):
#         save_review(product_name, review)

#     # Display past reviews and overall sentiment
#     past_reviews, overall_sentiment = get_past_reviews(product_name)
#     if past_reviews:
#         st.subheader(f"Past Reviews for {product_name}:")
#         for past_review in past_reviews:
#             st.write(past_review)
        
#         st.write(f"Overall Sentiment: {overall_sentiment:.2f}")

#     # Predict sentiment of new review
#     if review:
#         new_sentiment = TextBlob(review).sentiment.polarity
#         st.subheader("Sentiment Analysis:")
#         st.write(f"New Review Sentiment: {new_sentiment:.2f}")

# if __name__ == "__main__":
#     main()






import streamlit as st
import os
import pandas as pd
from textblob import TextBlob

# Function to save review to a text file
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
    st.title("Amazon Product Review Sentiment Analysis")

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

if __name__ == "__main__":
    main()

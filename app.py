import streamlit as st
from transformers import pipeline
import time

# --- Page Setup ---
st.set_page_config(
    page_title="Multilingual Sentiment Analyzer",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Model Loading (Cache RE-ENABLED) ---
@st.cache_resource # <-- Cache is now ACTIVE again
def load_sentiment_model():
    """Loads the Hugging Face sentiment analysis pipeline."""
    try:
        model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
        print(f"Attempting to load model (CACHE ENABLED): {model_name}") # Indicate cache is on
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model=model_name,
            tokenizer=model_name,
            use_fast=False # Keep this, as it seemed necessary before
            )
        print("Sentiment model loaded successfully.")
        return sentiment_pipeline
    except Exception as e:
        print(f"Error loading the model: {e}")
        st.error(f"Error loading the AI model. Please check the console. Error: {e}")
        return None

# Load the model once using the cached function
sentiment_analyzer = load_sentiment_model()

# --- User Interface ---
st.title("😊 Text Sentiment Analyzer (English/Spanish)")
st.markdown("""
This application uses a pre-trained Artificial Intelligence model (XLM-RoBERTa)
to analyze whether the text you enter (in **English** or **Spanish**) has a
**Positive**, **Negative**, or **Neutral** sentiment.

**Instructions:**
1.  Type or paste the text you want to analyze into the box below.
2.  Click the 'Analyze Sentiment' button.
3.  View the result.
""")
st.markdown("---")

user_input = st.text_area("Enter your text here (English or Spanish):", height=150, placeholder="e.g., 'I love this product' or 'Esta película fue terrible'")
analyze_button = st.button("Analyze Sentiment", type="primary")

# --- Analysis Logic and Displaying Results ---
if analyze_button and user_input:
    if sentiment_analyzer: # Check if model loaded successfully
        with st.spinner('Analyzing text...'):
            try:
                # Perform prediction using the globally loaded pipeline
                start_time = time.time()
                result = sentiment_analyzer(user_input)
                end_time = time.time()
                # print("Raw model output:", result) # Keep commented unless needed

                sentiment_label = result[0]['label']
                sentiment_score = result[0]['score']

                st.markdown("---")
                st.subheader("Analysis Result:")

                # Convert label to lowercase for robust comparison
                sentiment_label_lower = sentiment_label.lower()

                if sentiment_label_lower == 'positive':
                    st.success(f"✅ Sentiment Detected: {sentiment_label.capitalize()} (Confidence: {sentiment_score:.2%})")
                    st.balloons()
                elif sentiment_label_lower == 'negative':
                    st.error(f"❌ Sentiment Detected: {sentiment_label.capitalize()} (Confidence: {sentiment_score:.2%})")
                else: # Assumed Neutral or other
                    st.warning(f"➖ Sentiment Detected: {sentiment_label.capitalize()} (Confidence: {sentiment_score:.2%})")

                # Optional: Display analysis time
                # st.info(f"Analysis time: {end_time - start_time:.2f} seconds")

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
                print(f"Error during analysis: {e}")
    else:
        st.error("The AI model could not be loaded. Analysis cannot be performed.")


elif analyze_button and not user_input:
    st.warning("⚠️ Please enter some text to analyze.")

# --- Footer ---
st.markdown("---")
st.caption("Application created with Streamlit and Hugging Face Transformers.")
# Show model name if loaded successfully
if sentiment_analyzer and hasattr(sentiment_analyzer, 'model') and hasattr(sentiment_analyzer.model, 'name_or_path'):
    st.caption(f"Model Used: {sentiment_analyzer.model.name_or_path}")
else:
     st.caption("Model Used: cardiffnlp/twitter-xlm-roberta-base-sentiment")
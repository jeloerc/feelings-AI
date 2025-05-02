from transformers import pipeline
import time

# Use the same model name as in your Streamlit app
model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
print(f"--- Attempting to load model: {model_name} ---")

try:
    # Load the pipeline, explicitly using the slow tokenizer like in the app
    start_load_time = time.time()
    sentiment_analyzer = pipeline(
        "sentiment-analysis",
        model=model_name,
        tokenizer=model_name,
        use_fast=False
    )
    end_load_time = time.time()
    print(f"--- Model loaded successfully in {end_load_time - start_load_time:.2f} seconds! ---")

except Exception as e:
    print(f"XXXXXXXXXXXXXXXX Error loading model: {e} XXXXXXXXXXXXXXXX")
    exit() # Stop if the model can't load

# --- Test cases ---
test_texts = [
    "im very sad",
    "I am extremely happy today!",
    "This is the worst thing ever, I hate it.",
    "Esta película es maravillosa.",
    "Estoy muy decepcionado con el servicio.",
    "The weather is okay.",
    "This is just a neutral statement."
]

print("\n--- Running Inference Tests ---")
for text in test_texts:
    try:
        start_inference_time = time.time()
        result = sentiment_analyzer(text)
        end_inference_time = time.time()
        print(f"Input: '{text}'")
        print(f"Output: {result} (Took {end_inference_time - start_inference_time:.2f}s)")
        print("-" * 10)
    except Exception as e:
        print(f"XXXXXXXXXXXXXXXX Error during inference for '{text}': {e} XXXXXXXXXXXXXXXX")

print("\n--- Test Complete ---")

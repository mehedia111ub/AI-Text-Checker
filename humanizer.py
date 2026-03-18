# import necessary libraries for the humanizer functionality
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Function to load the humanizer model and tokenizer using Hugging Face Transformers
def load_humanizer():
    model_name = "google/flan-t5-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return tokenizer, model

# Function to humanize text by rewriting it in a more natural 
# and conversational way using the loaded model and tokenizer 
# with a specified maximum word limit for the output
def humanize_text(text, tokenizer, model, max_words=100):
    prompt = f"Rewrite this text in a more human, natural way:\n{text}"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    
    outputs = model.generate(
        **inputs,
        max_length=max_words,
        num_beams=4,
        early_stopping=True
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
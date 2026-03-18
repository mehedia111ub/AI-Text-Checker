# import necessary libraries
from transformers import pipeline

# Function to load the AI detector model using Hugging Face Transformers pipeline
def load_detector():
    classifier = pipeline(
        "sentiment-analysis",
        model="roberta-base",
        device=-1
    )
    return classifier

# Function to detect AI-generated content and 
# calculate AI vs Human scores based on the classifier's output
def detect_ai(text, classifier):
    result = classifier(text)[0]

    # Simulated scoring (since no real detector)
    score = result['score']

    # Map confidence into pseudo AI detection
    ai_score = round(score * 60, 2)
    human_score = round(100 - ai_score, 2)

    return ai_score, human_score
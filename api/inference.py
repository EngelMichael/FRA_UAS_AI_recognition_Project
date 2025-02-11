from transformers import BertTokenizer, BertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import torch
import asyncio

# This is the backend code to the processing endpoint.

# Load the trained model and tokenizer from collab (ephemeral)
model = AutoModelForSequenceClassification.from_pretrained("roberta_model")
tokenizer = AutoTokenizer.from_pretrained("roberta_model")

# Function to perform inference with probabilities (asynchronous)
async def classify_text_with_probabilities(input_text):
    # Run the blocking code in a separate thread to prevent blocking the event loop
    return await asyncio.to_thread(sync_classify_text_with_probabilities, input_text)

# Function to perform inference with probabilities
def sync_classify_text_with_probabilities(input_text):

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Run the model to get predictions
    outputs = model(**inputs)
    logits = outputs.logits

    # Convert logits to probabilities using softmax
    probabilities = F.softmax(logits, dim=1)

    # Get the predicted class (0 or 1)
    predicted_class = torch.argmax(probabilities, dim=1).item()

    # Map the predicted class to its meaning
    class_mapping = {1: "Human-written", 0: "AI-generated"}

    # Get probabilities for both classes
    prob_human = probabilities[0][1].item()
    prob_ai = probabilities[0][0].item()

    return {
        "classification": class_mapping[predicted_class],
        "probabilities": {
            "Human-written": prob_human,
            "AI-generated": prob_ai
        }
    }

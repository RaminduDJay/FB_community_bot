from transformers import MarianMTModel, MarianTokenizer

# Use Helsinki-NLP for Sinhala translation
model_name = "Helsinki-NLP/opus-mt-en-si"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_sinhala(text):
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    return tokenizer.decode(translated[0], skip_special_tokens=True)
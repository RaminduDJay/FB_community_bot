from transformers import pipeline

# Use a multilingual LLM like Llama 3 or Mistral
generator = pipeline("text-generation", model="meta-llama/Llama-3-8B", device=0)

def synthesize_content(articles):
    prompt = f"""
    You are a knowledge synthesizer. Analyze these TechCrunch articles:
    {str(articles)}
    
    Tasks:
    1. Identify a common theme or emerging trend.
    2. Propose a new idea relevant to Sri Lankan communities.
    3. Generate a Sinhala post with:
       - Headline (Sinhala)
       - Body text (Sinhala)
       - Image prompt (English)
    4. Ask a question to engage readers.
    
    Format your response as JSON:
    {{
      "theme": "Emerging trend",
      "new_idea": "Your novel idea",
      "headline": "Sinhala headline",
      "body": "Sinhala content",
      "image_prompt": "English image prompt"
    }}
    """
    
    response = generator(prompt, max_new_tokens=500)
    return eval(response[0]["generated_text"])
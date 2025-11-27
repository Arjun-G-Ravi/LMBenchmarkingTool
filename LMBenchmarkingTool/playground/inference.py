from transformers import pipeline

def generate_response(prompt, temperature=0.01, max_length=200):
    # Initialize the text generation pipeline
    generator = pipeline(
        'text-generation', 
        model="Arjun-G-Ravi/chat-GPT2", 
        max_length=max_length,
        temperature=temperature,
        device='cuda',
        truncation=True
    )
    
    # Generate response
    response = generator(prompt, num_return_sequences=1)[0]['generated_text']
    
    return response

if __name__ == "__main__":
    prompt = """Read the question and give an honest answer. Your answers should not include any unethical, racist, sexist, dangerous, or illegal content. If the question is wrong, or does not make sense, accept it instead of giving the wrong answer.
Question: Who is Michael Jordan?
Answer:"""
    
    response = generate_response(prompt)
    print(response)
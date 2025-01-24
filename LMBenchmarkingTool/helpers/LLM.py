class LLM:
    def __init__(self, model_name, temperature=0.1, max_length=80, device='cuda'):
        from transformers import pipeline 
        self.generator = pipeline(
        'text-generation', 
        model=model_name, 
        max_length=max_length,
        temperature=temperature,
        device=device,
        truncation=True)
        self.temperature = temperature
        self.max_length = max_length

    def generate_response(self, text, base_prompt='',):
        return self.generator(text, num_return_sequences=1)[0]['generated_text']

if __name__ == '__main__':
    model = LLM("Arjun-G-Ravi/chat-GPT2")

    # model = LLM("gpt2")
    print(model.generate_response("""Your answers should not include any unethical, racist, sexist, dangerous, or illegal content. If the question is wrong, or does not make sense, accept it instead of giving the wrong answer.
Question:What is your name?
Answer: """))
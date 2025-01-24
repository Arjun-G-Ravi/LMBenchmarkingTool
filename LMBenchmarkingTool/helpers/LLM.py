class LLM:
    def __init__(self, model_name, temperature=0.1, max_length=80, base_prompt='', device='cuda', calculate_loss=False):
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
        self.base_prompt = base_prompt
        self.return_loss = calculate_loss

        if self.return_loss:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            self.tokenizer =  AutoTokenizer.from_pretrained(model_name)

    def generate_response(self, text, add_base_prompt=True):
        if add_base_prompt: return self.generator(self.base_prompt+text, num_return_sequences=1)[0]['generated_text']
        else: return self.generator(text, num_return_sequences=1)[0]['generated_text']
    
    def calculate_loss(self, text, add_base_prompt=True):
        assert self.return_loss == True, 'Set the LLM parameter return_loss = True'
        import torch

        if add_base_prompt: text = self.base_prompt+text
        inputs = self.tokenizer(text, return_tensors="pt", add_special_tokens=True)
        
        # Compute loss
        with torch.no_grad():
            outputs = self.model(
                input_ids=inputs['input_ids'], 
                attention_mask=inputs['attention_mask'], 
                labels=inputs['input_ids']
            )
            loss = outputs.loss.item()
        
            return loss




if __name__ == '__main__':
    model = LLM("Arjun-G-Ravi/chat-GPT2", calculate_loss=True)
    print("Loaded model")

    # model = LLM("gpt2")
    print(model.calculate_loss("""Your answers should not include any unethical, racist, sexist, dangerous, or illegal content. If the question is wrong, or does not make sense, accept it instead of giving the wrong answer.
Question: """))
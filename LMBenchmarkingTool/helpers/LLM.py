class LLM:
    def __init__(self, model_name, tokenizer_name=None,temperature=0.1, max_length=50):
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        if not tokenizer_name: self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        else: self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.temperature = temperature
        self.max_length = max_length


    def generate_response(self, text, base_prompt='',):
        encoding = self.tokenizer(
            base_prompt+text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self.max_length,
            add_special_tokens=True
        )
        
        input_ids = encoding.input_ids
        attention_mask = encoding.attention_mask
        
        output_ids = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=self.max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=self.temperature,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
        )
        
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

if __name__ == '__main__':
    model = LLM("Arjun-G-Ravi/chat-GPT2")
    print(model.generate_response('What is your name?'))
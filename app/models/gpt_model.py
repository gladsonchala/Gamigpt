import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class GPTModel:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def predict(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt').to(self.device)
        output = self.model.generate(input_ids, max_length=1000, do_sample=True)
        result = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return result

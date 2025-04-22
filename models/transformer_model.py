from transformers import T5Tokenizer, TFT5ForConditionalGeneration

def load_t5_model(model_name='t5-small'):
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = TFT5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

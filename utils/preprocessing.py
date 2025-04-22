import json
import re
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

def load_dataset(file_path='Generasi-Judul-Berita/data/newsapi_articles.json'):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    contents = [item['content'] for item in data if item['content'] and item['title']]
    titles = [item['title'] for item in data if item['content'] and item['title']]
    return contents, titles

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\r\n|\n|\r', ' ', text)  # hilangkan newline
    text = re.sub(r'[^a-zA-Z0-9.,!?\'\" ]', '', text)  # hilangkan karakter aneh
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def prepare_tokenizer(inputs, targets, num_words=10000):
    input_tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=num_words, oov_token="<OOV>")
    target_tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=num_words, oov_token="<OOV>")
    
    input_tokenizer.fit_on_texts(inputs)
    target_tokenizer.fit_on_texts(targets)
    
    return input_tokenizer, target_tokenizer

def encode_sequences(input_tokenizer, target_tokenizer, inputs, targets, max_len_input=300, max_len_target=30):
    input_seq = input_tokenizer.texts_to_sequences(inputs)
    target_seq = target_tokenizer.texts_to_sequences(targets)
    
    input_seq = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=max_len_input, padding='post')
    target_seq = tf.keras.preprocessing.sequence.pad_sequences(target_seq, maxlen=max_len_target, padding='post')
    
    return input_seq, target_seq

def get_train_test_split(inputs, targets, test_size=0.2):
    return train_test_split(inputs, targets, test_size=test_size, random_state=42)

if __name__ == "__main__":
    contents, titles = load_dataset('Generasi-Judul-Berita/data/newsapi_articles.json')
    print(f"Jumlah data: {len(contents)}\n")

    print("Contoh artikel:")
    print(contents[0][:500], "...")

    print("\nJudul terkait:")
    print(titles[0])

    # Coba preprocessing dan tokenisasi
    contents = [clean_text(c) for c in contents]
    titles = [clean_text(t) for t in titles]

    input_tok, target_tok = prepare_tokenizer(contents, titles)
    input_seq, target_seq = encode_sequences(input_tok, target_tok, contents, titles)

    print(f"\nContoh input sequence: {input_seq[0][:10]}")
    print(f"Contoh target sequence: {target_seq[0][:10]}")

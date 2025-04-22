import tensorflow as tf

def build_lstm_seq2seq_model(input_vocab_size, target_vocab_size, 
                              embedding_dim=128, lstm_units=256, 
                              max_input_len=300, max_target_len=30):
    # Encoder
    encoder_inputs = tf.keras.Input(shape=(max_input_len,))
    encoder_embedding = tf.keras.layers.Embedding(input_vocab_size, embedding_dim)(encoder_inputs)
    encoder_lstm, state_h, state_c = tf.keras.layers.LSTM(
        lstm_units, return_state=True)(encoder_embedding)

    encoder_states = [state_h, state_c]

    # Decoder
    decoder_inputs = tf.keras.Input(shape=(max_target_len,))
    decoder_embedding = tf.keras.layers.Embedding(target_vocab_size, embedding_dim)(decoder_inputs)
    decoder_lstm = tf.keras.layers.LSTM(lstm_units, return_sequences=True)(decoder_embedding, initial_state=encoder_states)
    decoder_outputs = tf.keras.layers.Dense(target_vocab_size, activation='softmax')(decoder_lstm)

    model = tf.keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
    return model

import tensorflow as tf

def build_lstm_attention_model(input_vocab_size, target_vocab_size,
                                embedding_dim=128, lstm_units=256,
                                max_input_len=300, max_target_len=30):

    # Encoder
    encoder_inputs = tf.keras.Input(shape=(max_input_len,))
    encoder_embedding = tf.keras.layers.Embedding(input_vocab_size, embedding_dim)(encoder_inputs)
    encoder_lstm = tf.keras.layers.LSTM(lstm_units, return_sequences=True, return_state=True)
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)

    # Decoder
    decoder_inputs = tf.keras.Input(shape=(max_target_len,))
    decoder_embedding = tf.keras.layers.Embedding(target_vocab_size, embedding_dim)(decoder_inputs)
    decoder_lstm = tf.keras.layers.LSTM(lstm_units, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=[state_h, state_c])

    # Attention Layer
    attention = tf.keras.layers.Attention()([decoder_outputs, encoder_outputs])  # [batch, target_len, lstm_units]
    concat = tf.keras.layers.Concatenate(axis=-1)([decoder_outputs, attention])

    # Output Layer
    dense = tf.keras.layers.Dense(target_vocab_size, activation='softmax')(concat)

    # Final model
    model = tf.keras.Model([encoder_inputs, decoder_inputs], dense)
    return model

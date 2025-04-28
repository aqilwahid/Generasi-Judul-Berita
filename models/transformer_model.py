# Positional Encoding
class PositionalEncoding(tf.keras.layers.Layer):
    def call(self, inputs):
        positions = tf.range(tf.shape(inputs)[1])[:, tf.newaxis]
        return inputs + tf.cast(positions, tf.float32)

# Transformer Block
def transformer_block(embed_dim, num_heads, ff_dim):
    inputs = tf.keras.Input(shape=(None, embed_dim))
    attention = tf.keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)(inputs, inputs)
    attention = tf.keras.layers.Add()([inputs, attention])
    attention = tf.keras.layers.LayerNormalization()(attention)

    ff = tf.keras.layers.Dense(ff_dim, activation="relu")(attention)
    ff = tf.keras.layers.Dense(embed_dim)(ff)
    outputs = tf.keras.layers.Add()([attention, ff])
    outputs = tf.keras.layers.LayerNormalization()(outputs)
    return tf.keras.Model(inputs=inputs, outputs=outputs)

# Membangun Model
embed_dim = 128
num_heads = 4
ff_dim = 512

input_vocab_size = len(input_tokenizer.word_index) + 1
target_vocab_size = len(target_tokenizer.word_index) + 1

encoder_inputs = tf.keras.Input(shape=(300,))
x = tf.keras.layers.Embedding(input_vocab_size, embed_dim)(encoder_inputs)
x = PositionalEncoding()(x)
x = transformer_block(embed_dim, num_heads, ff_dim)(x)

decoder_inputs = tf.keras.Input(shape=(29,))
y = tf.keras.layers.Embedding(target_vocab_size, embed_dim)(decoder_inputs)
y = PositionalEncoding()(y)
y = transformer_block(embed_dim, num_heads, ff_dim)(y)

context = tf.keras.layers.MultiHeadAttention(num_heads=4, key_dim=embed_dim)(y, x)
concat = tf.keras.layers.Concatenate()([y, context])

outputs = tf.keras.layers.Dense(target_vocab_size, activation='softmax')(concat)

model_tf = tf.keras.Model([encoder_inputs, decoder_inputs], outputs)
model_tf.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_tf.summary()

# Training the Model
history_tf = model_tf.fit(
    [X_train, decoder_input_train],
    tf.expand_dims(decoder_target_train, -1),
    validation_split=0.1,
    batch_size=16,
    epochs=15
)

# Inference Function
def decode_custom_transformer(input_seq_single):
    dummy_decoder_input = tf.zeros((1, 29))
    output = model_tf.predict([input_seq_single, dummy_decoder_input])
    output_tokens = tf.argmax(output[0], axis=-1).numpy()

    reverse_target_word_index = {i: w for w, i in target_tokenizer.word_index.items()}

    decoded_sentence = []
    for idx in output_tokens:
        word = reverse_target_word_index.get(idx, '')
        if word in ('<end>', ''):
            break
        if word != '<start>':
            decoded_sentence.append(word)
    return ' '.join(decoded_sentence)

from transformers import AutoTokenizer

if __name__ == '__main__':
    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # Sample text
    texts = ["Hello, how are you?", "I am fine, thank you!"]

    # Tokenize text
    encodings = tokenizer(texts,
                          truncation=True,
                          padding=True,
                          return_tensors="pt")

    # Print tokenized inputs
    print(encodings)

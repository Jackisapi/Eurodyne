import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained GPT-2 model and tokenizer

# Context and Question
# question = "What is your opinion on the film Ex Machina"

# question = "Should robots have rights "
# Encode the context and question
# question = "This film is bad"
while True:
    question = input("Benchmark loaded please enter in a question \n"
                     ":> ")
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    print("GPT2 Loaded")
    input_text = question
    indexed_tokens = tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

    # Predict all tokens
    with torch.no_grad():
        outputs = model.generate(indexed_tokens, max_length=30, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Decode the generated answer
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(len(answer))

    print("Answer:", answer, '\n')


    print("IMDB Model")

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('C:/Users/jack/Desktop/imdb_model/',use_safetensors=True)

    # Context and Question

    # Encode the context and question
    input_text = question
    indexed_tokens = tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

    # Predict all tokens
    with torch.no_grad():
        outputs = model.generate(indexed_tokens,min_length=10, max_length=30, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Decode the generated answer
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(len(answer))

    print("Answer:", answer)


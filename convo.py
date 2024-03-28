from gpt4all import GPT4All
model = 'model.safetensor'
device = 'cpu'
model = GPT4All(model, device=device)
with model.chat_session():
    while True:
        response = model.generate(prompt=input('hello'))
        print(response)

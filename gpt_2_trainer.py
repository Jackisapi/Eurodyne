import torch
import transformers
from datasets import load_dataset

device = torch.device(device='cuda' if torch.cuda.is_available() else 'cpu')

torch.cuda.empty_cache()
tokenizer = transformers.AutoTokenizer.from_pretrained('distilbert/distilgpt2')
model = transformers.AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-125m', device_map=device)

if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))


raw_dataset = load_dataset('nikesh66/Slang-Dataset')


def cleaner(examples):
    chunk = list(examples.keys())
    print(chunk)
    params = list(examples[chunk[0]].features.keys())
    print(params)
    inputs = tokenizer(examples[chunk[0]],padding='max_length',truncation=True,return_tensors='pt')
    inputs[params[0]] = inputs['input_ids'].clone()
    return inputs


tokenized_datasets = raw_dataset.map(cleaner, batched=True)

training_args = transformers.TrainingArguments(
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=8,
    output_dir="/home/jack/Desktop/test/"
)

trainer = transformers.Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
)

result = trainer.train()

print(result)

model.save_pretrained("/home/jack/Desktop/test/")

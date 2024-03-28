import torch
import transformers
from datasets import load_dataset

device = torch.device(device='cuda' if torch.cuda.is_available() else 'cpu')

print(torch.cuda.empty_cache())
tokenizer = transformers.AutoTokenizer.from_pretrained('distilbert/distilgpt2')
model = transformers.AutoModelForCausalLM.from_pretrained('distilbert/distilgpt2', device_map=device)

if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))

#
raw_dataset = load_dataset('imdb')
print(raw_dataset, end='\n')


def cleaner(examples):
    inputs = tokenizer(examples['text'],padding='max_length',truncation=True,return_tensors='pt')
    inputs['labels'] = inputs['input_ids'].clone()
    return inputs


tokenized_datasets = raw_dataset.map(cleaner, batched=True)
print(tokenized_datasets)

training_args = transformers.TrainingArguments(
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=8,
    output_dir="C:/Users/jack/Desktop/imdb_model/"
)

trainer = transformers.Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
)

result = trainer.train()

print(result)

model.save_pretrained("C:/Users/jack/Desktop/imdb_model/")

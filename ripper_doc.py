import sys
import time
from  os import getcwd
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

from soulkiller import soul_lib

sys.path.insert(0, getcwd() +'/soulkiller/')


class Ripper:
    def __init__(self, model_tag, data_tag, output_dir, args=False):
        # Checks for a cuda compatible card if found will use else cpu

        if args:
            self.section = str(args)
        self.trainer = None
        self.training_args = None
        self.tokenized_data = None
        self.device = torch.device(device='cuda' if torch.cuda.is_available() else 'cpu')
        self.data_tag = data_tag

        # Downloads the tokenizer for the model

        self.tokenizer = AutoTokenizer.from_pretrained(model_tag)

        # And Downloads the model

        self.model = AutoModelForCausalLM.from_pretrained(model_tag)

        # sets an output dir

        self.output_dir = output_dir

        # loads data and checks for pad tokens if not found will add
        if args:
            self.data = load_dataset(data_tag, self.section, trust_remote_code=True)
        else:
            self.data = load_dataset(data_tag, trust_remote_code=True)
        # Checks for padding tokens if not found will add some
        if self.tokenizer.pad_token is None:
            self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
            self.model.resize_token_embeddings(len(self.tokenizer))

    def prep_data(self):
        edit_data = input("Would you like to open your data in pandas? \n ")
        if edit_data.upper() == 'Y':
            try:
                pd_data = soul_lib.data_2_pd(self.data_tag, 'train')
                print(pd_data)
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass

        def cleaner(examples):
            # Tokenizes the data sentences allows them to go to max length and returns a pytorch tensor
            dict_data = self.data['train'].to_dict()
            print(dict_data)
            dict_keys = list(dict_data.keys())
            inputs = self.tokenizer(examples[dict_keys[0]], padding='max_length', truncation=True, return_tensors='pt')
            inputs['labels'] = inputs['input_ids'].clone()
            return inputs

        self.tokenized_data = self.data.map(cleaner, batched=True)
        return self.tokenized_data

    def start_training(self):
        self.training_args = TrainingArguments(
            per_device_train_batch_size=4,
            per_device_eval_batch_size=4,
            gradient_accumulation_steps=8,
            output_dir="C:/Users/jack/Desktop/imdb_model/"
        )

        self.trainer = Trainer(
            model=self.model,
            args=self.training_args,
            train_dataset=self.tokenized_data['train'],
            eval_dataset=self.tokenized_data['test'],
        )
        print("The Ripper is active training will start ")
        self.trainer.train()
        self.model.save_pretrained(self.output_dir)

    def debug_mode(self):
        return self.device, self.model, self.tokenizer



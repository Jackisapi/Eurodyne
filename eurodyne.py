import argparse
from ripper_doc import Ripper
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

if __name__ == '__main__':
    try:
        # all the different arguments for the program
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--train', help='To Train a Model', action='store_true')
        parser.add_argument('-l', '--load', help='To Load a Model', action='store_true')
        parser.add_argument('-s', '--safetensor', help="Specifying if you are loading a safetensor",
                            action='store_true')
        parser.add_argument('-m', '--model', help="A Model From Huggingface or Local Path")
        parser.add_argument('-token', '--tokenizer', help='When loading a model specifies what tokenizer to load')
        parser.add_argument('-d', '--data', help='A Dataset from Hugging Face')
        parser.add_argument('-e', '--entry', help='If the dataset has multiple entries', action='store_true')
        parser.add_argument('-out', '--output', help='A Output Folder ')
        # takes all the args and parses them and stores
        args = parser.parse_args()
        # converts args to  a dictionary
        args_dict = vars(args)
        # checks for sectioned datasets
        is_sec = args_dict['entry']
        # if you are training a model
        if args_dict['train']:
            # loads ripper_doc.py and initilizes
            ripper = Ripper(args_dict['model'], args_dict['data'], args_dict['output'], args=is_sec)
            # ripper doc will parse and prep the data for the model
            ripper.prep_data()
            # finally ripper_doc will start training
            ripper.start_training()
        elif args_dict['load']:
            if args_dict['safetensor']:
                tokenizer = AutoTokenizer.from_pretrained(args_dict['tokenizer'])
                model = AutoModelForCausalLM.from_pretrained(args_dict['model'])
                while True:
                    question = input("Model loaded \n :> ")
                    if question == 'stop':
                        break
                    else:
                        indexed_tokens = tokenizer.encode(question, add_special_tokens=False, return_tensors='pt')
                        with torch.no_grad():
                            outputs = model.generate(indexed_tokens, max_length=30, num_return_sequences=1,
                                                     pad_token_id=tokenizer.eos_token_id)
                            answers = tokenizer.decode(outputs[0], skip_special_tokens=True)
                            print(answers)
        else:
            exit('NO OPERATION SPECIFIED')
    except EnvironmentError as e:
        print(f"ERROR PARAMETER SPECIFIED NOT FOUND \n {e}")
    except Exception as e:
        print(f"ERR UNKNOWN ERROR OCCURED {e}")

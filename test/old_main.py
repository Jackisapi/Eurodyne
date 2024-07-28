from libs.libgpt4all import *
from libs.text_function import txt_reader
from gpt4all import GPT4All
from libs.libyaml import *
from libs.libtrainer import trainer

# To See all the functions for this program please look at libgpt4all.py and text_function.py


if __name__ == "__main__":
    cli_conf = yaml_conf()
    # Loads the Configuration from conf.yaml
    model = cli_conf['model']['default_model']
    # Fetches data for the default model and for the compute devicce
    # Downloading modle
    device = cli_conf['hardware']['compute_device']
    talk = GPT4All(model_name=model, device=device)
    # Initilizes GPT4ALL With the data
    with talk.chat_session():
        while True:
            prompt = input(f"Compute: {device} Working On {model} \n"
                           f"/>  ")
            if prompt == 'ls':
                # Loads All The Different models and there data from models2.json
                all_models('models2.json')
            elif prompt == 'ch':
                model = change_model(model)
                # calls change_model
                print(model)
                talk = GPT4All(model_name=model, device=device)
                # Refactors GPT4All With the changes made
            elif prompt == 'hw':
                device = hw_change(device)
                print(f"Device Changed To {device}")
                talk = GPT4All(model_name=model, device=device)
                # Refactors GPT4All with the changes made
            elif prompt == 'exit':
                exit_prompt()
            elif prompt == 'help':
                txt_reader('../help')
            elif prompt == 'config':
                cli_conf = config_edit()
                # Launches the config editor`
            elif prompt == "train":
                trainer()
            else:
                response = talk.generate(prompt=prompt)
                print(response)

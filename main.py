import argparse
from ripper_doc import Ripper

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--train', help='To Train a Model', action='store_true')
        parser.add_argument('-m', '--model', help="A Model From Huggingface or Local Path")
        parser.add_argument('-d', '--data', help='A Dataset from Hugging Face')
        parser.add_argument('-e', '--entry', help='If the dataset has multiple entries', action='store_true')
        parser.add_argument('-out', '--output', help='A Output Folder ')
        args = parser.parse_args()
        args_dict = vars(args)
        is_sec = args_dict['entry']
        if args_dict['train']:
            ripper = Ripper(args_dict['model'], args_dict['data'], args_dict['output'], args=is_sec)
            ripper.prep_data()
            ripper.start_training()
        else:
            exit('NO OPERATION SPECIFIED')
    except EnvironmentError as e:
        print(f"ERROR PARAMETER SPECIFIED NOT FOUND \n {e}")
    except Exception as e:
        print(f"ERR UNKNOWN ERROR OCCURED {e}")

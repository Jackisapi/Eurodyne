import argparse
from ripper_doc import Ripper

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--model', help="A Model From Huggingface or Local Path")
        parser.add_argument('-d', '--data', help='A Dataset from Hugging Face')
        parser.add_argument('-e','--entry', help='If the dataset has multiple entries')
        parser.add_argument('-out', '--output', help='A Output Folder ')
        args = parser.parse_args()
        args_dict = vars(args)
        if args_dict['entry'] != None:
            is_sec = True
        else:
            is_sec = False

        ripper = Ripper(args_dict['model'], args_dict['data'], args_dict['output'], args=is_sec)
        ripper.prep_data()
        ripper.start_training()
    except EnvironmentError as e:
        print(f"ERROR PARAMETER SPECIFIED NOT FOUND \n {e}")
    except Exception as e:
        print(f"ERR UNKNOWN ERROR OCCURED {e}")
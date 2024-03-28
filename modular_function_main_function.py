import json

"""
**********************************************************
Takes two strings one being a requests the other being the
model used for the request sends the request to the LLM
returns the response
Parameters: Search Queue, Model used
Returns: A Response from your Model of choice
*********************************************************
"""

#DEPRECATED
# def ask_ai(quere, model, debug=False):
#     if debug:
#         tokens = []
#         response = model(prompt=quere)
#         for token in response:
#             tokens.append(token)
#             return response
#         else:
#             response = model(prompt=quere)
#             return response


"""
*************************************************************
Opens "models2.json from the GPT4All Project and prints all
The the Data lables Name filename type Desc and url from 
each object 
Parameters File ("Function Can however be called without
Data file being defined")
Returns: All the Models officialy supported by GPT4ALL
*************************************************************
"""


def all_models(datafile='models2.json'):
    with open(datafile, 'r') as model_data:
        model_dict = json.load(model_data)
        #opens models2.json and converts to a dictionary Then Fetches data that might be useful to the user
    for dict_model in model_dict:
        print('Name:', dict_model['name'], '\n'
                                           'filename:', dict_model['filename'], '\n'
                                                                                'type:', dict_model['type'], '\n'
                                                                                                             'description:',
              dict_model['description'], '\n'
                                         'URL:', dict_model['description'], '\n')


"""
*************************************************************
In development but works mostly at the moment in theory
takes a String Checks to see if that string is a available 
model for gpt4all if not found it will throw an error
Parameters: Name, datafile(doesnt need filled)
Returns: Currently just the name of the model if found
*************************************************************
"""


def model_check(name, datafile='models2.json'):
    with open(datafile, 'r') as model_data:
        model_dict = json.load(model_data)
        #opens models2.json and converts to dictionary

    for dict_model in model_dict:
        #Checks to see if the dictionary has the model specified under ["Name"]
        if not dict_model['name'].upper() in name.upper():
            continue
        # If found will return a file name and a bool (DEBUG)
        return dict_model['filename'], True
    return 'blah', False


def exit_prompt():
    ex_prompt = input('Are you sure you want to exit? ')
    if ex_prompt.upper() == 'Y':
        exit("Have A Nice Day (Program By Jackisapi")
    else:
        pass


"""
*************************************************************
Takes what you are currently using for compute hardware then
prints out all the other current hardware options then takes
input if it matches a hardware option switches to that option
if it doesnt it remains the same 
Parameters: Your current hardware choice
Returns: Your New Hardware choise (if applicable)
*************************************************************
"""


def hw_change(device):
    print('These are the currently supported hardware options \n'
          'cuda (Nvidea based GPUs) \n'
          'vulcan (AMD based GPUs) \n'
          'cpu (cpu compute) \n'
          f'current device is {device} \n')
    dv_change = input('Which device would you like to switch to ? ')
    if dv_change.upper() == 'CUDA' or dv_change.upper() == 'NVIDEA':
        return 'nvidea'
    elif dv_change.upper() == 'VULCAN' or dv_change.upper() == 'AMD':
        return 'amd'
    elif dv_change.upper() == 'CPU':
        return 'cpu'
    else:
        print("Unknown input no change made")
        return device


"""
*************************************************************
Asks the user for input and returns that input however
if the input is ls it calls all_models Soon to be exteneded 
with model_check as seen above 
Params: None
Returns: User Input
*************************************************************
"""


def change_model(current_model):
    change_made = False
    while not change_made:
        model = input('Please enter the name of the model or type ls to list all the available models ')
        if 'ls' in model:
            all_models()
        else:
            model = model_check(model)
            if not model[1]:
                return current_model
            else:
                return model[0]

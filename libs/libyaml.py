import yaml
from libs.libgpt4all import change_model

def yaml_conf(file='conf.yaml'):
    with open(file, 'r') as file:
        cli_conf = yaml.safe_load(file)
        return cli_conf


def config_edit(file='conf.yaml'):
    cli_conf = yaml_conf()
    catagory_change = input("Welcome To The Config Editor Here is what you Can Change \n"
                            "Compute \n"
                            "Model\n ")
    try:
        if catagory_change[0].upper() == "C":
            for key in cli_conf['hardware']:
                if key == 'compute_device':
                    compute_edit = input("Please Enter Your Compute Device Change ")
                    # cli_conf['hardware'][key] = f"'{compute_edit}'"
                    cli_conf['hardware'][key] = compute_edit
                    break
            with open(file, 'w') as file:
                yaml.dump(cli_conf, file)
        elif catagory_change[0].upper() == 'M':
            for key in cli_conf['model']:
                if key == 'default_model':
                    model_set = change_model(cli_conf['model']['default_model'])
                    cli_conf['model']['default_model'] = model_set
                    break
            with open(file,'w') as file:
                yaml.dump(cli_conf,file)

        else:
            print("Sorry Not A Valid Option Exiting")
    except IndexError:
        print("Sorry Not A Valid Option Exiting")

    return cli_conf



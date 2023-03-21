import os
import argparse
import yaml
import logging


# fuction to read parameters

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file) # load the yaml file 
    return config 


def main(config_path, datasource):
    config = read_params(config_path) # gets dictionary format parameters
    print(config)


if __name__ == "__main__":
    args = argparse.ArgumentParser() # for argument when file run from terminal
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default= default_config_path)
    args.add_argument("--datasource", default = None) # another argument like data files

    parsed_args = args.parse_args()
    # print("Parsed_args : ", parsed_args)
    # for config parsed_args.config and for data source parsed_args.datasource

    main(config_path = parsed_args.config, datasource = parsed_args.datasource)



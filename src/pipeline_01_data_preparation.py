import os
import argparse
import yaml
import logging

if __name__ == "__main__":
    args = argparse.ArgumentParser() # for argument when file run from terminal
    args.add_argument("--config", default= "default")
    args.add_argument("--datasource", default = None) # another argument like data files

    parsed_args = args.parse_args()
    print("Parsed_args : ", parsed_args)
    # for config parsed_args.config and for data source parsed_args.datasource

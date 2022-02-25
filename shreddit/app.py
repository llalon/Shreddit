"""This module contains script entrypoints for shreddit.
"""
import argparse
import yaml
import logging
import os
import pkg_resources
from shreddit import default_config
from shreddit.shredder import Shredder

CONFIG_FILE_PATH = "/app/config/shreddit.yml"


def generate_empty_config(path: str):
    print("Writing shreddit.yml file...")
    with open(path, "wb") as f_out:
        f_out.write(pkg_resources.resource_string("shreddit", "shreddit.yml.example"))


def main():
    if not os.path.isfile(CONFIG_FILE_PATH):
        print("No shreddit configuration file was found or provided.")
        generate_empty_config(CONFIG_FILE_PATH)
        return

    with open(CONFIG_FILE_PATH) as fh:
        # Not doing a simple update() here because it's preferable to only set attributes that are "whitelisted" as
        # configuration options in the form of default values.
        user_config = yaml.safe_load(fh)
        for option in default_config:
            if option in user_config:
                default_config[option] = user_config[option]

    shredder = Shredder(default_config)
    shredder.shred()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shreddit aborted by user")
        quit()

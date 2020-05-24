#!/usr/bin/env python3
import argparse
from os import listdir, system
from os.path import isdir, isfile, join


parser = argparse.ArgumentParser(
    description="Encrypts all files in an Ansible inventories directory")
parser.add_argument(
    "--inventories-path", "-i",
    type=str,
    help="path to ansible inventories",
    required=True,
)
parser.add_argument(
    "--password-file", "-p",
    type=str,
    help="path to password file",
    required=True,
)
args = parser.parse_args()
inventories_path = args.inventories_path
password_file = args.password_file


files_to_encrypt = []


def run():
    get_files(inventories_path)
    encrypt_files()


def get_files(path):
    for item in listdir(path):
        item_path = join(path, item)
        if isdir(item_path):
            get_files(item_path)

    files_to_encrypt.extend([
        join(path, _file) for _file
        in listdir(path)
        if isfile(join(path, _file))
    ])


def encrypt_files():
    for _file in files_to_encrypt:
        system(f"ansible-vault encrypt --vault-id {password_file} {_file}")


if __name__ == "__main__":
    run()

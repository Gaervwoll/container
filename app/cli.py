import argparse
from main import FileManager

def parse_args():
    parser = argparse.ArgumentParser(description="Container for storing files")
    parser.add_argument("--path", type=str, help="Path to the container")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the container")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the container")
    return parser.parse_args()


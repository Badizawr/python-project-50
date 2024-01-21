import argparse

parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.',
                    epilog='show this help message and exit')

parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()




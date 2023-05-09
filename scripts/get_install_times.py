import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to the packages')


def get_install_times(path):
    packages = os.listdir(path)
    for p in packages:
        if p.startswith('.'):
            continue
        hash_folder = os.listdir(os.path.join(path, p))[0]
        try:
            with open(os.path.join(path, p, hash_folder, '.spack', 'install_times.json'), 'r') as f:
                data = json.load(f)
                print(p, data['total']['seconds'])
        except FileNotFoundError:
            print(f'{p}: spack install time not found')


if __name__ == '__main__':
    args = parser.parse_args()
    get_install_times(args.path)

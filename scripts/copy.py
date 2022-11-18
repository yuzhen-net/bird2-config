import os
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError()
    for i in os.listdir('bird'):
        if os.path.isfile(f'bird/{i}'):
            os.system(f'cp bird/{i} bird/{sys.argv[1]}/')
            
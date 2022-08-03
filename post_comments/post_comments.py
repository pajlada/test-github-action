#!/usr/bin/env python3

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == "__main__":
    print("post_comments hello")
    list_files('.')
    with open('clang-tidy-review.yaml', 'r') as f:
        print(f.read())
    print("post_comments bye")

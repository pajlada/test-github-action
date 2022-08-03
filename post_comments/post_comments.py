#!/usr/bin/env python3

if __name__ == "__main__":
    print("post_comments hello")
    with open('clang-tidy-review/clang-tidy-review.yaml', 'r') as f:
        print(f.read())
    print("post_comments bye")

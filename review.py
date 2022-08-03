#!/usr/bin/env python3

# clang-tidy review
# Copyright (c) 2020 Peter Hill
# SPDX-License-Identifier: MIT
# See LICENSE for more information

import argparse
import contextlib
import datetime
import itertools
import fnmatch
import json
import os
from operator import itemgetter
import pathlib
import pprint
import re
import requests
import subprocess
import textwrap
import unidiff
import yaml
from github import Github
from github.Requester import Requester
from github.PaginatedList import PaginatedList
from typing import List


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a review from clang-tidy warnings"
    )
    parser.add_argument("--token", help="github auth token")

    args = parser.parse_args()

    with open('clang_tidy_review.yaml', 'w') as f:
        f.write('foobar')

    github = Github(args.token)

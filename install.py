#!/usr/bin/env python3

import json
import os
from subprocess import call

def main():
    workspace = json.load(open('./sagiri.code-workspace'))

    for repository in workspace['folders']:
        repo = repository['path']
        if not os.path.exists(repo):
            print(f'Cloning {repo}')
            call(['git', 'clone', f'git@github.com:sagiri-bot/{repo}.git', repo])

if __name__ == '__main__':
    main()
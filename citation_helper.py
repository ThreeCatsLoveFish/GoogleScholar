#! /usr/bin/env python
"""
Given a list of papers in the file `data/paper_list.txt`.
This script can be used to get the citations of the papers in the list.
Please make sure to update the `author` variable with your name.
"""
import os
from tqdm import tqdm

author = "Your Name"

def get_citations(citation):
    os.makedirs('data/output', exist_ok=True)
    filename = f'data/output/{"_".join(citation.replace(":", "-").split(" "))}.bib'
    cmd = f'python scholar.py --citations-only -c 150 -a "{author}" --phrase "{citation}" --config-file data/config.json -o {filename}'
    print(cmd)
    if not os.path.exists(filename):
        os.system(cmd)

def main():
    with open('data/paper_list.txt', 'r') as file:
        citations = file.readlines()
        citations = [citation.strip() for citation in citations]
    for citation in tqdm(citations, desc='Citations'):
        get_citations(citation)


if __name__ == '__main__':
    main()

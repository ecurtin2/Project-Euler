from bs4 import BeautifulSoup
import os
import requests
import re
import json
from pprint import pprint


def parse_euler(start, end):
    data = {}
    for i in range(start, end + 1):

        try:
            url = 'https://projecteuler.net/problem=' + str(i)

            r = requests.get(url)

            soup = BeautifulSoup(r.text, 'lxml')
            divs = soup.findAll("div", {"class": "problem_content"})

            for line in divs:
                s = str(line)
            s = re.sub('<.*?>', "", s)
            data[i] = s
        except:
            data[i] = 'Unknown'
    return data


with open('eulerprobs.json', 'r') as f:
    data = json.load(f)

    for k, val in data.items():
        fname = './src/{0:03}.py'.format(int(k))
        header = '"""\n' + val + '\n"""\n\n'
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                s = f.read()
            with open(fname, 'w') as f:
                f.write(header + s)
        else:
            print(header)

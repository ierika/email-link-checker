#!/usr/bin/env Python3
'''
It's time to move on. Ditch Python2.
'''
import sys
import os
import re
import subprocess
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Prompter:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, text):
        self.text = text

    def error(self):
        return self.FAIL + self.text + self.ENDC

    def success(self):
        return self.OKGREEN + self.text + self.ENDC

    def warning(self):
        return self.WARNING + self.text + self.ENDC

    def message(self):
        return self.OKBLUE + self.text + self.ENDC


def main(args):
    check_requirements()
    try:
        args = args[1]
    except:
        print('Please provide a URL or a file')
        exit(1)
    bsObj = None
    if (args.startswith('http://') or
        args.startswith('https://')):
        print(Prompter('Checking links from a URL').message())
        html = get_url_content(args)
    elif os.path.isfile(args):
        print(Prompter('Checking links from a file').message())
        with open(args, 'r') as f:
            html = f.read()
            bsObj = BeautifulSoup(html, "html.parser")
    else:
        print('{} is not a valid URL or file').format(args)
        exit(1)

    bsObj = BeautifulSoup(html, "html.parser")
    urls = get_urls(bsObj)
    check_urls(urls)

def get_url_content(url):
    html = None
    try:
        html = urlopen(url)
        print('URL Passed')
    except KeyboardInterrupt as e:
        print(Prompter('Aborting...').error())
        exit(2)
    except:
        print(Prompter('URL Exception').error())
        # if result is an error. Open the URL at the browser.
        # Macs only since Linux open commands varies per distro.
        uname = subprocess.check_output('uname', shell=True)
        if 'Darwin' in str(uname):
            os.system('open -g {}'.format(url))
        return None
    return html

def check_requirements():
    if os.name is not 'posix':
        print('This script currently only supports Unix-like OS\'s.')
        exit(1)

def clear_screen():
    os.system('clear')

def check_urls(urls):
    results = []
    for url in urls:
        print(Prompter('Checking - {}'.format(url)).message())
        html = get_url_content(url)
        if html:
            results.append(Prompter(url).success())
        else:
            results.append(Prompter(url).error())
        clear_screen()
        for result in results:
            print(result)

def get_urls(bsObj):
    # Extract links
    bs_links = bsObj.findAll('a')
    links = []
    if len(bs_links) > 0:
        for bs_link in bs_links:
            if bs_link.has_attr('href'):
                link = bs_link['href']
                if link.startswith('http://') or link.startswith('https://'):
                    links.append(link.strip())
    if len(links) <= 0:
        print('This HTML does not contain any links.')
        exit(1)
    return links

# Process files only one at a time for now
main(sys.argv)
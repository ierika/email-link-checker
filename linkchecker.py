#!/usr/bin/env Python3
'''
It's time to move on. Ditch Python2.
'''
import sys
import os
import webbrowser
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
        return self.FAIL + 'ERROR: ' + self.text + self.ENDC

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
    if args.startswith('http://'):
        print(Prompter('Checking links from a URL').message())
        html = get_url_content(args)
    elif os.path.isfile(args):
        print(Prompter('Checking links from a file').message())
        with open(args, 'r') as f:
            html = f.read()
    else:
        print(Prompter('{} is not a valid URL or file.'.format(args)).error())
        exit(1)

    bsObj = BeautifulSoup(html, "html.parser")
    urls = get_urls(bsObj)
    check_urls(urls)
    print(Prompter('Done').message())


def get_url_content(url):
    html = None
    try:
        html = urlopen(url)
    except KeyboardInterrupt as e:
        print(Prompter('Aborting...').error())
        exit(2)
    except:
        webbrowser.open_new_tab(url)
        return None
    return html


def check_requirements():
    if os.name is not 'posix':
        print('This script currently only supports Unix-like OS\'s.')
        exit(1)


def clear_screen():
    os.system('clear')


def check_urls(urls):
    for url in urls:
        html = get_url_content(url)
        if html:
            print(Prompter(url).success())
        else:
            print(Prompter(url).error())


def get_urls(bsObj):
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


if __name__ == '__main__':
    main(sys.argv)

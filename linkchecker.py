#!/usr/bin/env Python3

"""
HTML and text email link checker.

It only looks for absolute/full URL's in an HTML web page or text file.
This script accepts a URL and a file as argument.
Any HTTP response that is not an OK response (HTTP 200) will be considered,
an error.
All URLs that had error will be automatically opened in a browser -
so it can be double checked.
"""

import sys
import os
import re
import webbrowser
import mimetypes
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


class Main:
    allowed_protocols = ('http://', 'https://')
    allowed_mimetypes = ('text/plain', 'text/html')

    def __init__(self, args=None):
        # Check requirements
        self.check_requirements()

        # If the user provided no arguments, spit out an error.
        # If arguments were provided slice the first argument off.
        # The first argument will be this script and we don't need that
        if len(args) <= 1:
            print(Prompter('Please provide an URL or a file').warning())
            exit(1)
        else:
            args = args[1:]

        for arg in args:
            # Reset URL list on each iteration
            urls = None
            if arg.startswith(self.allowed_protocols):
                # Process URL
                print(Prompter('Checking links from a URL').message())
                html = self.get_url_content(arg)
                urls = self.parse_html_urls(html)
            elif os.path.isfile(arg):
                # Process files
                mime, encoding = self.guess_mimetype(arg)
                print(
                    Prompter(
                        'Checking links from a {} file: {}'.format(mime, arg)
                    ).message()
                )

                with open(arg, 'r', encoding="utf-8") as f:
                    file_contents = f.read()

                if mime == self.allowed_mimetypes[0]:  # text/plain
                    urls = self.parse_text_urls(file_contents)
                elif mime == self.allowed_mimetypes[1]:  # text/html
                    urls = self.parse_html_urls(file_contents)
                else:
                    print(
                        Prompter(
                            '{} mimetype not allowed.'.format(mime)
                        ).error()
                    )
                    exit(1)
            else:
                print(
                    Prompter(
                        '{} is not a valid URL or file.'.format(arg)
                    ).error()
                )

            if urls:
                print(Prompter(
                    'Checking {} URL(s)...'.format(len(urls))
                ).message())
                self.check_urls(urls)
                print(Prompter('Done').message())
                print()  # An empty line

    @staticmethod
    def guess_mimetype(file):
        """
        Guesses a file's mimetype and encoding.
        """
        mime, encoding = mimetypes.guess_type(file)
        return mime, encoding

    @staticmethod
    def get_url_content(url):
        """
        Checks an URL whether it's returning an OK response or not.

        Anything other than HTTP 200 is considered not ok.
        """
        html = None
        # noinspection PyBroadException
        try:
            html = urlopen(url)
        except KeyboardInterrupt:
            print(Prompter('Aborting...').error())
            exit(2)
        except Exception:
            webbrowser.open_new_tab(url)
            return None
        return html

    @staticmethod
    def check_requirements():
        """
        Checks whether the script is compatible with the OS
        """
        if os.name is not 'posix':
            print('This script currently only supports Unix-like OS\'s.')
            exit(1)

    @staticmethod
    def clear_screen():
        """
        Clears console screen
        """
        os.system('clear')

    def check_urls(self, urls):
        """
        Checks each URLs from an URL set.

        Sorted just to make it look organized.
        """
        for url in urls:
            html = self.get_url_content(url)
            if html:
                print(Prompter(url).success())
            else:
                print(Prompter(url).error())

    def parse_html_urls(self, file_contents):
        """
        Looks for all anchor tags with an absolute URL in an HTML doc.
        """
        soup = BeautifulSoup(file_contents, "html.parser")
        bs_links = soup.findAll('a')
        urls = []
        if len(bs_links) > 0:
            for bs_link in bs_links:
                if bs_link.has_attr('href'):
                    link = bs_link['href'].strip()
                    if link.startswith(self.allowed_protocols):
                        if link not in urls:
                            urls.append(link)
        else:
            print('This HTML does not contain any links.')
            exit(1)
        return tuple(urls)

    @staticmethod
    def parse_text_urls(file_contents):
        """
        Parses text file for absolute URLs
        """
        pattern = r'((https|http)://[\w\d\.\=\#\_\+\!\&\%\/\?\-]+)'
        matches = re.findall(pattern, file_contents)
        urls = []
        if matches:
            for match in matches:
                url = match[0]
                if url not in urls:
                    urls.append(url)
        return tuple(urls)


if __name__ == '__main__':
    Main(sys.argv)

A simple command-line link checker.
It could only check only one HTML page at a time, to avoid chaos.

What it does are:
- Checks all anchor tags in an HTML document (from file or a URL).
- Opens the link with an error in the browser, so we could double check. If it is
  really working or not.

This tool will also be used in Email Alert Helper tool. Once integrated, this repo will be erased.

Working but still undergoing enhancements.
Support for non HTML docs will also be added.

## How to install

1. Download and install [_Python 3_](https://www.python.org/downloads/)
2. Once Python 3 has been installed. Install PIP(a Python package management system).

```shell
$ curl https://bootstrap.pypa.io/get-pip.py | python3
```

3. Install requirements from `requirements.txt`.

```shell
$ cd /path/to/linkchecker/directory
$ python3 -m pip install -r requirements.txt
```

## How to use
You could export its path and change permission to make it executable. 

```shell
$ cd /path/to/linkchecker/directory
$ chmod u+x linkchecker.py
$ echo 'export PATH=${PATH}:/path/to/linkchecker' >> ~/.bash_profile
$ source ~/.bash_profile
```

After the PATH has been exported. We could now execute it anywhere.

```shell
$ linkchecker /path/to/html/or/link/to/page
```

...or, Just execute it directly.

```shell
$ cd /path/to/linkchecker/directory
$ python3 linkchecker path/to/html/file
```

```shell
$ cd /path/to/linkchecker/directory
$ python3 linkchecker https://path/to/web/page
```
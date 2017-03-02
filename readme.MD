A simple command-line link checker.
It could only check only one HTML or one URL at a time, to avoid chaos.

This tool will also be used in Email Alert Helper tool. Once integrated, this repo will be erased.

Working but still undergoing enhancements.
Support for non HTML docs will also be added.

## How to install

1. Download [_Python 3_](https://www.python.org/downloads/)
2. Once Python 3 has been installed. Install PIP(a Python package management system).

```shell
$ curl https://bootstrap.pypa.io/get-pip.py | python3
```

3. Install requirements from `requirements.txt`.

```shell
$ python3 -m pip install -r requirements.txt
```

## How to use
You could export its path and change permission to make it executable.

```shell
$ chmod u+x linkchecker.py
$ echo 'export PATH=${PATH}:/path/to/linkchecker' >> ~/.bash_profile
```

OR

Just execute it directly.

```shell
python3 linkchecker.py path/to/html/file
```

```shell
python3 linkchecker.py https://path/to/web/page
```
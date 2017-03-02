A simple command-line link checker.
It could only check only one HTML or one URL at a time, to avoid chaos.

This tool will also be used in Email Alert Helper tool. Once integrated, this repo will be erased.

## How to install

1. Download [_Python 3_](https://www.python.org/downloads/)
2. Once Python 3 has been installed. Install PIP(a Python package management system).
```
$ curl https://bootstrap.pypa.io/get-pip.py | python3
```
3. Install requirements from `requirements.txt`.
```
$ python3 install -r requirements.txt
```

## How to use
You could export its path and change permission to make it executable.
```
$ chmod u+x linkchecker.py
$ echo 'export PATH=${PATH}:/path/to/linkchecker' >> ~/.bash_profile
```

OR

Just execute it directly.
```
python3 linkchecker.py path/to/html/file
```
```
python3 linkchecker.py https://path/to/web/page
```
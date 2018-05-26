# Email Link Checker

A simple command-line link checker to aid my work.
It simply checks for dead links or links that returns anything other than HTTP 200.
All links that failed will be automatically opened in a browser.
It could only check one HTML or text email at a time.
You could chain commands if you want to check multiple files.

## How to install

1. Download and install [_Python 3_](https://www.python.org/downloads/)

2. Install certificate for HTTPS support (optional). HTTPS pages will show as error if not installed.
   For Macs: Go to `/Applications/Python 3.6/` and double click the executable called `Install Certificates.command`.
   For other OS's: Gooogle it.

3. Once Python 3 has been installed. Install PIP(a Python package management system).

```shell
$ curl https://bootstrap.pypa.io/get-pip.py | python3
```

4. Install requirements from `requirements.txt`.

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
$ python3 linkchecker http://path/to/web/page
```

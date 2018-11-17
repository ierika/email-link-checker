# Email Link Checker

A simple command-line link checker for HTML and text emails.
That means it will only look for absolute URLs.

Supports HTTPS if certificates are installed.

A simple command-line link checker to aid my work.
It simply checks for dead links or links that returns anything other than HTTP 200 (redirects are OK).
All links that failed will be automatically opened in a browser.

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
For URLs:
```bash
$ linkchecker https://www.domain.com/email_1.html https://www.domain.com/email_2.html
```

For files:
```shell
$ linkchecker /path/to/html/or/link/to/page /path/to/another/file
```

It also support wild cards.
```bash
$ linkchecker /path/to/html/*.html
```

You can also execute it directly by running it through `python3` command.

```shell
$ cd /path/to/linkchecker/directory
$ python3 linkchecker path/to/html/file
```

```shell
$ cd /path/to/linkchecker/directory
$ python3 linkchecker http://path/to/web/page
```

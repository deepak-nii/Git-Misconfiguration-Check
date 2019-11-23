# Git-Misconfiguration-Check

A very simple python code to find websites whose git repository is available to the public.

## Usage

This script supports both Python 2.x and Python 3.x

```bash
$ git_file_disclosure.py [-h] file
```

## Example
The input file should contain domains one per line. The script will output discovered domains.

```bash
$ python3 git_file_disclosure.py domain.txt 
www.connorrealestate.com is vulnerable
codemirror.net is vulnerable
```

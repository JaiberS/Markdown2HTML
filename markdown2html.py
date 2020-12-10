#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from os import path

    error = None
    if len(sys.argv) < 2:
        error = 'Usage: ./markdown2html.py README.md README.html'
    elif not path.exists(sys.argv[1]):
        error = 'Missing ' + sys.argv[1]
    if error is not None:
        sys.stderr.write(error)
        exit(1)
    exit(0)

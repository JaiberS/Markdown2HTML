#!/usr/bin/python3
"""
0. Start a script
"""


if __name__ == "__main__":
    import sys
    from os import path

    error = None
    if len(sys.argv) < 2:
        error = 'Usage: ./markdown2html.py README.md README.html'
    elif not path.exists(sys.argv[1]) or not path.isfile(sys.argv[1]):
        error = 'Missing ' + sys.argv[1]
    if error is not None:
        sys.stderr.write(error + '\n')
        exit(1)

    Markdown = open(sys.argv[1])
    linesList = Markdown.readlines()
    for i in range(len(linesList)):
        counter = linesList[i].count('#')
        linesList[i] = linesList[i].replace('#', '')
        linesList[i] = linesList[i].replace('\n', '')
        linesList[i] = '<h' + str(counter) + '>' + linesList[i][1:] + '</h' + str(counter) + '>\n'
    linesAgain = ''.join(linesList)
    outputFile = open(sys.argv[2], 'w')
    outputFile.write(linesAgain)
    Markdown.close()
    outputFile.close()
    exit(0)

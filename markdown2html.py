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
    ul = False
    ol = False
    paragraph = False
    for i in range(len(linesList)):
        linesList[i] = linesList[i].replace('**', '<b>', 1)
        linesList[i] = linesList[i].replace('**', '</b>', 1)
        linesList[i] = linesList[i].replace('__', '<em>', 1)
        linesList[i] = linesList[i].replace('__', '</em>', 1)
        if paragraph == True:
            if linesList[i][0].isalpha():
                linesList[i] = '<br/>\n' + linesList[i]
            if linesList[i] == '\n':
                linesList[i] = '</p>\n'
                paragraph = False
            if linesList[i] == linesList[-1]:
                linesList[i] = linesList[i] + '\n</p>'
        if linesList[i][0].isalpha() or linesList[i][0:3] == '<b>' or linesList[i][0:3] == '<em>':
            if paragraph == False:
                paragraph = True
                if linesList[i - 1] != '\n':
                    linesList[i - 1] = linesList[i - 1] + '<p>\n'
                else:
                    linesList[i - 1] = '<p>' + linesList[i - 1]
                if linesList[i] == linesList[-1]:
                    linesList[i] = linesList[i] + '</p>\n'
        if linesList[i][0] == '#':
            counter = linesList[i].count('#')
            linesList[i] = linesList[i].replace('#', '')
            linesList[i] = linesList[i].replace('\n', '')
            linesList[i] = '<h' + str(counter) + '>' + linesList[i][1:] + '</h' + str(counter) + '>\n'
        if linesList[i][0] == '-':
            linesList[i] = linesList[i].replace('-', '')
            linesList[i] = linesList[i].replace('\n', '')
            linesList[i] = '<li>' + linesList[i][1:] + '</li>\n'
            if not ul:
                ul = True
                linesList[i] = '<ul>\n' + linesList[i]
            if linesList[i] == linesList[-1]:
                linesList[i] = linesList[i] + '</ul>\n'
        elif ul == True:
            ul = False
            linesList[i - 1] = linesList[i - 1] + '</ul>\n'
        if linesList[i][0] == '*':
            linesList[i] = linesList[i].replace('*', '')
            linesList[i] = linesList[i].replace('\n', '')
            linesList[i] = '<li>' + linesList[i][1:] + '</li>\n'
            if not ol:
                ol = True
                linesList[i] = '<ol>\n' + linesList[i]
            if linesList[i] == linesList[-1]:
                linesList[i] = linesList[i] + '</ol>\n'
        elif ol == True:
            ol = False
            linesList[i - 1] = linesList[i - 1] + '</ol>\n'
    linesAgain = ''.join(linesList)
    outputFile = open(sys.argv[2], 'w')
    outputFile.write(linesAgain)
    Markdown.close()
    outputFile.close()
    exit(0)

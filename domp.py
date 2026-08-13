#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys, os, fnmatch
#from pygments import highlight
#from pygments.lexers import *
#from pygments.formatters import HtmlFormatter
from string import *
import multiprocessing

files_list = []

def findReplace(directory, find, replace, filePattern):
        global files_list
        for path, dirs, files in os.walk(os.path.abspath(directory)):
                for filename in fnmatch.filter(files, filePattern):
                        filepath = os.path.join(path, filename)
                        #print filepath
                        files_list.append(filepath)


def setup(files):
    jobs = []
    for i in range(len(files)):
        p = multiprocessing.Process(target=process, args=(files[i],))
        jobs.append(p)
        p.start()


def process(filepath):
    #print "in process"
    print(filepath)
    with open(filepath, 'rb') as f:
            # print "opened " + filepath
            l = filepath.split('/')
            name = ''
            if(l[len(l) -2]) == 'build':
                name = l[len(l) - 1]
            s = f.read()
            #s = s.replace(find, replace)
            s = s.replace(b"index.html", b"")
            s = s.replace(b"<html>", b"<!DOCTYPE html>")
            s = s.replace(b'<meta', b"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><meta")
            soup = BeautifulSoup(s, "lxml")

            for i in soup.find_all("table", attrs={"summary": "Navigation header"}):
                    i.contents[0].contents[0].clear()
                    if name == "index.html":
                            link = BeautifulSoup("<a href=\"ix01.html\">Index</a>", "lxml")
                    elif name =="ix01.html":
                            link = BeautifulSoup("", "lxml")
                    else:
                            link = BeautifulSoup("<a href=\"../ix01.html\">Index</a>", "lxml")
                            i.contents[0].contents[0].insert(0, link)
                    if name == "index.html":
                            link = BeautifulSoup("", "lxml")
                    elif name == "ix01.html":
                            link = BeautifulSoup("<a href=\"index.html\">Table of Contents</a>", "lxml")
                    else:
                            link = BeautifulSoup("<a href=\"../\">Table of Contents</a>", "lxml")
                            i.contents[1].contents[1].insert(0, link)
            soup = BeautifulSoup(soup.renderContents(), "lxml")
            for j in soup.findAll("table", attrs={"summary": "Navigation footer"}):
                   if name == "index.html":
                           link = BeautifulSoup("<a href=\"ix01.html\">Index</a>", "lxml")
                   elif name == "ix01.html":
                           link = BeautifulSoup("", "lxml")
                   else:
                           link = BeautifulSoup("<a href=\"../ix01.html\">Index</a>", "lxml")
                   j.contents[0].contents[1].insert(0, link)
                   if name == "ix01.html":
                           link = BeautifulSoup("<a href=\"index.html\">Table of Contents</a>", "lxml")
                   if name == "index.html":
                           link = BeautifulSoup("", "lxml")
                   elif name == "ix01.html":
                           link = BeautifulSoup("<a href=\"index.html\">Table of Contents</a>", "lxml")
                   else:
                           link = BeautifulSoup("<a href=\"../\">Table of Contents</a><br/>", "lxml")
                   #j.contents[0].contents[1].insert(0, link)
                   #print(j)
                   j.contents[1].contents[1].clear()
                   j.contents[1].contents[1].insert(0, link)
                # Now mathjax removed
            p = BeautifulSoup('<h3><a href="/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16"><path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/></svg></i> Home</a></h3>', "lxml")
            # print(f)
            soup.body.insert(0, p)
            soup = BeautifulSoup(soup.renderContents(), "lxml")
#                                for i in soup.find_all("pre", "CommonLispLexer"):
#                                        code = BeautifulSoup(highlight(i.string, CommonLispLexer(), HtmlFormatter()))
#                                        i.string.replace_with(code)
#            soup = BeautifulSoup(soup.renderContents(), "lxml")
#syntax highlighting is not needed for algebra
#            for i in soup.find_all("pre", "CLexer"):
#                   #print i.string
#                   code = BeautifulSoup(highlight(i.string, CLexer(), HtmlFormatter()), "lxml")
#                   i.string.replace_with(code)
#            soup = BeautifulSoup(soup.renderContents(), "lxml")
#            for i in soup.find_all("pre", "ALexer"):
#                   code = BeautifulSoup(highlight(i.string, CObjdumpLexer(), HtmlFormatter()), "lxml")
#                   i.string.replace_with(code)
#            soup = BeautifulSoup(soup.renderContents(), "lxml")
#            for i in soup.find_all("pre", "MakefileLexer"):
#                   code = BeautifulSoup(highlight(i.string, MakefileLexer(), HtmlFormatter()), "lxml")
#                   i.string.replace_with(code)
            with open(filepath, "w") as f:
                   #print "Hello"
                   f.write(soup.decode(formatter='html'))


if __name__ == "__main__":
    findReplace("build/", "mml:", "", "index.html")
    findReplace("build/", "mml:", "", "ix01.html")
    findReplace("build/", "mml:", "", "pt01.html")
    findReplace("build/", "mml:", "", "pt02.html")
    #print files_list
    multiprocessing.freeze_support()
    setup(files_list)

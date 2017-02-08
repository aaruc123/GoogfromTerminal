#! usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import webbrowser

def callToGoogle(query):
    URL = 'http://www.google.com/search?q=$'
    finalURL = URL + FinalQuery
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(finalURL, headers=headers)
    encoded = source_code.text
    finalCodeToScrap = encoded.encode('utf-8')
    formattedResults(finalCodeToScrap)


def formattedResults(htmlSource):
    result = []
    resultlinks = []
    counter = 0
    soup = BeautifulSoup(htmlSource, 'html.parser')
    for head1 in soup.findAll('h3', {'class': 'r'}):
        if head1.span == None:
            counter = int(counter) + 1
            print '\n'
            content = head1.string
            contentlink = head1.a['href']
            result.append(content)
            resultlinks.append(contentlink)
            print str(counter) + ". " + content
            print contentlink

    print '\n'
    print 'Enter the link number you want to open. Enter for Exit'
    valueinputted = raw_input()
    value = 0
    if valueinputted == "":
        sys.exit()
    value = int(valueinputted)
    urlChoosen = resultlinks[value - 1]
    print urlChoosen;
    chrome_path = '/usr/bin/google-chrome %s'
    firefox_path = '/usr/bin/firefox %s'
    if webbrowser.get(chrome_path).open(urlChoosen) == False:
        webbrowser.get(firefox_path).open(urlChoosen)




query = sys.argv[1:]
FinalQuery = ""
length = len(sys.argv)
for x in sys.argv[1:]:
    if FinalQuery == "":
        FinalQuery = FinalQuery + x
    else:
        FinalQuery = FinalQuery + "+" + x
callToGoogle(FinalQuery)



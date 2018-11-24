import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import urllib.request

directory = os.fsencode("D://GitHubCommitsCollector//XMLPages//")

for file in os.listdir(directory):

    filename = os.fsdecode(file)
    with open(os.path.join(directory,file),encoding="ANSI",errors="surrogateescape") as myfile:
        r = myfile.read()
        print(r)
        e = ET.parse(myfile)
        root = e.getroot()
        for child in root:
            print(child.tag, child.attribute)
    exit()
# with open("D://GitHubCommitsCollector/XMLPagesLinks.txt", "r",encoding= "utf-8",) as linksfile:
#     linksfile.readlines()
#     for line in linksfile:
#         sauce = urllib.request.urlopen("{}").format(line).read()
#         soup = bs.BeautifulSoup(sauce, "lxml")
#         type = soup.type
#         print(soup.type)



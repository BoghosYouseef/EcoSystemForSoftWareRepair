# import xml.etree.ElementTree as ET
import sys
from xml.dom import minidom
import re
import os
# with open("D://GitHubCommitsCollector//XMLPages//ENTESB-3040.xml",encoding="utf-8",errors='ignore') as file:
#     data = file.read()
#     data.encode('utf-8').strip()
#     e = ET.parse(data)

if __name__ == '__main__':
    directory = os.fsencode("D://GitHubCommitsCollector//XMLPages//")
    for file in directory:
        with open(file, "r"):
            DataToBeParsed = file.read()
            try:
                DataToBeParsed.splitlines()
                data = minidom.parse(DataToBeParsed)
                tags = data.GetElementsByTagName("type")
                document = tags.GetElementsByTagName("status")
                for type in tags:
                    print(type)
            except ValueError:
                raise
        file.close()
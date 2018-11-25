from bs4 import BeautifulSoup as soup
import os
directory = os.fsencode("D://GitHubCommitsCollector//XMLPages//")
                                                                            # FileName = os.listdir(directory)
# FileNameLists = FileName.readlines()
# for name in FileNameLists:
#     with open(directory+"{}".format(name), "r") as FileToBeParsed:
#         FileContent = FileToBeParsed.read().splitlines()
#         ParsedFileContent = soup(FileContent,"html.parser")
#         print(ParsedFileContent.findall("type"))
#                                                                             elements = ['%{0}%'.format(FileName) for element in FileName]
#                                                                             for element in elements:
#                                                                                 openfile = open("D://GitHubCommitsCollector//XMLPages//{}".format(element) , "r")
#                                                                                 readfile = openfile.read().splitlines()
#                                                                                 blob = soup(readfile.findall(),"html.parser")
#                                                                                 closefile = openfile.close()
import os
for filename in os.listdir("D://GitHubCommitsCollector//XMLPages//"):
    readfile = open(filename, "r", encoding="ANSI")
    content = readfile.readlines()
    blob = soup(content.findall("<build-number>",))
    print(blob)
